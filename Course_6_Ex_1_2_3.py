import re
import operator
import json
with open("text.txt", "r") as f:
    text = f.read()
    print(text)
cuvinte = re.split(r'[ ,.]', text)
print("lista de cuvinte:")
print(cuvinte)
aparitii = {x:cuvinte.count(x) for x in cuvinte}
print(aparitii)
y = list(aparitii.values())
z = list(aparitii.keys())
new_list = []
for single in y:
    frecventa =(single/len(cuvinte))*100
    new_list.append(frecventa)
print("1---dictionar aparitii")
print(aparitii)
y = new_list
di = dict(zip(z, y))
print("mai jos dictionar")
print(di)
# key_copy = di.values()  # Feel free to use any iterable collection
coffee_copy = {**di}
for k,v in coffee_copy.items():
    if di[k] < 1:
        del di[k]
print("2---dictionar sortat, valori este 1%")
print(di)
with open("json_6_1_1.json", "w", encoding="utf-8") as f:
    json.dump(di, f, ensure_ascii=False, indent=4)
with open("json_6_1_1.json", "r", encoding="utf-8") as f:
    my_data = json.load(f)
type(my_data)
print(my_data)
coffee_copy2 = {**di}
for k,v in coffee_copy2.items():
    if di[k] < 2.1:
        del di[k]
print("3---dictionar sortat 10 valori")
print(di)