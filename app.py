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

@app.route('/exp2', methods=['GET', 'POST'])
def exp2():
    if request.method == 'POST':
        data = request.json
        A = data.get('matrixA')
        B = data.get('matrixB')

        if not A or not B or len(A[0]) != len(B):
            return jsonify(error="Invalid matrix dimensions for multiplication."), 400

        # Multiply matrices
        result = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
        return jsonify(result=result)

    return render_template('exp2.html')
    


if __name__ == '__main__':
    app.run(debug=True)
