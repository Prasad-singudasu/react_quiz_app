import sqlite3

# Connect to database
conn = sqlite3.connect('learning_agent.db')
cursor = conn.cursor()

print("\n=== LEARNING SESSIONS ===")
cursor.execute("SELECT * FROM learning_sessions")
for row in cursor.fetchall():
    print(row)

print("\n=== QUIZ ATTEMPTS ===")
cursor.execute("SELECT * FROM quiz_attempts")
for row in cursor.fetchall():
    print(row)

print("\n=== CHECKPOINTS ===")
cursor.execute("SELECT * FROM checkpoints")
for row in cursor.fetchall():
    print(row)

conn.close()
