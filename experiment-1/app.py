from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    try:
        n = int(request.args.get('n', 1))
        numbers = [random.randint(0, 100) for _ in range(n)]
        return jsonify(numbers=numbers)
    except ValueError:
        return jsonify(error="Invalid input"), 400


if __name__ == '__main__':
    app.run(debug=True)
