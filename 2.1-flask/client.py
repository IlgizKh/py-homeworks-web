import requests

response = requests.post("http://127.0.0.1:8080/",
                         json={"name": "bike", "owner": "Ivan", "description": "new bike for sale"}
                         )
print(response.status_code)
print(response.text)

exit()
# response = requests.get("http://127.0.0.1:8080/adv/5/",
#                          )
# print(response.status_code)
# print(response.text)


# response = requests.delete("http://127.0.0.1:8080/adv/5",
#                          )
# print(response.status_code)
# print(response.text)



