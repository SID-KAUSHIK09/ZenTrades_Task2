import requests

url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
output_file = "assignment.json"

response = requests.get(url)
if response.status_code == 200:
    with open(output_file, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded JSON file successfully: {output_file}")
else:
    print(f"Failed to download JSON file. Status code: {response.status_code}")
