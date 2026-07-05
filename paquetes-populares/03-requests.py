import requests

# url = "https://jsonplaceholder.typicode.com/users"

# r = requests.get(url, timeout=10)
# r = r.json()

# for user in r:
#   print(user["name"])

# url = "https://jsonplaceholder.typicode.com/users/1"

# r = requests.get(url, timeout=10)
# print(r.json())

url = "https://jsonplaceholder.typicode.com/users/2"
apikey = "123456"
headers = {
  "Autorization": f"Bearer {apikey}"
}
r = requests.delete(url, timeout=10)
print(r.status_code)