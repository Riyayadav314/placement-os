import sqlite3
import bcrypt

DATABASE = "placement.db"


def connect():

    conn = sqlite3.connect(DATABASE)

    return conn


def create_table():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users(

        username TEXT PRIMARY KEY,

        password TEXT,

        fullname TEXT,

        college TEXT,

        branch TEXT,

        cgpa REAL,
        
        email TEXT,
        
        mobile TEXT,
        
        city TEXT,
        
        address TEXT

    )

    """)

    conn.commit()

    conn.close()

    print("✅ Database Created Successfully")


# ================= ADD USER =================

def add_user(username, password, fullname, college, branch, cgpa, email, mobile,city,address):

    conn = connect()

    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    cursor.execute("""
    INSERT INTO users
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        username,
        hashed_password,
        fullname,
        college,
        branch,
        cgpa,
        email,
        mobile,
        city,
        address
    ))

    conn.commit()

    conn.close()

    print("✅ User Added Successfully")

# ================= CHECK USER =================

def check_user(username):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    return user is not None


# ================= LOGIN =================

def login_user(username, password):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        stored_password = user[1]

        if bcrypt.checkpw(
            password.encode(),
            stored_password.encode()
        ):

            return user

    return None


# ================= UPDATE PROFILE =================

def update_profile(
    username,
    fullname,
    college,
    branch,
    cgpa,
    email,
    mobile,
    city,
    address
):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users
    SET
        fullname=?,
        college=?,
        branch=?,
        cgpa=?,
        email=?,
        mobile=?,
        city=?,
        address=?
    WHERE username=?
    """, (
        fullname,
        college,
        branch,
        cgpa,
        email,
        mobile,
        city,
        address,
        username
    ))

    conn.commit()

    conn.close()

    print("✅ Profile Updated Successfully")
    
    # ================= CHANGE PASSWORD =================

def update_password(username, new_password):

    conn = connect()

    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(
        new_password.encode(),
        bcrypt.gensalt()
    ).decode()

    cursor.execute("""
    UPDATE users
    SET password=?
    WHERE username=?
    """, (hashed_password, username))

    conn.commit()

    conn.close()

    print("✅ Password Updated Successfully")

    # ================= ADMIN DATA =================

def get_admin_data():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT fullname, cgpa FROM users ORDER BY cgpa DESC LIMIT 1")
    top_student = cursor.fetchone()

    conn.close()

    return users, total_users, top_student

# ================= LEADERBOARD =================

def get_leaderboard():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT fullname, cgpa
    FROM users
    ORDER BY cgpa DESC
    """)

    students = cursor.fetchall()

    conn.close()

    return students
# ================= SEARCH USER =================

def search_user(username):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE username=?
    """, (username,))

    user = cursor.fetchone()

    conn.close()

    return user

# ================= DELETE USER =================

def delete_user(username):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM users
    WHERE username=?
    """, (username,))

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    return deleted

# ================= EXPORT USERS =================

def export_users():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT username, fullname, college, branch, cgpa
    FROM users
    """)

    users = cursor.fetchall()

    conn.close()

    return users


# ================= SHOW USERS =================

def show_users():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    for user in users:
        print(user)

    conn.close()


# ================= MAIN =================

if __name__ == "__main__":

    create_table()

    # Example
    # add_user("riya123", "12345", "Riya Yadav", "United University", "AIML", 8.5)

    show_users()