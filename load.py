import os

from jinja2 import Environment, FileSystemLoader

# import model

TEMPLATE_PATH = "templates"
INDEX_NAME = "index.html"
BUILD_PATH = "build"


def build(win_stat: dict):
    os.makedirs(BUILD_PATH, exist_ok=True)
    jinja = Environment(loader=FileSystemLoader(TEMPLATE_PATH))
    content = jinja.get_template(INDEX_NAME).render(win_stat=win_stat)

    with open(os.path.join(BUILD_PATH, INDEX_NAME), "w", encoding="utf-8") as f:
        f.write(content)
