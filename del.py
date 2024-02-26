import json
import os

from PIL import Image


def prepare_ch_json():
    data = {}
    for i in os.listdir("static/img/characters/"):
        if i.startswith("Character"):
            name = i.replace("Character_", "").replace("_Resize_Wish_500_500.webp", "")
            data[name.replace("_", " ")] = {
                "element": "hydro",
                "ru": "Е Лань",
                "href": os.path.join("./static/img/characters", i)
            }

    with open("data/characters.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    print("prepare_ch_json is done")


def resize():
    for i in os.listdir("static/img/characters/original"):
        if i.startswith("Character"):
            img = Image.open("static/img/characters/original/" + i)

            max_width, max_height = 500, 500
            width, height = img.size
            scale = min(max_width / width, max_height / height)
            new_size = (int(width * scale), int(height * scale))
            resized_img = img.resize(new_size)

            new_name = i.replace("_Full_Wish.webp", "_Resize_Wish_500_500.webp")
            resized_img.save("static/img/characters/" + new_name)

    print("resize is done")


def resize_main():
    img = Image.open("static/img/gi_index_original.webp")
    resized_img = img.resize((1920, 1080))
    resized_img.save("static/img/gi_index.webp")
    print("resize_main is done")


# resize_main()
# prepare_ch_json()
print("all done")
