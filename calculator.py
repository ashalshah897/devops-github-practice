from flask import Flask, render_template, request

app = Flask(__name__)

# Math functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

# This shows your index.html page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# This does the math when you click the button
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        n1 = float(request.form['num1'])
        n2 = float(request.form['num2'])
        op = request.form['operation']
        
        if op == 'add': result = add(n1, n2)
        elif op == 'subtract': result = subtract(n1, n2)
        elif op == 'multiply': result = multiply(n1, n2)
        
        return f"<h1>The Answer is: {result}</h1><br><a href='/'>Go Back</a>"
    except Exception as e:
        return f"Error: {e}<br><a href='/'>Go Back</a>"

if __name__ == '__main__':
    # nosonar: This line is safe for my local DevOps practice
    app.run(host='0.0.0.0', port=5000)  # NOSONAR
