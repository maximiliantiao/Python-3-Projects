import json

class Banking_Sys():
	def __init__(self):
		pass

	def login(self, username, password):
		with open('user_info.txt', 'r') as infile:
			user_info = json.load(infile)
			for data in user_info[username]:
				if data['username'] == username and data['password'] == password:
					return True
				else:
					return False



if __name__ == '__main__':
	banking = Banking_Sys()
	print("Welcome!")
	print("1. Create a new account")
	print("2. Login")
	print("3. Exit")

	option = int(input("Enter here: "))
	if option == 1:
		user_info = {}
		name = input("Name: ")
		dob = input("Date of Birth (MM/DD/YYYY): ")
		username = input("Username: ")
		password = input("Password: ")
		user_info[username].append({
			'name' : name,
			'dob' : dob,
			'username' : username,
			'password' : password
		})
		with open('user_info.txt', 'a') as outfile:
			json.dump([user_info], outfile)


	elif option == 2 :
		correct_login = False
		while not correct_login:
			username = input("Username: ")
			password = input("Password: ")
			correct_login = banking.login(username, password)
			if correct_login:
				print("Correct login!")
			else:
				print("Incorrect login!")

	elif option == 3:
		pass
	else:
		print("Error!")
	


