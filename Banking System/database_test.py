import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

#c.execute('''CREATE TABLE user_info (name, dob, account_type, amount, username, password)''')

#c.execute("INSERT INTO user_info VALUES ('Max Tiao', '01/03/2000', 'Checking', 1000, 'mtiao', 'mtiao')")


t = ('Max Tiao',)
c.execute('SELECT amount FROM user_info WHERE name=?', t)
amount = c.fetchone()
print(amount[0])


conn.commit()

conn.close()
