import sqlite3
conn = sqlite3.connect('tf_idf.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
print("users")
print(cursor.fetchall())

# cursor.execute("SELECT * FROM statistics")
# print("statistics")
# print(cursor.fetchall())

cursor.execute("SELECT * FROM documents")
print("documents")
print(cursor.fetchall())

# cursor.execute("SELECT * FROM collection_documents")
# print("collection_documents")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM collections")
# print("collections")
# print(cursor.fetchall())

cursor.close()
# Runing Code
# python -m db_schema.testing_db