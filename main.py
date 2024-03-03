import pandas as pd
import pprint
import math
from load import build
import json
from datetime import datetime

empty_roll = [{
    'is_weapon': False,
    'name': 'Not exist data',
    'pity': "",
    'print_name': '(´•︵•`)',
    'time': datetime.now().strftime("%d.%m.%Y"),
}]
xlsx_path = "data/gi/paimonmoe_wish_history.xlsx"
with open("data/gi/ru.json", "r") as f:
    en_ru = json.load(f)


def main():
    win_condition = {"Character Event": [], "Weapon Event": [], "Standard": [], "Beginners' Wish": []}
    win_stat = {
        "Character Event": {
            "print_name": "События Персонажа",
            "type": "event",
        },
        "Weapon Event": {
            "print_name": "События Оружия",
            "type": "event",
        },
        "Standard": {
            "print_name": "Стандарт",
            "type": "standard",
        },
        "Beginners' Wish": {
            "print_name": "Баннер Новичка",
            "type": "standard",
        },
    }
    char_const = {}

    sheet_names = list(win_condition.keys())

    dfs = []
    for sheet_name in sheet_names:
        df = pd.read_excel(xlsx_path, sheet_name=sheet_name)

        five_star = df[df.iloc[:, 3] == 5]
        avg = five_star["Pity"].mean()
        win_stat[sheet_name].update({
            "count": df.shape[0],
            "avg": 0 if math.isnan(avg) else round(avg, 2),
            "before": (five_star["Pity"] < avg).sum(),
            "after": (five_star["Pity"] > avg).sum(),
            "legendary": five_star.shape[0],
        })
        dfs.append(df)

    for df in dfs:
        df['Time'] = pd.to_datetime(df['Time'], errors='coerce')

    for i, df in enumerate(dfs):
        df['Sheet'] = sheet_names[i]

    dfs_filtered = [df[df.iloc[:, 3] == 5] for df in dfs]

    merged_data = pd.concat(dfs_filtered, ignore_index=True)
    merged_data.sort_values(by='Time', inplace=True)

    for idx, row in merged_data.iterrows():
        rus_name = en_ru[row["Name"]]

        win_condition[row["Sheet"]].append({
            "name": f"{row['Name']} C{char_const[row['Name']]}" if row["Name"] in char_const else row["Name"],
            "print_name": f"{rus_name} C{char_const[row['Name']]}" if row["Name"] in char_const else rus_name,
            "pity": row["Pity"],
            "time": row["Time"].strftime("%d.%m.%Y"),
            "is_weapon": row["Type"] == "Weapon" and row["Sheet"] in ["Standard", "Beginners' Wish"]
        })
        char_const[row["Name"]] = min(char_const.get(row["Name"], 0) + 1, 6)

    for key, value in win_condition.items():
        value.reverse()
        win_stat[key]['pulls'] = empty_roll if len(value) == 0 else value

    return win_stat


if __name__ == "__main__":
    win_stat = main()
    pprint.pprint(win_stat)

    print("------------------------------------")

    build(win_stat)

    print("done")
