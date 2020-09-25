# python rest curd mysql 
---

### python rest crud
* $ pip install Flask
* $ pip install flask-restful
* $ pip install mysql-connector-python

### To run mongo docker 
* docker run -p 3306:3306 --name espark-mysql -e MYSQL_ROOT_PASSWORD=root mysql

### To get greetings
* $ curl localhost:5000/
### get all users
* $ curl localhost:5000/users
### get user by id
* $ curl localhost:5000/user/1
### create new users
* $ curl -X POST -H "Content-Type: application/json" -d '{"id":"4","name":"sonu singh"}' http://localhost:5000/user
### update users
* $ curl -X PUT -H "Content-Type: application/json" -d '{"name":"sonu singh thakur"}' http://localhost:5000/user/4
### delete users
* $ curl -X DELETE http://localhost:5000/user/4

### To kill the docker 
* docker ps -a
* docker stop <'container-id'>
* docker rm -f <'container-id'>