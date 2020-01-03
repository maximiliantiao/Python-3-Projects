from getpass import getpass
import sqlite3
import os

class Banking_Sys():

	def __init__(self):
		# Variables that methods will use when getting bank info
		self.acc_name = ""
		self.acc_dob = ""
		self.acc_type = ""
		self.acc_amount = 0
		self.acc_username = ""
		self.acc_password = ""
		pass

	# 
	# Authenticate user login information. Return True if login information is correct. Otherwise, return False
	#
	# user_name -> user inputted username
	# pass_word -> user inputted password
	#
	def login(self, user_name, pass_word):
		conn = sqlite3.connect('bank_info.db')
		c = conn.cursor()
		# Get information from user_name. If information == None, method returns False
		c.execute("SELECT * FROM users_info WHERE username=?", (user_name,))			
		user = c.fetchone()
		if user == None:
			conn.commit()
			conn.close()
			return False
		self.acc_name = user[0]
		self.acc_dob = user[1]
		self.acc_type = user[2]
		self.acc_amount = user[3]
		self.acc_username = user[4]
		self.acc_password = user[5]

		if self.acc_username == user_name and self.acc_password == pass_word:
			conn.commit()
			conn.close()
			return True
		else:
			conn.commit()
			conn.close()
			return False

	#
	# Display welcome message and brief user with preliminary information of bank account
	#
	def get_info(self):
		print("\n**** Welcome %s! ****\n" % (self.acc_name))
		print("Your %s account currently have $%d in your account." % (self.acc_type, self.acc_amount))

	#
	# Withdraw amount from the bank account
	#
	# pass_word -> user's password
	# take_amount -> amount to take out from the current amount in the account
	#
	def withdraw(self, pass_word, take_amount):
		new_amount = self.acc_amount - take_amount
		if new_amount < 0:
			print("Invalid amount. Withdraw limit is %d" % self.acc_amount)
			return False

		conn = sqlite3.connect('bank_info.db')
		c = conn.cursor()
		c.execute('UPDATE users_info SET amount=? WHERE password=?', (new_amount, pass_word))

		conn.commit()
		conn.close()

	#
	# Deposit amount to the bank account
	#
	# pass_word -> user's password
	# add_amount -> amount to add to the current amount in the account
	#
	def deposit(self, pass_word, add_amount):
		new_amount = self.acc_amount + add_amount
		conn = sqlite3.connect('bank_info.db')
		c = conn.cursor()

		c.execute('UPDATE users_info SET amount=? WHERE password=?', (new_amount, pass_word))

		conn.commit()
		conn.close()

	#
	# Change the password to the account
	#
	# pass_word -> user's new password
	#
	def change_password(self, pass_word):
		conn = sqlite3.connect('bank_info.db')
		c = conn.cursor()
		c.execute('UPDATE users_info SET password=? WHERE username=?', (pass_word, self.acc_username))
		conn.commit()
		conn.close()

# end class

if __name__ == '__main__':
	banking = Banking_Sys()
	while True:
		print("\nWelcome to Simple Banking!")
		print("1. Create a new account")
		print("2. Login")
		print("3. Exit")

		option = int(input("Enter here: "))

		if option == 1:
			acc_name = str(input("Name: "))
			acc_dob = str(input("Date of Birth (MM/DD/YYYY): "))
			acc_username = str(input("Username: "))
			acc_password = str(input("Password: "))

			print("Please select an account type")
			print("1. Checking")
			print("2. Savings")
			number = int(input('Enter here: '))

			acc_type = "Checking" if number == 1 else "Savings"

			deposit = input("Would you like to deposit an amount? (y/n) ")

			if deposit == 'y':
				acc_amount = int(input("Enter amount: "))
			else:
				acc_amount = 0

			if os.stat('bank_info.db').st_size == 0:
				conn = sqlite3.connect('bank_info.db')
				c = conn.cursor()
				c.execute('''CREATE TABLE users_info (name text, dob text, account_type text, amount real, username text, password text)''')
				c.execute('INSERT INTO users_info VALUES (?, ?, ?, ?, ?, ?)', (acc_name, acc_dob, acc_type, acc_amount, acc_username, acc_password))
				
				conn.commit()
				conn.close()
			
			else:
				conn = sqlite3.connect('bank_info.db')
				c = conn.cursor()
				c.execute('INSERT INTO users_info VALUES (?, ?, ?, ?, ?, ?)', (acc_name, acc_dob, acc_type, acc_amount, acc_username, acc_password))
				conn.commit()
				conn.close()

		elif option == 2 :
			correct_login = False
			while not correct_login:
				login = input("Username: ")
				secret = getpass()
				correct_login = banking.login(login, secret)
			# end while

				if correct_login:
					banking.get_info()
					while True:
						print("\nPlease select one of the following actions: ")
						print("1. Deposit")
						print("2. Withdraw")
						print("3. More Actions")
						print("4. Go Back to Previous Menu")

						choice = int(input("Enter here: "))

						if choice == 1:
							to_add = int(input("\nEnter amount to deposit to account: "))
							banking.deposit(secret, to_add)
						elif choice == 2:
							to_take = int(input("\nEnter amount to withdraw from account: "))
							while to_take > banking.acc_amount:
								to_take = int(input("Enter amount to withdraw from account: "))

							banking.withdraw(secret, to_take)
						elif choice == 3:
							while True:
								print("\nPlease select one of the following actions: ")
								print("1. View your information")
								print("2. Change your password")
								print("3. Go Back to Previous Menu")

								choice = int(input("Enter here: "))
								if choice == 1:
									print("\n*Your Information*")
									print("Name: %s" % banking.acc_name)
									print("Date of Birth: %s" % banking.acc_dob)
									print("Account type: %s" % banking.acc_type)
									print("Account amount: %d" % banking.acc_amount)
									print("Username: %s" % banking.acc_username)
									print("Password: %s" % banking.acc_password)
								elif choice == 2:
									new_secret = input("\nEnter a new password: ")
									banking.change_password(new_secret)
								elif choice == 3:
									break
								else:
									print("Invalid option. Enter a valid option!")
							# end while

						elif choice == 4:
							break
						else:
							print("Invalid option. Enter a valid option!")
					# end while
					
				else:
					print("Incorrect username or password!")

		elif option == 3:
			print("Thank you for using Simple Banking. Goodbye!")
			exit(0)
		else:
			print("Invalid option. Enter a valid option!")
	# end while

# end of main
	


