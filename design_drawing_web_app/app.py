import sqlite3
from flask import Flask, render_template, request

# connect to database
conn = sqlite3.connect('login_db.db')
# create cursor object
cursor = conn.cursor()
print("Successfully connected to the database")
# check if table exists
tables_list = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'
                             AND name='design_user_details'; """).fetchall()
if not tables_list:
    print('Table not found!')
    # Create table in login_db database with four columns.
    conn.execute("""CREATE TABLE design_user_details(name VARCHAR(100), email VARCHAR(200), phone_no INT, 
                 password VARCHAR(100)); """)
    print("Table is created")
else:
    print('Table found!')
# commit changes
conn.commit()
# terminate the connection
conn.close()

app = Flask(__name__)


@app.route('/')
def home():
    """Displays login page which takes email and password for authentication."""
    return render_template('login_page.html')


@app.route('/register')
def register():
    """Displays register page which takes the user details and stores into the database."""
    return render_template('registration_page.html')


@app.route('/add', methods=['POST'])
def add():
    """If details are stored in the table success message is displayed else error message is displayed."""
    # getting user entered details using the name attribute from the form
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['ph_no']
        password = request.form['pwd']
        # If the form details are empty show the error message
        if name == '':
            msg = "Please Input Name"
        elif email == '':
            msg = "Please Input Email ID"
        elif contact == '':
            msg = "Please Input Phone Number"
        elif password == '':
            msg = "Please Input Password"
        else:
            conn = sqlite3.connect('login_db.db')
            cursor = conn.cursor()
            record = cursor.execute(f"SELECT * FROM design_user_details WHERE email='{email}'")
            if record.fetchone():
                msg = "Email is already exists. Create account using another email."
            else:
                print("Empty Row")
                try:
                    cursor.execute("INSERT INTO design_user_details(name, email, phone_no, password) VALUES (?, ?, ?, ?)", 
                                   (name, email, contact, password))
                    conn.commit()
                    msg = "New record is created successfully"
                except:
                    conn.rollback()
                    msg = "Error..! couldn't insert the details into the database."
            conn.close()
    return render_template("registration_page.html", msg=msg)


@app.route('/check', methods=['POST'])
def check():
    """If login credentials are existed in the table their details will be displayed
    else registration form is displayed."""
    # getting user entered details using the name attribute from the form
    email = request.form['email']
    password = request.form['pwd']
    # If the form details are empty show the error message
    if email == '':
        msg = "Please Input Email ID"
    elif password == '':
        msg = "Please Input Password"
    else:
        conn = sqlite3.connect('login_db.db')
        cursor = conn.cursor()
        record = cursor.execute(f"SELECT * FROM design_user_details WHERE email='{email}' AND password='{password}';")
        if record.fetchone():
            return render_template("design_page.html", user_details=record)
        else:
            msg = "Your don't have an account. Please create account using below link."
        conn.close()
    return render_template("login_page.html", msg=msg)


app.run(debug=True)
