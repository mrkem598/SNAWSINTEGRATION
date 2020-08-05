#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://dev59361.service-now.com/api/now/table/u_code_from_aws?sysparm_limit=10'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'AWS_SN_USER1'
pwd = 'CDM_DHS_mo123'

# Set proper headers
headers = {"Name":"u_name","Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
