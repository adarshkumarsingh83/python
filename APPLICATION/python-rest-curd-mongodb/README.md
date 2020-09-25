# python rest curd mongodb 
---

### python rest crud
* $ pip install Flask
* $ pip install flask-restful
* $ pip install pymongo

### To run mongo docker 
* docker run -p 27017:27017 mongo

### To get greetings
* $ curl localhost:5000/
### get all users
* $ curl localhost:5000/users
### get user by id
* $ curl localhost:5000/user/1
### create new users
* $ curl -X POST -H "Content-Type: application/json" -d '{"_id":"4","data":{"name":"sonu singh"}}' http://localhost:5000/user
### update users
* $ curl -X PUT -H "Content-Type: application/json" -d '{"data":{"name":"sonu singh thakur"}}' http://localhost:5000/user/4
### delete users
* $ curl -X DELETE http://localhost:5000/user/4

### To kill the docker 
* docker ps -a
* docker stop <'container-id'>
* docker rm -f <'container-id'>
