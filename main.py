import os
import requests

API_KEY = os.environ.get('NINJA_API')

API_URL = 'https://api.api-ninjas.com/v1/country?name=South Africa'
headers = {'X-Api-Key': API_KEY}

try:
    response = requests.get(API_URL, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == requests.codes:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

except Exception as e:
    print("An error occurred:", e)
