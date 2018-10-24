from flask import Flask, request
app = Flask(__name__) 
# Create the appropriate app.route functions. Test and see if they work

#Make an app.route() decorator here for when the client sends the URI "/puppies"
@app.route('/puppies', methods=['GET', 'POST'])
def puppiesFunction():
    if request.method == 'GET':
       return "Yes, GET puppies!"
    if request.method == 'POST':
       return "Yes, POST puppies!"
  
 
#Make another app.route() decorator here that takes in an integer named 'id' for when the client visits a URI like "/puppies/5"
@app.route('/puppies/<int:id>', methods=['GET', 'POST'])
def puppiesFunctionId(id):
  if request.method == 'GET':
     return "This GET method will act on the puppy with id %s" % id
  if request.method == 'POST':
     return "This POST method will act on the puppy with id %s" % id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	
