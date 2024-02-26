import os

from jinja2 import Environment, FileSystemLoader

# import model

TEMPLATE_PATH = "templates"
INDEX_NAME = "index.html"
BUILD_PATH = "build"
ELEMENTS = {
    "Анемо": "/static/img/element/Anemo.svg",
    "Гео": "/static/img/element/Geo.svg",
    "электро": "/static/img/element/Electro.svg",
    "Дэндро": "/static/img/element/Dendro.svg",
    "Гидро": "/static/img/element/Hydro.svg",
    "Пиро": "/static/img/element/Pyro.svg",
    "Крио": "/static/img/element/Cryo.svg"
}
SOCIAL = {
    "YouTube": {
        "src": "/static/img/social/youtube.svg",
        "href": "https://www.youtube.com/"
    },
    "Twitch": {
        "src": "/static/img/social/twitch.svg",
        "href": "https://www.twitch.tv/"
    },
    "VK": {
        "src": "/static/img/social/vk.svg",
        "href": "https://vk.com/"
    },
    "Spotify": {
        "src": "/static/img/social/spotify.svg",
        "href": "https://open.spotify.com/"
    },

    "Discord": {
        "src": "/static/img/social/discord.svg",
        "href": "https://discord.com/"
    },
    "Instagram": {
        "src": "/static/img/social/instagram.svg",
        "href": "https://instagram.com/"
    },
    "HoYoLAB": {
        "src": "/static/img/social/hoyolab.png",
        "href": "https://www.hoyolab.com/"
    },
    "X": {
        "src": "/static/img/social/twitter.svg",
        "href": "https://twitter.com/"
    },
}


def build(win_stat: dict):
    os.makedirs(BUILD_PATH, exist_ok=True)
    jinja = Environment(loader=FileSystemLoader(TEMPLATE_PATH))
    content = jinja.get_template(INDEX_NAME).render(win_stat=win_stat, elements=ELEMENTS, social=SOCIAL)

    with open(os.path.join(BUILD_PATH, INDEX_NAME), "w", encoding="utf-8") as f:
        f.write(content)
