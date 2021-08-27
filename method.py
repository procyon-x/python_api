import requests

'''1. Делает http-запрос любого типа без параметра method.
2. Делает http-запрос не из списка. Например, HEAD. Без параметра method.'''

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
any_met = [requests.get(url), requests.post(url), requests.put(url), requests.delete(url), requests.head(url)]
for i in range(len(any_met)):
    print(any_met[i], any_met[i].text)


'''2. Делает http-запрос не из списка. Например, HEAD. Добавила параметр method.'''

rs = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})
print(rs, rs.text)


'''3. Делает запрос с правильным значением method. Для примера взяла DELETE.'''

rs1 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "DELETE"})
print(rs1, rs1.text)


'''4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.'''

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

met = [
    {"method": "GET"},
    {"method": "POST"},
    {"method": "PUT"},
    {"method": "DELETE"},
]

for rsp in met:
    print("GET " + requests.get(url, params=rsp).text)

for rsp in met:
    print("POST " + requests.post(url, data=rsp).text)

for rsp in met:
    print("PUT " + requests.put(url, data=rsp).text)

for rsp in met:
    print("DELETE " + requests.delete(url, data=rsp).text)
