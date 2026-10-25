import sqlite3 

# 1. connect to database
connection = sqlite3.connect("servers.db")
cursor = connection.cursor()

# 2. create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS servers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL
)
""")

# 3. insert servers without creating duplicates
servers = [
    ("web-server-01", "Running"),
    ("web-server-02", "Running"),
    ("app-server-01", "Stopped")
]

cursor.executemany("""
INSERT OR IGNORE INTO servers (name, status)
VALUES (?, ?)
""", servers)

connection.commit()

# 4. display all servers
print("\n--- Server Inventory ---")

cursor.execute("SELECT id, name, status FROM servers")
for server in cursor.fetchall():
    print(server)

# 5. update a server's status
cursor.execute("""
UPDATE servers
SET status = ?
WHERE name = ?
""", ("Stopped", "web-server-01"))

connection.commit()

print("\n--- Inventory After Update ---")

cursor.execute("SELECT id, name, status FROM servers")
for server in cursor.fetchall():
    print(server)

# 6. close database connection
connection.close()

print("\nPractical completed successfully!")