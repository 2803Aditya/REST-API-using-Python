![](Images/Flask_Python.jpg)

# Introduction
## About [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer)
- A RESTful API (also known as REST API) is an application programming interface (API or web API).
- It a way for two computer systems to communicate over HTTP in a similar way to web browsers and servers. 
- REST stands for representational state transfer.<br/><br/>
### A RESTful web service request contains:<br/>
**An Endpoint URL**: An application implementing a RESTful API will define one or more URL endpoints with a domain, port, path, and/or querystring.

**The HTTP method**: Differing HTTP methods can be used on any endpoint which map to application create, read, update, and delete (CRUD) operations:

- HTTP method	CRUD	Action
- GET	read	returns requested data
- POST	create	creates a new record
- PUT or PATCH	update	updates an existing record
- DELETE	delete	deletes an existing record

**Body Data**: Data is normally transmitted in the HTTP body in an identical way to HTML (form) submissions or by sending a single 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JSON-encoded data string.

### Flask Installation in Python 
> pip install flask
### Flask RESTful Installation in Python
> pip install flask-restful

## About [MongoDB Atlas](https://www.mongodb.com/cloud/atlas?jmp=partners_knowi)
- MongoDB Atlas is a cloud-based, open-source, NoSQL database that uses JSON documents with dynamic schemas, serving as an alternative to table databases.
- Atlas provides all the features of MongoDB, while automating database administration tasks such as database configuration, infrastructure provisioning, patches, scaling events, backups, and more, freeing up developers to focus on what matters to them most.
- MongoDB Atlas also provides the dual benefit of flexibility and scalability.

### Pricing
- #### Free Tier (In Use)
  - MongoDB offers a free tier that users can use for learning, prototyping, and early deployment. This free edition called M0 Sandbox is limited to 512MB of storage, shared vCPU  and RAM, 100 max connections, and a limit of one M0 cluster.

### Getting Started with MongoDB Atlas
- You can refer to this link for better understanding: https://www.knowi.com/blog/getting-started-with-mongodb-atlas-overview-and-tutorial/

## About [Docker](https://www.docker.com/)

- Docker is an open source project that makes it easy to create containers and container-based apps.
- It provides a small and lightweight execution environments that make shared use of the operating system kernel but otherwise run in isolation from one another.

### Components of Docker
#### Dockerfile
- Each Docker container starts with a Dockerfile. A Dockerfile is a text file written in an easy-to-understand syntax that includes the instructions to build a Docker image (more on that in a moment).
- A Dockerfile specifies the operating system that will underlie the container, along with the languages, environmental variables, file locations, network ports, and other components it needs—and, of course, what the container will actually be doing once we run it.

#### Docker Image
- Once you have your Dockerfile written, you invoke the Docker build utility to create an image based on that Dockerfile.
- A Docker image is a portable file containing the specifications for which software components the container will run and how.

#### Docker Container
- Docker’s run utility is the command that actually launches a container.
- Each container is an instance of an image.
- Containers are designed to be transient and temporary, but they can be stopped and restarted, which launches the container into the same state as when it was stopped.


# Get Started

## MongoDB Atlas Registeration
Firstly, register youself on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas?jmp=partners_knowi) and create a connection with your cluster.

After a successful creation of the connection we'll get a URI string, and with the help of that we gonna connect our cluster with the flask application.

URI string example:
> mongodb+srv://&lt;Username&gt;:'&lt;password&gt;'@&lt;ClusterName&gt;.csb3w.mongodb.net/&lt;DatabaseName&gt;?retryWrites=true&w=majority

Tutorial : https://www.knowi.com/blog/getting-started-with-mongodb-atlas-overview-and-tutorial/

## RESTful API using FLASK
- Install all the required libraries/dependencies using the pip command.
```
  pip install flask
  pip install flask_pymongo
  pip install urlib
  pip install dnspython
```
- After the successful installation of each dependencies, next step is importing dependenies in our python file.
```
  import flask, flask_pymongo, urllib, dnspython
```
**Flask**: Flask provides you with tools, libraries and technologies that'll allow us to build a web application.<br/>
**Flask PyMongo**: Flask-PyMongo bridges Flask and PyMongo and manages MongoDB connections for your Flask app.<br/>
**urllib**: In case when we've any escaped characters in out password field of URI string.<br/>
**dnspython**: Provides DNS toolkit for python.<br/>

