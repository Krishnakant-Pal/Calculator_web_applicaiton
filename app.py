from flask import Flask,request,render_template


app = Flask(__name__)


@app.route('/')
def welcome():
    return "<h>Welcome to the Flask</h>"

@app.route('/calculator',methods = ["GET"])
def math_operation():

    operation = request.json('operation')
    number1 = request.json('number1')
    number2 = request.json('number2')

    if operation == 'add':
        result = number1 + number2
    elif operation == 'multiply':
        result = number1 * number2
    elif operation == 'division':
        result = number1 / number2
    elif operation == 'subtraction':
        result = number1 / number2
    else:
        result = "Please provide the proper operation"
    return result
        



if __name__ == '__main__':
    app.run()

