# generate_data.py

import sqlite3
from faker import Faker
import random

# Create a SQLite database
conn = sqlite3.connect('students.db')  # Database name is specified here
cursor = conn.cursor()

# Create a table for students
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade TEXT,
    performance_score INTEGER
)
''')

# Generate dummy data
fake = Faker()
grades = ['A', 'B', 'C', 'D', 'F']
for _ in range(1200):
    name = fake.name()
    grade = random.choice(grades)
    performance_score = random.randint(0, 100)
    cursor.execute('''
    INSERT INTO students (name, grade, performance_score) VALUES (?, ?, ?)
    ''', (name, grade, performance_score))

# Commit changes and close the connection
conn.commit()
conn.close()