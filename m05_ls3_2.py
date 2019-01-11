"""
скрипт який виведе список файлів та директорій поточній директорії
"""

from pathlib import Path, PurePath

p = Path(".")
p = list(p.glob('*'))

list_clin = []
for i in p:
    list_clin.append(str(PurePath(i)))
list_clin.sort()

with open('list.txt', 'w') as f:
    list_str = ''
    for x in list_clin:
        list_str = x + '\n'
        f.write(list_str)
