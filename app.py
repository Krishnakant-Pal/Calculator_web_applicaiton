from flask import Flask,request,render_template,jsonify

app = Flask(__name__)


dic = {"add":"+","subtract":"-","multiply":"*","divide": '/'}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/calculator')
def index():
    return render_template('calculate.html')


@app.route('/calculate',methods = ["POST","GET"])
def math_operation():   
    try: 
    
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                return "<h3>Error: Cannot divide by 0</h3>"

        return render_template('result.html', num1=num1, num2=num2, operation=dic[operation], result=result)

    except ValueError:
        return "<h3>Error: Invalid input. Please enter valid numbers.</h3>"


if __name__ == '__main__':
    app.run(debug=True)

