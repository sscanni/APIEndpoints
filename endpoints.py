from flask import Flask, request
app = Flask(__name__) 
# Create the appropriate app.route functions. Test and see if they work

#Make an app.route() decorator here for when the client sends the URI "/puppies"
@app.route('/puppies', methods=['GET', 'POST'])
def puppiesFunction():
    if request.method == 'GET':
       #Call the method to Get all of the puppies
       return "Yes, GET puppies!"
    if request.method == 'POST':
       #Call the method to make a new puppy
       return "Yes, POST puppies!"
  
 
#Make another app.route() decorator here that takes in an integer named 'id' for when the client visits a URI like "/puppies/5"
@app.route('/puppies/<int:id>', methods=['UPDATE', 'POST', 'DELETE'])
def puppiesFunctionId(id):
  if request.method == 'UPDATE':
     #Call the method to get a specific puppy based on their id
     return "This UPDATE method will act on the puppy with id %s" % id
  if request.method == 'POST':
     return "This POST method will act on the puppy with id %s" % id
     #Call the method to update a puppy
  elif request.method == 'DELETE':
       #Call the method to remove a puppy
       return "This DELETE method will act on the puppy with id %s" % id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	
