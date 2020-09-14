# python rest services 

---

## Two approach for rest api development using 
* S/W installation for web base pyhton 

---

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

@app.route('/',method = ['POST', 'GET'])
def wish():
     if (request.method == 'POST'):
        dataPayload = request.get_json()
	    return jsonify({'requestPayload': dataPayload }) , 201
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

### Flast-RESTful for rest api 
* $ pip install Flast-RESTful 



---
