from pathlib import Path
import json

def fuckzyt():
    path = Path('zyt.json')
    contents = path.read_text()
    zyt = json.loads(contents)

    print(f"i love you {zyt}")

    if path.exists(): # use exists() to judge whether it exists
        return("张语桐你的骚逼真臭")
    else:
        return(f"i want to fuck you everyday, {zyt}")