from flask import Flask, jsonify, request
from data import data

# define the app variable.
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

##we will create another route function which will take the name 
# of the planet from the URL argument and then find its data in the dictionary
# and then return the data.

@app.route("/planet")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

#explanation of code -
#Here, we are first fetching the name of the planet from the URL argument.
#We are then using the next() function to find a dictionary that satisfies the
#condition, which is, the value of name should match with the name we are
#providing! We are then finally returning only the
#planet’s data this time.##
if __name__ == "__main__":
    app.run()