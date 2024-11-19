# REST API

💡 [Tap here](https://new.oprosso.net/p/4cb31ec3f47a4596bc758ea1861fb624) **to leave your feedback on the project**. It's anonymous and will help our team make your educational experience better. We recommend completing the survey immediately after the project.

## Contents

[[_TOC_]]


## Chapter I 

### Introduction

Hello! In this block you'll learn about RESTful API and how it's developed in the most popular languages. At the end, you'll get a practical task on how to design an API for your own store!

## Chapter II

### REST API
Let's start by deciphering the acronym. REST —  **RE**presentational **S**tate **T**ransfer. This technology allows you to retrieve and modify data and states of remote applications by passing HTTP requests over the Internet or any other network.

Simply put, a REST API is when a server application gives a client application access to its data through a specific URL.

The REST API allows you to use the HTTP protocol (the encrypted version is HTTPS) to communicate between programs, which is how we receive and send most information on the Internet.

When we type the URL http://website.com/something into the address bar, we are actually going to the website.com server and requesting a resource called /something. "Go there, get me that" is the HTTP request. Now suppose a program is running on website.com and another program wants to access it. In order for the program to understand what functions it needs, different addresses are used.

The foundation of the REST API is [HTTP Methods](https://www.rfc-editor.org/rfc/rfc2616). 
Standard HTTP methods:
- GET — clients use GET to access resources located on the server at the specified address;
- POST — used to send data to the server;
- PUT — used to completely create or update an existing resource;
- PATCH — used to update a portion of an existing resource;
- DELETE — used to delete a resource.

So, there are 5 functions that any program can use to get resource data. In fact, there are also functions like HEAD, OPTIONS, etc.

REST API is the most popular solution to organize interaction between different programs. It is used to connect mobile applications with server applications, to build microservice applications or to provide access to third-party programs.

It's important to note that each REST API request returns its results in numeric codes (called HTTP statuses). Remember when you had to return some code in training programs (e.g. 0 for success, 1 for error, etc.)? Here we have a similar idea.

![linux_network](./misc/images/http_responses.png)

Using the REST API you can exchange not only textual information, but also send data in special formats: XML, JSON, etc.

Yes, there are other API system architectures (JSON-PRC, XML-RPC, GraphQL). However, REST is still the most popular tool for building interaction between remote applications.

#### How does REST work??
The basic principle of the RESTful API is the same as the Internet. The client communicates with the server through the API when it needs a resource. Developers describe how the REST API is used by the client in the API documentation for the server application. The following are the basic steps of a REST API request:
- The client sends a request to the server. Guided by the API documentation, the client formats the request so that the server understands it.
- The server authenticates the client and confirms that the client has the right to make the request.
- The server receives the request and processes it internally.
- The server sends the response back to the client. The response contains information that tells the client whether the request was successful. The request also contains information requested by the client.
- REST API request and response information can vary slightly depending on how developers design the API.

### What is a RESTful system?
For a distributed system to be considered RESTful (designed according to [REST](https://restfulapi.net/)), it must meet a number of criteria.

- **Client-Server.** The system should be separated into client and server parts. This separation allows the clients to be "decoupled" from the specific way the server works, thus improving the mobility of the code.

- **Stateless.** The server does not need to know anything about client states. Requests need only contain enough information to be handled.

- **Cache.** Each response must be marked as cacheable or not. This prevents clients from reusing old data.

- **Uniform interface.** A uniform interface defines the interface (the set of available functions) between clients and servers. This simplifies the architecture and allows its parts to evolve independently.

- **Layered System.** It is allowed to divide the system into a hierarchy of layers, but with the condition that each component can only see the components of the next layer.

### Swagger & Open API 3.0
"Swagger" was the original name of the OpenAPI specification, but the specification was later changed to "OpenAPI" to emphasize the open nature of the standard.

The OpenAPI specification defines a standard that is a (RESTful) HTTP API that allows both humans and computers to discover and understand the capabilities of a service without access to source code or documentation.

The OpenAPI specification document is a Swagger file in YAML (or json) format created to describe the API.

In general, the document consists of the following parts:

- openapi

   The openapi object specifies the version of the specification (for example, in our case it is 3.0.0). Example:
    ```yaml
    openapi: "3.0.2"
    ```
    By the way, you can write your document in the official [online editor.](https://swagger.io/tools/swagger-editor/)

- info

    This object contains basic information about the API (e.g. header, version, license link, etc.) Let's look at the example:
    ```yaml
    openapi: "3.0.2"
    info:
      title: "The best API"
      description: "This is the most RESTful API in your life!"
      version: "1.2"
      termsOfService: "link"
      contact:
          name: "The best API contact"
          url: "link"
          email: "mail@mail"
      license:
          name: "Licence name"
          url: "link"
    ```

- servers

    This object allows you to specify the base path used in API requests. The base path is the part of the URL that comes before the endpoint. Endpoints will be considered in the path object. Let's look at the example of servers.

    ```yaml
    servers:
      - url: http://localhost:5000/
        description: main server
    ```

- paths

    The path object contains information about endpoints. Each element in path object contains operations object (GET, POST, PUT, DELETE methods). The structure of a single connection endpoint looks like this.

    ```yaml
    paths:
      /weather:
        get:
          tags:
          summary:
          description:
          operationId:
          externalDocs:
          parameters:
          responses:
          deprecated:
          security:
          servers:
          requestBody:
          callbacks:
    ```
    Not all fields are mandatory. For example, if a request has no request body parameters, it is not necessary to include the requestBody object.

    Request parameters contain an array of parameters with their objects. 

    ```yaml
    parameters:
    - name: 
      in: 
      description:
      required:
      example:
      allowEmptyValue:
      ...
    - name:
      in:
      description:
      ...
    ```
    
    See also the example of the responses object.

    ```yaml
    responses:
        200:
          description: Successful response
          content:
            application/json:
              schema:
                title: Sample
                type: object
                properties:
                  placeholder:
                    type: string
                    description: Placeholder description

        404:
          description: Not found response
          content:
            text/plain:
              schema:
                title: Not found
                type: string
                example: Not found
    ```

- components

    This object contains reused definitions that can appear in several places in the specification document.

- security

    The security object specifies the security or authorization protocol used to send requests.

Besides, there are tags and externalDocs objects.

#### **Swagger UI**

Swagger UI provides a framework that reads the OpenAPI specification and creates a web page with interactive documentation where requests can be sent in real time.

The official [swagger specification](https://swagger.io/specification/).

It is important to note that there are two approaches to writing documentation. The first approach is to write documentation almost automatically on the basis of the code. The second is to write it separately from the code.

**In the task you will write comments in the code, which will be the basis for the OpenAPI specification, i.e. use the 1 approach.**

![Swagger example](./misc/images/swagger.png)

### Implementation of the HTTP API in modern programming languages
You can look at examples based on which you can implement HTTP API in the materials.

### About Postgres
You will need a DBMS (database management system) to implement your project. We recommend that you use Postgres. What is Postgres?

PostgreSQL is an open source object-relational database management system. Because it is an open source project, it is constantly being improved and supports many extensions. New versions of the database are released on a regular basis. Both UNIX-like systems and Windows systems are supported.

You can download PostgreSQL from the [official website](https://www.postgresql.org/download/). If you download the desktop version, you will also get PgAdmin, a client for working with postgres.

It is also possible to run postgres in a docker container and access it from localhost after configuring the ports.

How do you use postgres in your applications? You need to specify a connection string and, depending on the language, use libraries to work with the database:
- Python — peewee, psycopg2;
- C# — EntityFramework;
- Go — pq;
- Java — pgJDBC.

## Chapter III
Well, well, it's time to do things on your own.

### StoreAPI
So you've decided to open your own store. You don't have money to buy a website, so you decide to write everything yourself. A properly written backend will allow you to make a website, desktop, and even mobile applications later. And they will all get their data from our REST API. Don't forget about foreign keys. Learn the difference between DAL (Data Access Layer) and DTL (Data Transfer Layer) objects.

**Store type**: appliance store.

** Pay attention! ** We implement relational model in the database! Study the models carefully and design the database model according to normal forms. You will have to learn about normal forms by yourself!

The entities are:
```
// Client
{
    id
    client_name
    client_surname
    birthday
    gender
    registration_date
    address_id
}
```
```
// Product
{
    id
    name
    category
    price
    available_stock // the number of products purchased
    last_update_date // date of last purchase
    supplier_id
    image_id: UUID
}
```
```
// Suppliers
{
    id
    name
    address_id
    phone_number
}
```
```
// Images
{
    id : UUID
    image: bytea
}
```

```
// Addresses
{
    id
    country
    city
    street
}

```
It is possible to add additional entities.

The entities described above must be implemented in the PostgreSQL relational database. According to the resulting tables, you must use DAO (Data Access Objects) objects in the project to retrieve data in the repositories. 

**Important**: You need to pick the optimal type in the DBMS to store the data (For each column field)! 

**Tip**: For unique identifiers use UUID/GUID type.

You need to implement popular types of HTTP requests (GET, POST, PUT, DELETE, PATCH).

- For clients:
    
    1. Add a client (json is input, corresponding to the structure described above).

    2. Delete a client (by its identifier).

    3. Get clients by first and last name (parameters — first and last name).

    4. Get all clients (In this request it is necessary to provide optional pagination parameters in the request line: limit and offset.). If these parameters are missing, return the whole list.

    5. Change the client's address (parameters: Id and new address as json according to the format described above).

- For products:

    1. Add a product (json is input, corresponding to the structure described above).

    2. Decrease the quantity of the product (the id of the product and how much to decrease is given as an input).

    3. Get the product by id.

    4. Getting all the available products.

    5. Deleting a product by id.

- For suppliers:

    1. Add a supplier (json is input, corresponding to the structure described above).

    2. Change the supplier's address (parameters: Id and new address as json according to the format described above).

    3. Delete a supplier by id.

    4. Get all suppliers.

    5. Get a supplier by id.

- For images:

    1. Add an image (The byte array of the image and the product id is input).

    2. Change the image (the image id and a new line to replace is input).

    3. Delete an image by image id.
 
    4. Get an image of a specific product (by product id).
   
    5. Get an image by image id.

The methods that return an image must return an image (array of bytes) with the "application/octet-stream" header. The file must be loaded automatically.

For each of the requests described above, if the data in the body is provided to the input, it is necessary to validate the data and if validation was unsuccessful — give 400 error code with the message.

If the request includes data update or receipt by Id, it is necessary to return error code 404 with the message in case of missing data.

If the request involves returning a list of data, an empty list is returned if there is no data.

Mandatory requirements: 
- Full coverage of methods with OpenAPI specification, presence of swagger comments and example objects. The Swagger specification should be given at: 
  >http://localhost:{YourPort}/swagger/index.html
- You have to use DTOs (Data Transfer Objects) to communicate with the API. To convert one model to another, use mappers. The path to the controller methods must start with the prefix: 
  >/api/v1/...
- The API must necessarily be designed according to [RESTFUL](https://restfulapi.net/) methodology.
- Use the database to store data, implementing the **Repository** pattern as the data access layer.
