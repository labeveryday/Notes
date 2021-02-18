# Curl 


## Notes

### Examples

curl request to login to the DevNet sandbox ACI Apic

```bash
curl -d '{"aaaUser":{"attributes": {"name": "admin", "pwd": "ciscopsdt"}}}' -H "Content-Type: application/json" -X POST https://sandboxapicdc.cisco.com/api/aaaLogin.json
```


#### Resources