import json # 注意这里不能命名为 json.py
from pathlib import Path

name = "name"
path = Path('name.json')
contents = json.dumps(name)
path.write_text(contents)