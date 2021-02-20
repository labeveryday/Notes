# DevCor Notes

[DevCor Exam Topics and Labs](https://developer.cisco.com/certification/exam-topic-core/)

[DevNet Code Repo Here](https://github.com/CiscoDevNet/dne-dna-code)

Developing Applications using Cisco Core Platforms and APIs v1.0 (350-901)

## Exam topics and Labs

### 1.0 Software Development and Design

- [x] Setting up your Linux (Ubuntu) workstation as a development environment
- [x] Setting up your Windows workstation as a development environment
- [x] Setting up your macOS workstation as a development environment
- [x] What is a Development Environment and why do you need one?
- [x] A brief introduction to Git
- [x] Intro to Python Part 1  
- [x] Intro to Python Part 2
- [x] Coding 202: Parsing JSON using Python
- [x] Introduction to XML  
- [ ] Introduction to the Guest Shell
- [ ] Chat-Ops with Webex Teams and Python
- [ ] Firepower Management Center (FMC) REST API token-based authentication
- [ ] Exploring the 'webexteamssdk' Webex Teams Python Library
- [x] Git 100: Basics of the git version control system
- [ ] Git 101: Branching
- [ ] Git 102: Using git with servers
- [ ] Introduction to Webex Teams Apps
- [ ] Modern Application Development - This needs to be removed
- [x] Modern Application Development
- [ ] Understanding the OAuth Flow of a Webex Teams Integration
- [ ] Webex Teams Security and Access: Tokens, OAuth, Scopes, and Roles

### 2.0 Using APIs

- [x] What is REST? What are APIs
- [ ] Intro to Coding and APIs
- [ ] Getting started with REST APIs
- [ ] Hands On: Use Postman to interact with REST APIs
- [ ] Prime Infrastructure API 101: REST Basics
- [ ] Invoke Webex REST APIs from the interactive documentation
- [ ] Building Python Requests to Read and Create Webex Teams API Items
- [ ] Introduction to XML
- [ ] Introductory UCS Director REST API, Custom Tasks and Workflow Creation Part I
- [ ] Meraki Dashboard API Using Postman
- [ ] Meraki Location Scanning API Python
- [ ] Run a Webex Teams Bot Locally

### 3.0 Cisco Platforms

- [ ] Exploring Firepower Management Center (FMC) REST APIs
- [ ] Introduction to Meraki Integrations
- [ ] Introduction to Cisco DNA Center Northbound APIs
- [ ] Cisco DNA Center API Overview
- [ ] Cisco DNA Center Northbound API Modules
- [ ] What and Why of Model Driven Programmability
- [ ] Introducing YANG Data Modeling for the Network

### 4.0 Application Deployment and Security

- [ ] Introducing Containers
- [ ] Docker 101
- [ ] Microservices overview

### 5.0 Infrastructure and Automation

- [ ] Introduction to Meraki integrations
- [ ] Using the Meraki Dashboard API with postman
- [ ] Meraki location scanning API Python
- [ ] A hands-on introduction to the Cisco Container Platform v3.1
- [ ] Advanced Docker features
- [ ] Building an IOx Application with Docker
- [ ] Introduction to Ansible
- [ ] Managing Cisco Compute with Ansible
- [ ] Microservices overview

---

#### Notes

**Storing Application Secrets**

* Application secrets are:
    * Credentials used to access to third party systems
    * Credentials used to connect to databases
    * Credentials used for API calls

**Secrets can be used by the application based on the following:**

* Direct code storage or through `environment variables`
> NOTE: If you use this approach you should use environment variables through files. **NOT ON COMMAND LINE**
* Database storage - One secret to open the database and the rest of the secrets are stored in the database.
* API syncing services
* Encryption code storage - *Vaults* 
* Cloud-based secret services
* Cloud-based secret services accessed through an API gateway

**Examples for storing secrets**

```python
# Traditional Secret storing methods
# store secret in code directly
MY_SECRET = 'mypasswordkey'

# store secret in environment variable
MY_SECRET = os.environ["MY_KEY"]

# store secret in database
db = MySQLdb.connect("10.0.0.1", "username", "mypasswordkey", "MYDB")

# specific API code to connect to the syncing service
api = 'python code'
api.get_external_service()

# store secret in code encrypted file that requires a key file
MYSECRET = '19dNlanY&$2dvU'

```

**Applying End-to-End Encryption for APIs**

The reasons to protect and encrypt API traffic are:

* Business loss
* Compliance issues
* Reputation loss
* Raising in costs

North-south traffic protection is only perimetral security

* This is traffic in and out your network (VPN users)

East-west traffic protection is vital for security

* This is traffic that is moving within your organization (Data Center)

* To protect the east-west traffic, three approaches are available:
    * TLS or MTLS between services
    * Service mesh segmentation protocols (Proxy - Recommended) *istio, Linkrd* 
        * NOTE: when using a sevice mesh ICMP and UDP are not supported and you are not able to inspect the traffic.
    * Dedicated container firewall
* TLS East-West protection is similar to the north-south traffic protection

Options to protect north-south traffic:

* Using traditional TLS authentication and encryption or Mutual TLS (MTLS) authentication
* Using TLS or IPsec from the client to an API gateway or NGFW
* Using a cloud-based VPN service
* Using dedicated cloud connections

---

##### My Blogs

How to become a network engineer

https://www.labeveryday.com/post/how-to-become-a-network-engineer-in-2020

Do Network Engineers Need to Know Programming

https://www.labeveryday.com/post/do-network-engineers-need-to-know-programming

8 Python Resources for Network Engineers

https://www.labeveryday.com/post/8-python-resources-for-network-engineers

Six Skills You Need to Know to Become a Network Automation Engineer

https://www.labeveryday.com/post/six-skills-you-need-to-know-to-become-a-network-automation-engineer

How I Got Started with Network Automation

https://blogs.cisco.com/developer/start-in-network-automation

These 5 Learning Labs will Kick Start Your Network Automation Skills

https://blogs.cisco.com/developer/kick-start-network-automation-skills

##### Other blogs

How can DevNet Help You?
- https://blogs.cisco.com/partner/how-can-devnet-help-you?dtid=osscdc000283
- DevNet is our new developer program
- DevNet helps software developers build applications based on Cisco products- theseapps can help you enhance and manage Cisco networks or create entirely new solutionsfor your customers.

How DevOps Changed My (Work) Life

- https://blogs.cisco.com/developer/devops-work-life?dtid=osscdc000283

- https://blogs.cisco.com/cin/network-automation-for-devops?dtid=osscdc000283

- https://blogs.cisco.com/developer/devops-part-12?dtid=osscdc000283

- https://blogs.cisco.com/cloud/simplifying-the-devops-and-netops-journey-using-cisco-sd-wan-cloud-hub-with-google-cloud?dtid=osscdc000283

- https://blogs.cisco.com/developer/digital-transformation-journey?dtid=osscdc000283

- https://blogs.cisco.com/ciscoit/principles-of-agile-infrastructure?dtid=osscdc000283
