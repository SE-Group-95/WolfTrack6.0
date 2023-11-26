import sqlite3

def create_tables():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS client (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            usertype TEXT NOT NULL
        )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        location TEXT,
        job_position TEXT,
        salary INTEGER,
        status TEXT
    )
    ''')
    conn.commit()
    conn.close()


def add_client(value_set):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    print(value_set)
    # Inserting rows into the 'client' table
    cursor.execute("INSERT INTO client (name, username, password, usertype) VALUES (?, ?, ?, ?)",
                       value_set)
    conn.commit()
    conn.close()

def search_username(data):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Querying the 'client' table
    cursor.execute("SELECT username FROM client Where username = '"+str(data)+"'")
    rows = cursor.fetchone()
    conn.close()
    return rows

def find_user(data):
    conn = sqlite3.connect('database.db')
    print('Data==>', data)
    cursor = conn.cursor()
    # Querying the 'client' table
    cursor.execute("SELECT * FROM client where username ='"+str(data)+"'")
    rows = cursor.fetchone()
    conn.close()
    print('rowsss->>>', rows)
    return rows

def add_job(data):
    conn = sqlite3.connect('database.db')
    print('Data==>', data)
    cursor = conn.cursor()
    # Inserting rows into the 'jobs' table
    cursor.execute("INSERT INTO jobs (company_name, location, job_position, salary, status) VALUES (?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()

