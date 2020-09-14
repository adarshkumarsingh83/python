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
		return {'messageId':'welcome to espark for id '+id }


api.add_resource(GreetWorld, '/')
api.add_resource(DataService, '/data/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
```

### To Run app 
* python WishService.py 

---
