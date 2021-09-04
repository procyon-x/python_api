import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
redirect_url = response.history
final_url = response

for i in range(len(redirect_url)):
    print(redirect_url[i].url)
print(final_url.url)
