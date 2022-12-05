import requests

endpoint = "https://httpbin.org/anything"

# Make a request to a web page, and return the status code:
get_response = requests.get(endpoint, json={'query': "Data Sent"})  # HTTP Request
# print(get_response.text)

print(get_response.json())
print(get_response.status_code)
