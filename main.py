import json
import os

entries = []

files = os.listdir(".")
for file in files:
    if not os.path.isdir(file):
        if file.split(".")[1] == "md":
            f = open(file)
            text = f.read()
            date = f.name.split(".")[0] + "T04:00:00Z"
            entries.append({
                "isAllDay": True,
                "text": text,
                "creationDate": date,
                "timeZone": "Asia\/Shanghai",
                "isPinned": False,
                "duration": 0,
                "starred": False
            })
day_one = {"metadata": {"version": "1.0"}, "entries": entries}

with open("./DayOne.json", 'w') as write_f:
    json.dump(day_one, write_f, indent=4, ensure_ascii=False)
