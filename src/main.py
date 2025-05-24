import os
import shutil
from copystatic import copy_files_recursive 
from create_content import generate_page, generate_pages_recursive

static_dir_path = "./static"
public_dir_path = "./public"
content_dir_path = "./content"

def main():
    print("Deleting public directory ...")
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)

    print("Copying static files to public directory ...")
    copy_files_recursive(static_dir_path, public_dir_path)

    #generate_page("./content/index.md", "./template.html", "./public/index.html")
    #generate_page("./content/test.md", "./template.html", "./public/testd1/testd2/index_test.html")
    generate_pages_recursive(content_dir_path, "./template.html", public_dir_path)

main()


