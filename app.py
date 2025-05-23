from flask import Flask, render_template, request, jsonify, session, redirect, url_for


app = Flask(__name__)

users_db = {}

app.secret_key = 'super-secret-key'

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

@app.route('/exp3', methods=['GET', 'POST'])
def exp3():
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if action == 'register':
            if username in users_db:
                return jsonify({'error': 'Username already exists.'}), 400
            users_db[username] = {'email': email, 'password': password}
            return jsonify({'message': 'User registered successfully!'})

        elif action == 'login':
            user = users_db.get(username)
            if user and user['password'] == password:
                session['user'] = username
                return jsonify({'message': f'Welcome {username}!'})
            return jsonify({'error': 'Invalid credentials'}), 401

    return render_template('exp3.html')

@app.route('/exp4', methods=['GET'])
def exp4():
    return render_template('exp4.html')

@app.route('/exp4/user', methods=['POST'])
def exp4_user():
    try:
        numbers = list(map(int, request.form.getlist('numbers')))
        if len(numbers) > 10:
            return render_template('exp4.html', numbers=[], largest="Too many numbers (max 10)")
        largest = max(numbers)
        return render_template('exp4.html', numbers=numbers, largest=largest)
    except Exception:
        return render_template('exp4.html', numbers=[], largest="Invalid input")



if __name__ == '__main__':
    app.run(debug=True)
