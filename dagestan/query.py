from urllib.request import urlopen
import json
import re

naib_id = 'fd1db04b-9c70-4b40-84a1-70091452f421'

vills = []
for i in range(1, 100):
    u = f'https://familio.org/api/v1/catalogs/dagestan1888/records?parent={naib_id}&page={i}'
    text = json.dumps(
        json.loads(urlopen(u).read()),
        ensure_ascii=False)
    vs = re.findall(r'"record_text": "(.*?)"', text)
    if not vs:
        break
    vills += vs

with open('list.txt', 'w', encoding="utf8") as f:
    f.write('\n'.join(vills[:-1]))
