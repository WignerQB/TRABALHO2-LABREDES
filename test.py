import json
f = open('conf.json', 'r')
data = json.load(f)
print(data)
f.close()

while True:
    try:
        print("Digite CTRL+c")
    except KeyboardInterrupt:
        print("Pegou")
        a= input(" ")
        exit()
    else:
        print("Não pegou")
