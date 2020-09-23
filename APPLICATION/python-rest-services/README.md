
* $ pip install Flask

### Flask-RESTful for rest api
* $ pip install flask-restful


## to get wish msg 
* $ curl localhost:5000/


## Get call 
* $ curl localhost:5000/data/10

## post call 
* curl -X POST -H "Content-Type: application/json" -d '{"username":"abc","password":"abc"}' http://localhost:5000/data

## put call 
* curl http://localhost:5000/data/100  -H "Content-Type: application/json" -d '{"username":"abc","password":"abc"}' -X PUT

## delete call
* curl http://localhost:5000/data/100 -X DELETE 