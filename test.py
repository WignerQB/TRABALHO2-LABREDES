import json
f = open('conf.json', 'r')
data = json.load(f)
print(data)
f.close()
