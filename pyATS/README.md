# pyATS Notes

# pyATS Notes

pyATS is a tool that allows an engineer to have an end-to-end testing ecosystem. 


pyATS is extensible by design. It enables developers to start with small, simple, linear test cases and easily scale towards large and complex tests.

To find labs on DevNet:

[Introduction to pyATS](https://developer.cisco.com/learning/lab/intro-to-pyats/step/1)

[Introduction to Genie](https://developer.cisco.com/learning/lab/intro-to-genie/step/1)

[Parsers with Genie](https://developer.cisco.com/learning/lab/parsers-with-genie/step/1)

[Genie System Profiling](https://developer.cisco.com/learning/lab/pts-with-genie/step/1)

## Features
- Write test cases that you can re-use, inherit, extend, and scale

### Intro to pyATS

[pyATS Documentation](https://developer.cisco.com/docs/pyats/api/)

[Reserve this sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/6b023525-4e7f-4755-81ae-05ac500d464a?diagramType=Topology)

You have several options to install pyATS

NOTE: Only supported versions of python are `v3.5.x`, `v3.6.x` and `v3.7.x`

1. `core framework only:` this installs just the core pyATS framework with zero optional extras.

All of these dependencies get installed

```python
pip list
Package              Version
-------------------- ---------
aiofiles             0.6.0
aiohttp              3.6.3
aiohttp-swagger      1.0.15
async-lru            1.0.2
async-timeout        3.0.1
attrs                20.3.0
certifi              2020.12.5
cffi                 1.14.5
chardet              3.0.4
cryptography         3.3.1
dill                 0.3.3
distro               1.5.0
idna                 2.10
Jinja2               2.11.2
junit-xml            1.9
MarkupSafe           1.1.1
multidict            4.7.6
pathspec             0.8.1
pip                  20.1.1
psutil               5.8.0
pyats                21.1
pyats.aereport       21.1
pyats.aetest         21.1
pyats.async          21.1
pyats.connections    21.1
pyats.datastructures 21.1
pyats.easypy         21.1
pyats.kleenex        21.1.1
pyats.log            21.1
pyats.reporter       21.1
pyats.results        21.1
pyats.tcl            21.1
pyats.topology       21.1
pyats.utils          21.1.2
pycparser            2.20
python-engineio      3.13.2
python-socketio      4.6.0
PyYAML               5.4.1
requests             2.25.1
setuptools           47.1.0
six                  1.15.0
typing-extensions    3.7.4.3
unicon               21.1
unicon.plugins       21.1
urllib3              1.26.3
yamllint             1.26.0
yarl                 1.5.1
```

2. `pyATS + pyATS Library/Genie:` this installs the core pyATS framework, and the standard pyATS network automation library, Genie.

NOTE: This is the recommended option

```

```



Before running a test suite, you must first define the devices that you are running your test against. 

- This is your yaml `testbed` file

> The lab uses virl and does not show how to install and setup pyATS

### Intro to Genie

Genie is the pyATS SDK that contains all the tools needed for Network Test Automation.

- Genie leverages Python

- Provides a method for network testers to interact with devicees through libraries and avoid functional programming. 

- Genie is used internall for Cisco

Python models respresent network features such as BGP, OSPF, VxLAN

[Available models](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models)

[Available parsers](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers)

Before running a test suite, you must first define the devices that you are running your test against.

Steps to install genie

1. Create virtual directory and activate it

```bash
# Create the virtual environment
python3 -m venv venv

# Activate the environment
source /venv/bin/activate
```

2. Install Genie packages

```bash
# Install genie
pip install genie
pip install genie.libs.robot
```

NOTE: You may have to install pyats[full] as well

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
