import json
import os

from jinja2 import Environment, FileSystemLoader

TEMPLATE_PATH = "templates"
BUILD_PATH = "build"
DATA_PATH = "data"

INDEX_NAME = "index.html"
ELEMENTS_NAME = "elements.json"
SOCIAL_NAME = "social.json"
CHARACTERS = "characters.json"


def build(win_stat: dict):
    with open(os.path.join(DATA_PATH, ELEMENTS_NAME)) as f:
        elements = json.load(f)
    with open(os.path.join(DATA_PATH, SOCIAL_NAME)) as f:
        social = json.load(f)
    with open(os.path.join(DATA_PATH, CHARACTERS)) as f:
        characters = json.load(f)

    os.makedirs(BUILD_PATH, exist_ok=True)
    jinja = Environment(loader=FileSystemLoader(TEMPLATE_PATH))

    characters = sorted(characters.items(), key=lambda x: x[1]["element"])
    characters = {k: dict(sorted(v.items())) for k, v in characters}

    render_data = {
        "win_stat": win_stat,
        "elements": elements,
        "social": social,
        "characters": characters
    }
    content = jinja.get_template(INDEX_NAME).render(**render_data)

    with open(os.path.join(BUILD_PATH, INDEX_NAME), "w", encoding="utf-8") as f:
        f.write(content)
