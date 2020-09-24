# python docker 

---

### python rest crud
* $ pip install Flask
* $ pip install flask-restful

```
app
├─── requirements.txt
├─── Dockerfile
├─── .gitignore
└─── src
     └─── server.py
```

### server.py
```
from flask import Flask
server = Flask(__name__)

@server.route("/")
 def hello():
    return "Hello World!"

if __name__ == "__main__":
   server.run(host='0.0.0.0')
```


### requirements.txt
```
Flask==1.1.1
```

### .gitignore
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
```

### Dockerfile
```
# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./server.py" ]
```

### To Build Image 
* $ docker build -t adarshkumarsingh83/python-docker .

### to list the docker images 
* $ docker images
```
REPOSITORY                           TAG                                              IMAGE ID            CREATED             SIZE
adarshkumarsingh83/python-docker     latest                                           985285c812d3        19 seconds ago      891MB
```

### To execut the docker iamges 
* $ docker run -p 5000:5000 adarshkumarsingh83/python-docker
```
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [24/Sep/2020 15:33:32] "GET / HTTP/1.1" 200 -
```
### To view the docker process 
* $ docker ps -a 

## to stop the container 
* docker stop <'container-id'>
* docker rm -f <'container-id'>

## To remove the docker iamge 
* $ docker iamges 
* docker image rm -f <'image-id'>
