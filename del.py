import json
import os
import pprint


# from PIL import Image


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


# def resize():
#     for i in os.listdir("static/img/characters/original"):
#         if i.startswith("Character"):
#             img = Image.open("static/img/characters/original/" + i)
#
#             max_width, max_height = 500, 500
#             width, height = img.size
#             scale = min(max_width / width, max_height / height)
#             new_size = (int(width * scale), int(height * scale))
#             resized_img = img.resize(new_size)
#
#             new_name = i.replace("_Full_Wish.webp", "_Resize_Wish_500_500.webp")
#             resized_img.save("static/img/characters/" + new_name)
#
#     print("resize is done")


# def resize_main():
#     img = Image.open("static/img/gi_index_original.webp")
#     resized_img = img.resize((1920, 1080))
#     resized_img.save("static/img/gi_index.webp")
#     print("resize_main is done")

def foo():
    with open("data/characters_data.json", "r") as f:
        characters_data = json.load(f)

    result = {}
    for en_name, ru_name in characters_data.items():
        result[en_name] = {
            "ru": ru_name,
            "element": ""
        }

    with open("data/characters_data.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False)


with open("data/elements.json") as f:
    elements = json.load(f)
with open("data/characters.json") as f:
    characters = json.load(f)
with open("data/characters_data.json") as f:
    characters_data = json.load(f)

for key, values in characters_data.items():
    characters[key]["element"] = values["element"]

with open("data/characters.json", "w", encoding="utf-8") as f:
    json.dump(characters, f, ensure_ascii=False)

# print(characters)
pprint.pprint(characters)
# characters = dict(sorted(characters.items(), key=lambda x: x[1]["ru"]))
# print(type(characters))

# resize_main()
# prepare_ch_json()
print("all done")
