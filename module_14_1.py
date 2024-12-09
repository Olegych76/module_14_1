import sqlite3 as sql

connection = sql.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute('INSERT INTO users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

cursor.execute('UPDATE users SET balance = ? WHERE id%2 != ?', (500, 0))

cursor.execute('DELETE FROM users WHERE (id+2)%3 = ?', (0,))

cursor.execute('SELECT username, email, age, balance FROM users WHERE age != ?', ('60',))

users = cursor.fetchall()

for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()
