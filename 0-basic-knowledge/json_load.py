from pathlib import Path
import json

def get_name():
    path = Path('name.json')
    contents = path.read_text()
    text = json.loads(contents)

    print(f"##########{text}")

    if path.exists(): # use exists() to judge whether it exists
        return f"{text}" 
    else:
        return f"Do not exists"