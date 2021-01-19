#!/usr/bin/env python
# Parsing json lab
import requests
import json
from pprint import pprint

# disable certifications warnings so that you can do your API call
requests.packages.urllib3.disable_warnings()

# create json payload to login into api
encoded_body = json.dumps(
    {
        "aaaUser": {
            "attributes": {
                "name": "admin",
                "pwd": "ciscopsdt"
                }
            }
        }
    )

# Log into the APIC
resp = requests.post("https://sandboxapicdc.cisco.com/api/aaaLogin.json", data=encoded_body, verify=False)

# Create cookie to log into apic
header = {
    "Cookie": "APIC-cookie=" + resp.cookies["APIC-cookie"]
}

# Get health faults on APIC
tenants = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json?rsp-subtree-include=health,faults", headers=header, verify=False)

# Print results in text format
print(tenants.text)

# Create a json object
json_response = json.loads(tenants.text)

# Print a string json response
print(json.dumps(json_response, sort_keys=True, indent=4))

# Save the string json to a json file
with open('apic.json', 'w') as f:
    f.writelines(json.dumps(json_response, sort_keys=True, indent=4))

degraded = []

# Print each tenant name with dn and health
for tenant in json_response['imdata']:
    print('*' * 4 + f"Now printing tenant: {tenant['fvTenant']['attributes']['name']}" + ('*' * 4 ))
    print(f"dn: {tenant['fvTenant']['attributes']['dn']}")
    for health in tenant['fvTenant']['children']:        
        print(f"health: {health['healthInst']['attributes']['cur']}")
        if int(health['healthInst']['attributes']['cur']) < 100:
            degraded.append({tenant['fvTenant']['attributes']['name']: health['healthInst']['attributes']['cur']})
