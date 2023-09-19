from flask import Flask, render_template, request
from functions import add
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/calc/add/<int:num1>/<int:num2>', methods=['GET'])
def add_route(num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    result = add(num1, num2)

    return f'{result}'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)