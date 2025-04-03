from textnode import TextNode, TextType
import os
import sys
from shutil import rmtree, copy
from extract_markdown import generate_page, generate_pages_recursive

def main():
    basepath = sys.argv[0]
    copy_static_to_public()
    #generate_page("content/index.md", "./template.html", "./public/index.html")
    generate_pages_recursive("./content/", "./template.html", "./docs/", basepath)

def copy_static_to_public():
    if os.path.exists("./static/"):
        if os.path.exists("./public/"):
            rmtree("./public/")
        os.mkdir("./public/")
        copy_dirs("./static/", "./public/")

def copy_dirs(src_path, dst_path):
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    for entry in os.listdir(src_path):
        if os.path.isfile(src_path+entry):
            copy(src_path+entry, dst_path+entry)
        else:
            copy_dirs(src_path+entry+"/", dst_path+entry+"/")

main()
