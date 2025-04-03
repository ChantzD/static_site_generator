import re
import os
from block_markdown import markdown_to_html_node 

def extract_title(markdown):
    for line in markdown.split("\n"):
        if re.match(r"^# ", line):
            return line.strip("# ")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = open(from_path).read()
    template = open(template_path).read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    if not os.path.exists(("/").join(dest_path.split("/")[:-1])):
        os.makedirs(dest_path.split("/")[:-1])
    new_file = open(dest_path, 'a')
    new_file.write(template)
