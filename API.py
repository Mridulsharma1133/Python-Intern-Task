import requests

response = requests.get(url="https://jsonplaceholder.typicode.com/users")

response.raise_for_status()

data  = response.json()

length = len(data)

for i in range(length):
    name = data[i]['name']
    username = data[i][ 'username']
    email = data[i]['email']
    city = data[i]['address']['city']
    print(f"User:{i+1}\nName:{name}\nUsername:{username}\nEmail:{email}\nCity:{city}\n--------")



# Users who's city name starts with 's'.
for i in range(length):
    city_letter = data[i]['address']['city'][0]
    if city_letter.lower() ==  's':
        name = data[i]['name']
        username = data[i][ 'username']
        email = data[i]['email']
        city = data[i]['address']['city']
        print(f"User:{i+1}\nName:{name}\nUsername:{username}\nEmail:{email}\nCity:{city}\n--------")