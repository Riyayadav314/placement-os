import sqlite3
import json
import os
from datetime import datetime

DATABASE = "placement.db"


def connect():
    return sqlite3.connect(DATABASE)


# ================= CREATE RESUME TABLES =================

def create_resume_tables():

    conn = connect()

    cursor = conn.cursor()

    # ================= RESUME TABLE =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resume(

        username TEXT PRIMARY KEY,

        objective TEXT,

        linkedin TEXT,

        github TEXT

    )
    """)

    # ================= SKILLS TABLE =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        skill TEXT

    )
    """)

    # ================= PROJECTS TABLE =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        title TEXT,

        description TEXT,

        technology TEXT,

        github_link TEXT

    )
    """)

    # ================= INTERNSHIP TABLE =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS internships(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        company TEXT,

        role TEXT,

        duration TEXT,

        description TEXT

    )
    """)

    # ================= CERTIFICATES TABLE =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS certificates(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        certificate_name TEXT,

        organization TEXT,

        year TEXT

    )
    """)

    # ================= LANGUAGES TABLE =================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS languages(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        language TEXT

    )
    """)

    conn.commit()

    conn.close()

    print("✅ Resume Tables Created Successfully")
    # ================= SAVE RESUME =================

def save_resume(username, objective, linkedin, github):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO resume
    (username, objective, linkedin, github)
    VALUES (?, ?, ?, ?)
    """, (
        username,
        objective,
        linkedin,
        github
    ))

    conn.commit()

    conn.close()

    return True


# ================= LOAD RESUME =================

def load_resume(username):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM resume
        WHERE username=?
        """,
        (username,)
    )

    data = cursor.fetchone()

    conn.close()

    return data


# ================= UPDATE RESUME =================

def update_resume(username, objective, linkedin, github):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE resume

    SET

    objective=?,

    linkedin=?,

    github=?

    WHERE username=?

    """, (

        objective,

        linkedin,

        github,

        username

    ))

    conn.commit()

    conn.close()

    return True


# ================= DELETE RESUME =================

def delete_resume(username):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM resume WHERE username=?",

        (username,)

    )

    conn.commit()

    conn.close()

    return True
# ================= SAVE SKILL =================

def save_skill(username, skill):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO skills(username, skill)
        VALUES(?, ?)
        """,
        (username, skill)
    )

    conn.commit()

    conn.close()

    return True


# ================= LOAD SKILLS =================

def load_skills(username):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT skill
        FROM skills
        WHERE username=?
        ORDER BY id
        """,
        (username,)
    )

    data = cursor.fetchall()

    conn.close()

    return data


# ================= DELETE SKILL =================

def delete_skill(username, skill):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM skills
        WHERE username=? AND skill=?
        """,
        (username, skill)
    )

    conn.commit()

    conn.close()

    return True


# ================= DELETE ALL SKILLS =================

def delete_all_skills(username):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM skills
        WHERE username=?
        """,
        (username,)
    )

    conn.commit()

    conn.close()

    return True
# ================= SAVE PROJECT =================

def save_project(username, title, description, technology, github_link):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO projects
    (username, title, description, technology, github_link)
    VALUES (?, ?, ?, ?, ?)
    """, (
        username,
        title,
        description,
        technology,
        github_link
    ))

    conn.commit()

    conn.close()

    return True


# ================= LOAD PROJECTS =================

def load_projects(username):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT title,
           description,
           technology,
           github_link
    FROM projects
    WHERE username=?
    ORDER BY id
    """, (username,))

    data = cursor.fetchall()

    conn.close()

    return data


# ================= DELETE PROJECT =================

def delete_project(username, title):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM projects
    WHERE username=? AND title=?
    """, (
        username,
        title
    ))

    conn.commit()

    conn.close()

    return True


# ================= DELETE ALL PROJECTS =================

def delete_all_projects(username):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM projects
    WHERE username=?
    """, (username,))

    conn.commit()

    conn.close()

    return True
# ================= SAVE INTERNSHIP =================

def save_internship(username, company, role, duration, description):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO internships
    (username, company, role, duration, description)
    VALUES (?, ?, ?, ?, ?)
    """, (
        username,
        company,
        role,
        duration,
        description
    ))

    conn.commit()
    conn.close()

    return True


# ================= LOAD INTERNSHIPS =================

def load_internships(username):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT company, role, duration, description
    FROM internships
    WHERE username=?
    ORDER BY id
    """, (username,))

    data = cursor.fetchall()

    conn.close()

    return data


# ================= DELETE ALL INTERNSHIPS =================

def delete_all_internships(username):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM internships WHERE username=?",
        (username,)
    )

    conn.commit()
    conn.close()

    return True


# ================= SAVE CERTIFICATE =================

def save_certificate(username, certificate_name, organization, year):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO certificates
    (username, certificate_name, organization, year)
    VALUES (?, ?, ?, ?)
    """, (
        username,
        certificate_name,
        organization,
        year
    ))

    conn.commit()
    conn.close()

    return True


# ================= LOAD CERTIFICATES =================

def load_certificates(username):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT certificate_name, organization, year
    FROM certificates
    WHERE username=?
    ORDER BY id
    """, (username,))

    data = cursor.fetchall()

    conn.close()

    return data


# ================= DELETE ALL CERTIFICATES =================

def delete_all_certificates(username):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM certificates WHERE username=?",
        (username,)
    )

    conn.commit()
    conn.close()

    return True


# ================= SAVE LANGUAGE =================

def save_language(username, language):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO languages(username, language) VALUES(?, ?)",
        (username, language)
    )

    conn.commit()
    conn.close()

    return True


# ================= LOAD LANGUAGES =================

def load_languages(username):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT language FROM languages WHERE username=? ORDER BY id",
        (username,)
    )

    data = cursor.fetchall()

    conn.close()

    return data


# ================= DELETE ALL LANGUAGES =================

def delete_all_languages(username):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM languages WHERE username=?",
        (username,)
    )

    conn.commit()
    conn.close()

    return True


# ================= MAIN =================

if __name__ == "__main__":

    create_resume_tables()