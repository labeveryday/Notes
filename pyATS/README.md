# pyATS Notes

https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/manageconnections.html

After installing the requirements file

Run this command to setup your test bed  and then go through the setup
genie create testbed interactive --output yaml/testbed.yml --encode-password

An example of genie
From the yaml directory. Create a file called testbed.yaml

```yaml
---
testbed:
  name: testbed
  credentials:
    default:
      password: ''
      username: duan

devices:
  SW6:
    os: ios
    type: ios
    connections:
      mgmt:
        ip: x.x.x.x
        protocol: ssh
```

Create a python file

```python
from genie.testbed import load

tb = load('yaml/testbed.yml')

dev = tb.devices['SW6']

dev.connect()

p1 = dev.parse('show run')
print(p1)
```