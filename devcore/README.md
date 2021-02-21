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

## Storing Application Secrets

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
---

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
        * NOTE: when using a setvice mesh ICMP and UDP are not supported and you are not able to inspect the traffic.
    * Dedicated container firewall
* TLS East-West protection is similar to the north-south traffic protection

Options to protect north-south traffic:

* Using traditional TLS authentication and encryption or Mutual TLS (MTLS) authentication
* Using TLS or IPsec from the client to an API gateway or NGFW
* Using a cloud-based VPN service
* Using dedicated cloud connections

---

## Securing Web and Mobile Applications

**Open Web Application Security Project (OWASP)**

- global and nonprofit cybersecurity foundation
- they provide free and open application security tools and standards
- they provide content on secure development, testing and code review
- they create and maintain the ten most critical web application security risks in a document called [OWASP Top Ten](https://owasp.org/www-project-top-ten/)

How to mitigate `A1:2017-Injection` SQL injection attacks?

- Deny anything that are not of the correct type

An example of a simple SELECT SQL query:

```python
login_query = 'SELECT * FROM USERS WHERE USER = ’ + user_name
```

If the user gives the input as `user_name = "' OR 1=1"`, the query returns all users in the database because 1=1 always evaluates as true—rendering the query effectively as `SELECT * FROM USERS`.

How to mitigate `A2:2017-Broken Authentication`

- 

How to mitigate `A3:2017-Sensitive Data Exposure`

- encrypt your data at rest

How to mitigate `A4:2017-XML External Entities`

- Check and verify where your data is written from

How to mitigate `A5:2017-Broken Access Control`

- Deny all request that have not been authenticated

How to mitigate `A7:2017-Cross-Site Scripting (XSS)`

- Always check where the data is coming from
- Use the logout button to keep attackers from taking advantage of your browser

**Injection Attacks and Data Validation**

- They allow attackers to relay malicious code through an application to another system.
- They are listed as the number one web application security rick in the OWASP Top 10
- They are among the oldest and most dangerous attacks that are aimed at web applications
- They lead to data loss, data theft, DOS and system compromise

Common injection attack types:

- SQL injection
- XSS injection
- LDAP injection
- Code injection
- CRLF injection
- Email header injection
- Host header injection
- Operating system command injection
- XPath injection

`Cerberus` in python is a very flexible validator, allowing the developer to specify their schema in several formats

**Example**

```python
import yaml
from cerberus import Validator
 schema_text = """
sku:
  type: integer
  required: True
  min: 1000
  max: 0xffff
description:
  type: string
  required: True
  maxlength: 30
"""
 schema = yaml.load(schema_text)
 v = Validator()


 # Invalid SKU, No Description
document = {'sku': 138}
v.validate(document, schema)
> False
v.errors
> {'sku': ['min value is 1000'], 'description': ['required field']}
 # Valid SKU, Description is too long
document = {'sku': 0xeff, 'description': 'This is a really long product description, far too long and will fail'}
v.validate(document, schema)
> False
v.errors
> {'description': ['max length is 30']}
 # A valid document
document = {'sku': 0xbeef, 'description': 'Demo product description'}
v.validate(document, schema)
> True

```

**XSS and Request Forgery**

XSS

- Occurs when an attacker injects malicious content into trusted content that is then fed to the victim. Typically, this kind of attack is persistent.

Mitigate with HTML core library

```python
html.escape(string quote=True)
html.unescape(string)
```

CSFR

- An attack on state changes. These attacks rely on tricking users into performing some sort of stateful action, like changing an email address or password. 

Mitigating use a CSRF token

Python applications that support CSRF tokens:

- Flask-WTF
- Flask-SeaSurf
- Django
- Pyramid
- Sanic-WTF

**OAuth Authorization Framework**

- OAuth is an open standard for access delegation.
- Released in 2007
- OAuth 1.0 was standardized in RFC5849 in 2010
- OAuth 2.0 was standardized in RFC6749 in 2012 and is the current standard
- Allows an end user to authorize an application to gain access to a third party service without sharing their credentials with the application
- Example using you social media to log into labeveryday.com or some other website

How does it work? 

1. Resource Owner (The Client) - tells client application that they wish to perform an OAuth action
2. Client application responds to the resource owner with a redirect to the OAuth authorization server; embedded in the redirect is the client ID
3. The user follows the redirect and communicates directly with the OAuth provider
4. The OAuth provider validates that the client ID is valid
5. The authorization server will redirect the user to the redirect URI


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
