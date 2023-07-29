from flask import Flask,request,render_template,jsonify


app = Flask(__name__)


@app.route('/')
def welcome():
    return "<h>Welcome to the Flask</h>"

@app.route('/calculator',methods = ["GET"])
def math_operation():

    operation = request.json["operation"]
    number1 = request.json["number1"]
    number2 = request.json["number2"]

    if operation == "add":
        result = int(number1) + int(number2)
    elif operation == "multiply":
        result = int(number1) * int(number2)
    elif operation == "division":
        result = int(number1) / int(number2)
    elif operation == "subtraction":
        result = int(number1) - int(number2)
    else:
        result = "Please provide the proper operation"
    return "The result is {}".format(result)        


if __name__ == '__main__':
    app.run(debug=True)

