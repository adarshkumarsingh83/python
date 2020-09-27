# python rest crud file 
---

### python rest crud
* $ pip install Flask
* $ pip install flask-restful

## To get greetings
* $ curl localhost:5000/
### get all users
* $ curl localhost:5000/users
### get user by id
* $ curl localhost:5000/user/1
### create new users
* $ curl -X POST -H "Content-Type: application/json" -d '{"id":4,"name":"sonu singh"}' http://localhost:5000/user
### update users
* $ curl -X PUT -H "Content-Type: application/json" -d '{"id":4,"name":"sonu singh thakur"}' http://localhost:5000/user/4
### delete users
* $ curl -X DELETE http://localhost:5000/user/4