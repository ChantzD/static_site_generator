from textnode import TextNode, TextType
import os
import sys
import shutil
from extract_markdown import generate_page, generate_pages_recursive

def main():
    basepath = "/" 
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    copy_files_recursive("./static", "./docs")
    generate_pages_recursive("./content/", "./template.html", "./docs/", basepath)

# def copy_static_to_public():
#     if os.path.exists("./static/"):
#         if os.path.exists("./public/"):
#             shutil.rmtree("./public/")
#         os.mkdir("./public/")
#         copy_dirs("./static/", "./public/")
#
# def copy_dirs(src_path, dst_path):
#     if not os.path.exists(dst_path):
#         os.mkdir(dst_path)
#     for entry in os.listdir(src_path):
#         if os.path.isfile(src_path+entry):
#             shutil.copy(src_path+entry, dst_path+entry)
#         else:
#             copy_dirs(src_path+entry+"/", dst_path+entry+"/")

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

main()
