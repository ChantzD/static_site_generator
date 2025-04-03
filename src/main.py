from textnode import TextNode, TextType
import os
from shutil import rmtree, copy

def main():
    copy_static_to_public()

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
