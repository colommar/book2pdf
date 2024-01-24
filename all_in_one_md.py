import codecs
import warnings
from pathlib import Path

import pdfkit
from markdown import markdown


class GitBook:
    __slots__ = (
        "working_directory",
        "output_filepath",
        "tmp_md_filepath",
        "encoding",
        "recursive",
    )

    def __init__(
        self,
        working_directory: str,
        output_filepath: str,
        encoding: str,
        recursive: bool,
    ):
        """见main.py中的argparse部分。"""
        self.working_directory = Path(working_directory)
        if not self.working_directory.is_dir():
            raise ValueError(f"{self.working_directory} is not a directory.")
        self.output_filepath = Path(output_filepath)
        if self.output_filepath.exists():
            warnings.warn("The output file already exists and will be overwritten.")
        self.tmp_md_filepath = self.output_filepath.with_suffix(".md").absolute()
        if self.tmp_md_filepath.exists():
            warnings.warn(
                "The temporary markdown file already exists and will be overwritten."
            )
        self.encoding = codecs.lookup(encoding).name
        self.recursive = recursive

    def _find_markdowns(self):
        pattern = "**/*.md" if self.recursive else "*.md"

        def not_opt(fp: Path):
            return fp.absolute() != self.tmp_md_filepath  # tmp_md_filepath已保证为绝对路径

        for f in filter(not_opt, self.working_directory.glob(pattern)):
            yield (
                f.read_text(encoding=self.encoding)
                .replace("# ", "## ")
                .replace("## 第", "# 第")
            )

    def _convert(self, html: str):
        pdfkit.from_string(
            markdown(html, extensions=["extra", "codehilite"], output_format="html"),
            self.output_filepath,
            configuration=pdfkit.configuration(
                wkhtmltopdf="wkhtmltopdf/wkhtmltopdf.exe"
            ),
            options={"encoding": self.encoding},
        )

    def merge(self):
        """将指定工作路径下的md文件合并成一个md文件并写入到指定的输出文件中。"""
        with open(self.tmp_md_filepath, "w", encoding=self.encoding) as f:
            f.writelines(self._find_markdowns())

    def convert(self):
        """将指定的md文件转换成pdf文件。"""
        with open(self.tmp_md_filepath, encoding=self.encoding) as f:
            html = f.read()
        self._convert(html)

    def merge_and_convert(self):
        """将指定工作路径下的md文件合并成一个md文件并转换成pdf文件。"""
        self._convert("\n".join(self._find_markdowns()))
