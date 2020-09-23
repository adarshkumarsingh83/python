# python rest services 

---

## Two approach for rest api development using 
* S/W installation for web base pyhton 

---
## website url
* https://flask.palletsprojects.com/en/1.1.x/

### Flask for basic rest api 
* $ pip install Flask

## Exmaple 

* WishService.py 
```
from flast import Flast, jsonify
app = Flask(__name__)

@app.route('/'')
def wish():
	return jsonify({'messagge':'welcome to espark'})

if __name__ = '__main__':
	app.run(debug=True)
```
### To Run app 
* python WishService.py 


## Exmaple 

* WishService.py 
```
from flast import Flast, jsonify, request

app = Flask(__name__)

@app.route('/data',method = ['POST', 'GET'])
def wish():
     if (request.method == 'POST'):
        requestPayload = request.get_json()
	    return jsonify({'requestPayload': requestPayload }) , 201
	 else:
	 	return jsonify({'messagge':'welcome to espark'})


@app.route('/data/<int:id>', method=['GET'])
def getData(id):
	return jsonify({'messageId':'welcome to espark for id '+id }) 

if __name__ = '__main__':
	app.run(debug=True)
```
### To Run app 
* python WishService.py 


---
## website url 
* https://flask-restful.readthedocs.io/en/latest/

### Flast-RESTful for rest api 
* $ pip install flask-restful

```
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class GreetWorld(Resource):
    def get(self):
        return {'messagge':'welcome to espark'}

    def post(self):
    	requestPayload = request.get_json()
    	return {'requestPayload': requestPayload } , 201 

class DataService(Resource):
	def get(self, id):
		return {'messageId':'welcome to espark for id '%id }

	def put(self, name):
	 	return {'messageId':'welcome to espark for name '%name }


api.add_resource(GreetWorld, '/')
api.add_resource(DataService, '/data/<int:id>')
api.add_resource(DataService, '/data/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
```

### To Run app 
* python WishService.py 


## Exmaple 

*  api.py
```
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

USERS = {
    '1': {'name': 'adarsh kumar'},
    '2': {'name': 'radha singh'},
    '3': {'name': 'amit kumar'},
}


def abort_if_user_doesnt_exist(id):
    if id not in USERS:
        abort(404, message="User {} doesn't exist".format(id))

parser = reqparse.RequestParser()
parser.add_argument('name')


# User
# shows a single user item and lets you delete a user item
class User(Resource):
    def get(self, id):
        abort_if_user_doesnt_exist(id)
        return USERS[id]

    def delete(self, id):
        abort_if_user_doesnt_exist(id)
        del USERS[id]
        return '', 204

    def put(self, id):
        args = parser.parse_args()
        user = {'name': args['name']}
        USERS[id] = user
        return user, 201


# UserList
# shows a list of all users, and lets you POST to add new user
class UserList(Resource):
    def get(self):
        return USERS

    def post(self):
        args = parser.parse_args()
        id = int(max(USERS.keys()) + 1
        USERS[id] = {'name': args['name']}
        return USERS[id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(UserList, '/user')
api.add_resource(User, '/user/<id>')


if __name__ == '__main__':
    app.run(debug=True)

```

### To Run app 
* python api.py
```
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
 ```

* GET the list
	* $ curl http://localhost:5000/user

* GET a single user
	* $ curl http://localhost:5000/user/1

* DELETE a user
	* $ curl http://localhost:5000/user/1 -X DELETE -v

* Add a new user
	* $ curl http://localhost:5000/user -d "name=sonu singh" -X POST -v

* Update a user
	* $ curl http://localhost:5000/user/4 -d "name=sonu kumar singh" -X PUT -v
---


