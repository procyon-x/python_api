import requests
import time

rs = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
response = rs.json()
print(rs.text)
token = response["token"]
response_status = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})

status = response_status.json().get("status")
if status == "Job is NOT ready":
    print(status)
    seconds = rs.json().get("seconds")
    time.sleep(seconds)
response_status2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
status2 = response_status2.json().get("status")
if status2 == "Job is ready" and "result" in response_status2.text:
    print("result:", response_status2.json().get("result"), ";", "status:", response_status2.json().get("status"))
