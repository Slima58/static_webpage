import os
import sys
import shutil
from copystatic import copy_files_recursive 
from create_content import generate_page, generate_pages_recursive

static_dir_path = "./static"
public_dir_path = "./public"
content_dir_path = "./content"
template_path = "./template.hml"
docs_dir_path = "./docs"

basepath =  "/" if len(sys.argv) < 2 else sys.argv[1]

def main():
    
    print("Deleting public directory ...")
    if os.path.exists(docs_dir_path):
        shutil.rmtree(docs_dir_path)

    print("Copying static files to public directory ...")
    copy_files_recursive(static_dir_path, docs_dir_path)

    generate_page(
        "./content/index.md",
        "./template.html",
        "./docs/index.html",
        basepath
    )
    generate_pages_recursive(
        content_dir_path,
        "./template.html",
        docs_dir_path,
        basepath
    )

main()


