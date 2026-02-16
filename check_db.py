import sqlite3
import os

# Check if database file exists
db_path = "learning_agent.db"
if os.path.exists(db_path):
    print(f"✅ Database file exists: {db_path}")
    print(f"   File size: {os.path.getsize(db_path)} bytes\n")
else:
    print(f"❌ Database file NOT found: {db_path}\n")
    exit()

# Connect and check tables
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(f"📊 Tables in database: {[t[0] for t in tables]}\n")

# Check each table
for table in tables:
    table_name = table[0]
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"Table '{table_name}': {count} records")
    
    if count > 0:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
        rows = cursor.fetchall()
        print(f"  Sample data: {rows[:2]}")
    print()

conn.close()

print("\n💡 If you see 0 records:")
print("   1. Make sure backend is running: python main.py")
print("   2. Take a quiz in the app")
print("   3. Check backend terminal for errors")
