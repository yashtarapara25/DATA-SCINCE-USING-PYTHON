import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('pm_poshan.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bills
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, bill_name TEXT, amount REAL, date TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS grants
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, grant_name TEXT, allocated_amount REAL, date TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, expense_name TEXT, amount REAL, date TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_bill', methods=['POST'])
def add_bill():
    bill_name = request.form['bill_name']
    amount = request.form['amount']
    date = request.form['date']
    
    conn = sqlite3.connect('pm_poshan.db')
    c = conn.cursor()
    c.execute("INSERT INTO bills (bill_name, amount, date) VALUES (?, ?, ?)", (bill_name, amount, date))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/add_grant', methods=['POST'])
def add_grant():
    grant_name = request.form['grant_name']
    allocated_amount = request.form['allocated_amount']
    date = request.form['date']
    
    conn = sqlite3.connect('pm_poshan.db')
    c = conn.cursor()
    c.execute("INSERT INTO grants (grant_name, allocated_amount, date) VALUES (?, ?, ?)", (grant_name, allocated_amount, date))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    expense_name = request.form['expense_name']
    amount = request.form['amount']
    date = request.form['date']
    
    conn = sqlite3.connect('pm_poshan.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (expense_name, amount, date) VALUES (?, ?, ?)", (expense_name, amount, date))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
