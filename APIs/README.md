# Understanding APIs ( Application Programming Interface )

An API is an Application Programming Interface

- Think of an API as a middle man that gives software the ability to communicate with another software.
- You have ACI and you have Python. In order to write code for ACI there is an API that exposes in order for you to communicate directly with ACI.
- API's use a URI

>NOTE: An API enforces that communication to return exactly what you expect.

REST - Representational State Transfer

- Is simple a way to use HTTP
- In order words it's a API that is build on HTTP.
- When you open your browser and type www.labeveryday.com you are sending a GET request to dns which is doing the same for the labeveryday server.
  
- This is how REST APIs work.
  - RESTful is how you design a rest API
  - HTTP Request - Headers and Payload
  - HTTP Response - Headers and Payload

## HTTP Response Codes

| Success (2xx)     | Description                                               |
| -------------     | :-------------:                                           |
| 200               | Request was successful                                    |
| 201               | The request has been fulfilled, new resource created      |
| 202               | Accepted for processing, but has not been completed.      |
| 204               | The server fulfilled request but does not return a body   |
| Server Error (5xx)| Description                                               |
| 500               | Internal Server Error                                     |
| 501               | Not Implemented                                           |
| Client Error (4xx)| Description                                               |
| 400               | Bad Request Malformed Syntax                              |
| 401               | Unauthorized                                              |
| 403               | Forbidden Server understood request, but refuses to fulfill it      |
| 404               | Resource not found given URI                              |

## CRUD

- Create (POST) - Creates a new resource
- Retrieve (GET) - Retrieve/Read a resource (safe)
- Update (PUT) - Update/Replace a resource
- Update (PATCH) - Update/Modify a resource (only changes)
- Delete (DELETE) - Removes a resource
