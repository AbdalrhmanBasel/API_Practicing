import requests

endpoint = "http://127.0.0.1:8001/api/"

# Make a request to a web page, and return the status code:
get_response = requests.get(endpoint, json={'query': "Data Sent"})  # HTTP Request
# print(get_response.text)

print(get_response.json())
print(get_response.status_code)
