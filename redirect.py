import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_response = response.history
second_response = response

new_url = first_response
for i in range(len(new_url)):
    print(new_url[i].url)
print(second_response.url)
