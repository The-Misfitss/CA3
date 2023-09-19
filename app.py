from flask import Flask, render_template, request

from functions import add

from functions import multiply

from functions import divide

from flask import Flask, jsonify

app = Flask(__name__)



@app.route('/calc/add/<int:num1>/<int:num2>', methods=['GET'])
def add_route(num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    result = add(num1, num2)

    return f'{result}'

@app.route('/calc/multiply/<int:num1>/<int:num2>', methods=['GET'])
def add_route(num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    result = multiply(num1, num2)

    return f'{result}'

@app.route('/calc/divide/<int:num1>/<int:num2>', methods=['GET'])
def add_route(num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    result = divide(num1, num2)

    return f'{result}'


if __name__ == '__main__':

    app.run(host='0.0.0.0',port=5000)

 