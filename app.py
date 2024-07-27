from flask import Flask, render_template, request
from logic_operations import AND, OR, NOT, IMPLICATION, BICONDITIONAL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    A = request.form.get('A') == 'true'
    B = request.form.get('B') == 'true'
    
    results = {
        'AND': AND(A, B),
        'OR': OR(A, B),
        'NOT_A': NOT(A),
        'NOT_B': NOT(B),
        'IMPLICATION': IMPLICATION(A, B),
        'BICONDITIONAL': BICONDITIONAL(A, B)
    }
    
    truth_table = [
        {'A': True, 'B': True},
        {'A': True, 'B': False},
        {'A': False, 'B': True},
        {'A': False, 'B': False},
    ]
    
    for row in truth_table:
        row['AND'] = AND(row['A'], row['B'])
        row['OR'] = OR(row['A'], row['B'])
        row['NOT_A'] = NOT(row['A'])
        row['NOT_B'] = NOT(row['B'])
        row['IMPLICATION'] = IMPLICATION(row['A'], row['B'])
        row['BICONDITIONAL'] = BICONDITIONAL(row['A'], row['B'])
    
    return render_template('results.html', results=results, truth_table=truth_table)

if __name__ == '__main__':
    app.run(debug=True)
