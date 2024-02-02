import markdown

file_path = "C:\\Users\\114514\\Desktop\\print\\yourgitbook"
# your gitbook local address
# you may put this document under the file_path

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

with open(file_path + '\\.gitbook\\all_in_one.md', 'r', encoding='utf-8') as markdown_file:
    markdown_content = markdown_file.read()

    html_content = markdown.markdown(markdown_content)

    with open(file_path + '\\.gitbook\\all_in_one.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

