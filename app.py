from flask import *
from dbscript import *

app = Flask(__name__)
app.secret_key = "123"

createDatabase("test.db")

# Check if categories already exist before inserting
with sqlite3.connect("test.db") as conn:
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM CATEGORY")
    category_count = c.fetchone()[0]

    if category_count == 0:
        # Categories don't exist, insert them
        categories = {1: 'Clothes', 2: 'Technology', 3: 'Cars', 4: 'Food', 5: 'Drink'}
        insert_categories("test.db", categories)

    
@app.route('/')
def Home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['Password']
        fullname = request.form['Fullname']
        email = request.form['Email']
        telephone_no = request.form['telephoneNo']

        with sqlite3.connect("test.db") as conn:
            c = conn.cursor()
            # Check if the username already exists
            c.execute("SELECT COUNT(*) FROM USER WHERE username=?", (username,))
            existing_user_count = c.fetchone()[0]

            if existing_user_count == 0:
                # Username doesn't exist, proceed with the insertion
                c.execute("INSERT INTO USER VALUES (?,?,?,?,?)", (username, password, fullname, email, telephone_no))
                conn.commit()
                return render_template('register.html', message="Successfully registered")
            else:
                # Username already exists, show an error message
                return render_template('register.html', message="Username already exists!")

    return render_template('register.html', message="")


@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = sqlite3.connect("test.db")
        c = conn.cursor()
        c.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
        row = c.fetchone()
        conn.close()
        if row != None:
            session["username"] = username
            return render_template('userpage.html', username = username)
        else:
            return render_template('login.html', message = "Wrong Username or Password!")
            
    return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop("username", None)
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