- Now, Create a connection between our flask application and MongoDB using the connection string.
```
db_name = &lt;DatabadeName&gt;
db_URI = mongodb+srv://&lt;Username&gt;:&lt;Password&gt;@myfirstcluster.csb3w.mongodb.net/&lt;DatabaseName&gt;?retryWrites=true&w=majority
app.config['MONGODB_NAME'] = db_name
app.config['MONGO_URI'] = db_URI

mongo = PyMongo(app)
```

**app** is a central object of our flask application
**app.configuration** Configuration of Database
**PyMongo** will manage MongoDB connections for our flask application.

#### CRUD operation API endpoints
- Let's see what each of the HTTP methods for our API does:
  - **GET /api/Products**: It will return the details of all objects from our collection (with status code 200).
  - **POST /api/Products/add**: Create a new object in our collection and return 201 status code.
  - **PUT /api/Products/&ltid&gt**: Update fields of an object (with success code 201 and status code 404 for an failed operation).
  - **DELETE /api/Products/delete/&ltid&gt**: Delete an Object from collection with success code 204 and 404 for an failed operation.
  - **GET /api/Products/find/&ltid&gt**: It will return details of the specified object (with failed status code 404).
  
 **Read Operation**
 ```
 @app.route('/api/Products', methods = ['GET'])   # Allowed Method "GET"               
def get_data():

    data = mongo.db.Titanic    # Collection name is "Titanic"
    output = []

    for i in data.find():      # Query the database
        output.append({'Product Name' : i['name'], 'Offer Price' : i['offer_price_value']}) 

    return jsonify({'Result' : output}) # JSON serialization and this'll return a JSON response to our browser
 ```
 
- Check out remanining CRUD operation in the Flask_RestAPI.py file.

```
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)
```

- **app.run**: The flask run command provides options to set the server listening IP address and port, SSL certificates, etc.
- **host = 0.0.0.0**: It is used for External web servers.

## Deploy Docker Container
- Create a file named 'requirements.txt'. This ifle will contain list of dependencies to be installed for our flask application.
**Using pip command**
> pip3 freeze > requirements.txt

File content:
```
  Flask==1.1.2
  flask-mongoengine==1.0.0
  Flask-PyMongo==2.3.0
  Flask-RESTful==0.3.8
  ...
  ..
  .
```

- Create another file called Dockerfile. This file will contain all the commands that would help us build the docker image.

Code inside file:
```
  # Python as a base image for our container
  from python:3.8.0-buster

  # Make a directory for our application
  WORKDIR /app

  # Create copy of requirements.txt file in current work directory
  copy requirements.txt .

  # pip install all the required libraries/dependencies
  Run pip install -r requirements.txt

  # Create our source code
  copy . /app 

  # Run the application
  CMD [ "python", "Flask_RestAPI.py" ]
```

- The Dockerfile created above creates base image with python installed in it.
- Then, in the next step set /app as working directory for our application.
- Copy all the required dependenices in working directory. "." is represents the root directory.
- Then, run a pip command that will install all the dependencies mentioned in the requirements.txt file.
- Copy all source code in the current directory using dot.
- At last use cmd command, it will run our flask application.

**Build the Image using the following command**
> docker build -t &lt;ImageName&gt; . (don't forgot the dot)

**After successful building of image, run the image inside the docker container using the following command**
> docker run -p 5500:5500 &lt;ImageName&gt;

- "-p" option will bind port 5500 of container to port 5500 on localhost of the host machine.
- BAM!!, YOU ARE ALL SET.

## How to Access APIs on localhost?

- Open cmd and make sure docker is running by using "docker" command.<br/>
![](Images/docker1.PNG)

- Then, run "docker images" command and It will show all images present on docker.<br/>
![](Images/docker2.PNG)

- Next, run "docker ps -a" command and It will show all containers.<br/>
![](Images/docker3.PNG)

- Then, run the following command shown below and It will start our container.
> docker run -p &lt;host-port&gt;:&lt;docker-port&gt; &lt;ImageName&gt;
- "-p" option will bind the host port and container port<br/>
![](Images/docker4.PNG)
- So, container is up and running.
- Now, go to browser and open http://localhost: &lt;host-port&gt; / &lt;Endpoint&gt; and we are done.<br/>
![](Images/docker5.PNG)

## How to use these APIs?

To use or test these APIs we are using [POSTMAN](https://web.postman.co/home). <br/>
Postman is a Google Chrome app for interacting with HTTP APIs. It presents you with a friendly GUI for constructing requests and reading responses.<br/><br/>
**Note: I've already mentioned the API enpoints above in the "RESTful API using Flask" section**
