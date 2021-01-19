# Notes on configuring Netmiko

When connecting to devices you can either import netmiko or ConnectHandler
I prefer to import from netmiko. 

Then you have to pass your device login arguments

```python
from netmiko import ConnectHandler


creds = {"username": "cisco",
         "password": "cisco",
         "ip": "1.1.1.1",
         "device_type": "cisco_ios"}

connect = ConnectHandler(**creds)
```

Now you are connected to your device. Now you can send commands.

```python
show_run = connect.send_command("show run", use_textfsm=True)

neighbors = connect.send_command("show cdp nei")
```
