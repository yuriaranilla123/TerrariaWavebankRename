import os
import re

track_mapping = {
    # === ORIGINAL 1–61 ===
    "01": "Overworld Night", "02": "Eerie", "03": "Overworld Day", "04": "Boss 1",
    "05": "Title Screen", "06": "Jungle", "07": "Corruption", "08": "The Hallow",
    "09": "Underground Corruption", "10": "Underground Hallow", "11": "Boss 2",
    "12": "Underground", "13": "Boss 3", "14": "Snow Biome", "15": "Space Night",
    "16": "Crimson", "17": "Boss 4", "18": "Alternate Overworld Day", "19": "Rain",
    "20": "Ice Biome", "21": "Desert", "22": "Ocean Day", "23": "Dungeon",
    "24": "Plantera", "25": "Boss 5", "26": "Temple", "27": "Eclipse",
    "28": "Rain Ambient", "29": "Mushroom Biome", "30": "Pumpkin Moon",
    "31": "Alternate Underground", "32": "Frost Moon", "33": "Underground Crimson",
    "34": "The Towers", "35": "Pirate Invasion", "36": "Underworld [Hell]",
    "37": "Martian Madness", "38": "Moon Lord [Lunar Boss]", "39": "Goblin Invasion",
    "40": "Sandstorm", "41": "Old Ones Army", "42": "Space Day", "43": "Ocean Night",
    "44": "Windy Day", "45": "Wind Ambient", "46": "Town Day", "47": "Town Night",
    "48": "Slime Rain", "49": "Day Remix", "50": "Journey Beginning Intro [Menu Music]",
    "51": "Journey Beginning Title", "52": "Storm [Monsoon]", "53": "Graveyard",
    "54": "Underground Jungle", "55": "Jungle Night", "56": "Queen Slime",
    "57": "Empress of Light", "58": "Duke Fishron", "59": "Morning Rain",
    "60": "Alt Title Theme [Console Menu]", "61": "Underground Desert",

    # === OTHERWORLDLY (62–88) — Drunk world / Terraria Otherworld OST ===
    "62": "Prelude [Otherworldly Rain]",
    "63": "Every Adventure Has a Beginning [Otherworldly Day]",
    "64": "Night Falls, Darkness Emerge [Otherworldly Night]",
    "65": "Below the Surface [Otherworldly Underground]",
    "66": "Secret of the Sands [Otherworldly Desert]",
    "67": "Enchanted Blue [Otherworldly Ocean]",
    "68": "Celestial Caverns [Otherworldly Mushroom]",
    "69": "Ancient Citadel [Otherworldly Dungeon]",
    "70": "The Endless Void [Otherworldly Space]",
    "71": "Journey to the Core [Otherworldly Underworld]",
    "72": "Glimmers of Vibrance [Otherworldly Snow]",
    "73": "Shadows of Corruption [Otherworldly Corruption]",
    "74": "Decay and Corrosion [Otherworldly Underground Corruption]",
    "75": "Blood Crawlers [Otherworldly Crimson]",
    "76": "Crimson Chasm [Otherworldly Underground Crimson]",
    "77": "A Sweet Menace [Otherworldly Underground Ice]",
    "78": "Twisted Virtue [Otherworldly Underground Hallow]",
    "79": "Enter Darkness [Otherworldly Eerie]",
    "80": "Sinkholes of Darkness [Otherworldly Boss 2]",
    "81": "Behold the OctoEye [Otherworldly Boss 1]",
    "82": "Fighting off the Invasion [Otherworldly Invasion]",
    "83": "Fighting the Night [Otherworldly The Towers]",
    "84": "Consumed by Darkness [Otherworldly Lunar Boss]",
    "85": "Rage Of Tarunnk [Otherworldly Plantera]",
    "86": "Sky Guardian [Otherworldly Jungle]",
    "87": "Otherworldly Wall of Flesh",
    "88": "Postlude - Credits [Otherworldly Hallow]",

    # === POST-1.4.1 ADDITIONS ===
    "89": "Journey's End [Credits]",
    "90": "Deerclops",
    "91": "Aether [Shimmer]",

    # === 1.4.5 BOSS-SPECIFIC TRACKS ===
    "92": "The Destroyer",      "93": "King Slime",
    "94": "Lunatic Cultist",    "95": "Alternate Queen Bee",
    "96": "Queen Bee",          "97": "The Twins",
    "98": "Skeletron Prime",    "99": "Eater of Worlds",
    "100": "Alternate Torch God", "101": "Torch God",
    "102": "Rainbow Boulder Intro", "103": "Rainbow Boulder Loop",
    "104": "Skeletron",
}

for filename in os.listdir('.'):
    if not (filename.endswith('.wav') or filename.endswith('.mp3')):
        continue

    match = re.match(r'^(\d+)', filename)
    if not match:
        continue

    key = str(int(match.group(1))).zfill(2)
    correct_name = track_mapping.get(key)
    if not correct_name:
        print(f"No mapping found for: {filename}")
        continue

    ext = os.path.splitext(filename)[1]
    new_name = f"{key} - {correct_name}{ext}"

    if filename == new_name:
        continue

    try:
        os.rename(filename, new_name)
        print(f"Renamed: {filename} → {new_name}")
    except FileExistsError:
        os.remove(filename)
        print(f"Removed duplicate: {filename}")

print("Done.")