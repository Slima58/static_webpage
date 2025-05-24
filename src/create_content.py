import shutil
from os import mkdir, listdir
from os.path import (
    exists,
    dirname,
    #split,
    #commonpath,
    isfile,
    join
)

from markdown_to_htmlnode import markdown_to_html_node

def extract_markdown_title(md):
    md_content = md.split("\n\n")
    for line in md_content:
        if not line.startswith("# "):
            continue
        elif line.startswith("# "):
            title = line.split(" ", maxsplit=1)[-1]
        else:
            raise Exception("This file does not have a title")
    
    return title

def read_file_contents(file):
    contents = open(file, "r")
    return contents.read()

def generate_page(from_path, template_path, dest_path):
    print(f"Generating path from\n{from_path} -> {dest_path} from {template_path}")
    """ LOADING FILES """
    origin_file = read_file_contents(from_path)
    temp_file = read_file_contents(template_path)

    """ EXTRACT TITLE AND CONTENT FROM FILES """
    origin_file_html_node = markdown_to_html_node(origin_file)
    origin_html = origin_file_html_node.to_html()

    content_title = extract_markdown_title(origin_file)

    """ LOADING TITLE AND CONTENT TO HTML PAGE """
    html_page = temp_file.replace("{{ Title }}", "{Title}") \
                .replace("{{ Content }}", "{Content}") \
                .format(Title = content_title, Content = origin_html )

    if not exists(dirname(dest_path)):
        directories = dirname(dest_path).split("/")[1:]
        dir_path = "."
        for dir in directories:
            dir_path += "/" + dir
            if exists(dir_path): 
                continue
            else:
                mkdir(dir_path)

    html_file = open(dest_path, 'w') 
    html_file.write(html_page)
                

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    content_files = listdir(dir_path_content)
    for file in content_files:
        file_path = join(dir_path_content, file)
        dest_path = join(dest_dir_path, file)
        if isfile(file_path):
            dest_path = dest_path.replace(".md", ".html")
            generate_page(file_path, template_path, dest_path)
        elif exists(dest_path):
            pass
        else:
            mkdir(dest_path)
            generate_pages_recursive(file_path, template_path, dest_path)




