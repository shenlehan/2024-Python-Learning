from pathlib import Path

path = Path('text.txt')
contents = path.read_text().split()
for i in contents:
    print(i)

path.write_text('Hello World')