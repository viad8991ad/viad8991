import json
import os

from jinja2 import Environment, FileSystemLoader

TEMPLATE_PATH = "templates"
BUILD_PATH = "build/gi"
DATA_PATH = "data/gi"

INDEX_NAME = "index.html"
GI_TEMPLATE = "gi.html"
ELEMENTS_NAME = "elements.json"
SOCIAL_NAME = "social.json"
CHARACTERS = "characters.json"
CHARACTERS_PATH_DIR = "../static/img/characters/"


def build(win_stat: dict):
    os.makedirs(BUILD_PATH, exist_ok=True)

    jinja = Environment(loader=FileSystemLoader(TEMPLATE_PATH))

    with open(os.path.join(DATA_PATH, ELEMENTS_NAME)) as f:
        elements = json.load(f)
    with open(os.path.join(DATA_PATH, SOCIAL_NAME)) as f:
        social = json.load(f)
    with open(os.path.join(DATA_PATH, CHARACTERS)) as f:
        characters = json.load(f)

    result = {}
    for key, value in elements.items():
        value["characters"] = []
        result[key] = value

    characters = dict(sorted(characters.items(), key=lambda x: x[1]["ru"]))

    for key, values in characters.items():
        values["href"] = CHARACTERS_PATH_DIR + values["href"]
        result[values["element"]]["characters"].append({key: values})

    render_data = {
        "win_stat": win_stat,
        "social": social,
        "data": result
    }
    content = jinja.get_template(GI_TEMPLATE).render(**render_data)

    with open(os.path.join(BUILD_PATH, INDEX_NAME), "w", encoding="utf-8") as f:
        f.write(content)
