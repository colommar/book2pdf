from typing import Union
from pathlib import Path
import codecs
import chardet
from markdown2pdf import convert

def merge_md(root: Path = Path('C:\\Users\\114514\\Desktop\\print\\gitbook_name'),
             dest_file: Path = Path('C:\\Users\\114514\\Desktop\\print\\gitbook_name\\.gitbook\\all_in_one.md'),
             dest_encoding: str = 'utf8',
             recurse: bool = True,
             ):
    
    root, dest_file = Path(root), Path(dest_file)

    if not root.is_dir():
        return

    pattern = '**/*.md' if recurse else '*.md'

    with open(dest_file, 'w', encoding=dest_encoding) as dest:
        for txt in Path(root).glob(pattern):
            if txt.absolute() == dest_file.absolute():
                continue

            print(txt.__str__() + "\n")

            text = txt.read_text(encoding='utf8')
            strContent = text.replace("# ", "## ")
            strContent = strContent.replace("## 第", "# 第")
            print(strContent)
            dest.write(strContent)

    convert(dest_file, pdf_file)

if __name__ == '__main__':
    merge_md() 
