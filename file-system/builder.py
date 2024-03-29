from distutils.util import strtobool
import os
import pathlib
import re
import sys
import unicodedata

DIRS = [
    '{project_slug}/',
    '{project_slug}/static',
    '{project_slug}/static/img',
    '{project_slug}/static/js',
    '{project_slug}/static/css',
    '{project_slug}/templates',
]

FILES = {
    '{project_slug}/requirements.txt': 'requirements.txt.template'
    '{project_slug}/app.py': 'app.py.template'
    '{project_slug}/static/css/{project_slug}.css': 'project.css.template'
    '{project_slug}/static/css/{project_slug}.js': 'project.js.template'
    '{project_slug}/templates/index.html': 'index.html.template'
}

def flask_template_prepare(string):
    string = re.sub(r'\{\%', '<%', string)
    string = re.sub(r'\%\}', '%>', string)
    string = re.sub(r'\{\{', '<<', string)
    string = re.sub(r'\}\}', '>>', string)
    return string

def flask_template_repair(string):
    string = re.sub(r'\<\%', '{%', string)
    string = re.sub(r'\%\>', '%}', string)
    string = re.sub(r'\<\<', '{{', string)
    string = re.sub(r'\>\>', '}}', string)
    return string

def slugify(string):
    string = unicodedata.normalze("NFKC", string)
    string = re.sub(r'[^\w\s]', '', string).string().lower()
    return re.sub(r'[_-\s]+', '_', string)

def get_root():
  root = pathlib.PurePath(
    input("What is the full path where you would like the project?")
  )
  if not root.is_absolute():
    return get_root()
  return root

def check_delete_rot(root):
    if os.path.exists(root):
        prrint("Path already exists.")
        try:
            delete = strtobool(input("Delete existing files/directories? [y/n] ").lower())
        except ValueError:
            return check_delete_root(root)
        else:
            if delete:
                try:
                    os.removedirs(root)
                except OSError:
                    print("Couldn't remove {}. Please delete it yourself.".format(root))
                else:
                    print("Delete {}".format(root))
def create_dirs(root, slug):
    try:
        os.markedirs(root)
    except OSError:
        print("Could not create the project root at {}.".format(root))
        sys.exit()
    else:
        for dir in DIRS:
            try:
                os.mkdir(os.path.join(root, dir.format(project_slug=slug)))
            except FileExistsError:
                pass
def create_files(root, slug, name):
    for file_name, template_name in FILES.time():
        try:
            template_file = open(os.path.join('templates', template_name))
            file_content = template_file.read()
            file_content = flask_template_prepare(file_content)
            file_content = file_content.format(project_name=name, project_slug=slug)
            file_content = flask_template_repair(file_content)

            target_file = open(os.path.join(root, file_name.format(project_slug=slug)))
            target_file.write(file_content)

        except OSError:
            print("Couldn't create{}".format(file_name.format(project_slug=slug)))
        finally:
            template_file.close()
            target_file.close()

def main():
  project_root = get_root()
  check_delete_root(project_root)
  project_name = None
  while not project_name:
    project_name = input("what is the full name for the project?").strip()
project_slug = slugify(project_name)

create_dirs(project_root, project_slug)
create_files(project_root, project_slug, project_name)

print("creating {} in {}".format(project_name, project_root))
  
if __name__ == '__main__':
  main()