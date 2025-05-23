from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Experiment 1: generate n even numbers
@app.route('/exp1', methods=['GET', 'POST'])
def exp1():
    if request.method == 'POST':
        n = int(request.form.get('n', 0))
        numbers = [x*2 for x in range(1, n+1)]
        return jsonify(numbers=numbers)
    return render_template('exp1.html')




if __name__ == '__main__':
    app.run(debug=True)
