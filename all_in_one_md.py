import markdown

file_path = "C:\\Users\\114514\\Desktop\\yourgitbook"
# your gitbook local address

all_path = []

all_path.append(file_path + "\\summary.md")

with open(file_path + "\\summary.md", 'r', encoding='utf-8') as file:
    content = file.read()
    for line in content.split('\n'):
        if "(" in line and ")" in line:
            start = line.index("(") + 1
            end = line.index(")")
            content = line[start:end]
            if content.endswith(".md"):
                all_path.append(file_path + "\\" + content)

all_in_one = ""

for i in all_path:
    with open(i, 'r', encoding='utf-8') as file:
        all_in_one += file.read()
        all_in_one += '\n\n\n'

with open(file_path + '\\.gitbook\\all_in_one.md', 'w', encoding='utf-8') as file:
    file.write(all_in_one)

css_style = """
<style>
body {
    font-family: 'Helvetica', 'Arial', sans-serif;
    margin: 20px;
}
h1, h2, h3, h4, h5, h6 {
    color: #333;
    border-bottom: 1px solid #eaecef;
    padding-bottom: 0.3em;
}
p, li {
    line-height: 1.6;
}
code {
    background-color: #f6f8fa;
    padding: 0.2em 0.4em;
    margin: 0;
    font-size: 85%;
    border-radius: 3px;
}
pre {
    background-color: #f6f8fa;
    border: 1px solid #eaecef;
    padding: 0.5em;
    overflow: auto;
    border-radius: 3px;
}
a {
    color: #0366d6;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
blockquote {
    padding: 0 1em;
    color: #6a737d;
    border-left: 0.25em solid #dfe2e5;
}
</style>
"""

with open(file_path + '\\.gitbook\\all_in_one.md', 'r', encoding='utf-8') as markdown_file:
    markdown_content = markdown_file.read()

    html_content = markdown.markdown(markdown_content)
    full_html_content = f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<title>Document</title>\n{css_style}\n</head>\n<body>\n{html_content}\n</body>\n</html>"

    with open(file_path + '\\.gitbook\\all_in_one.html', 'w', encoding='utf-8') as html_file:
        html_file.write(full_html_content)
