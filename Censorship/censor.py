import sys, getopt

if __name__ == '__main__':
	# Building array of bad_words
	bad_words = []
	bad_words_found = []
	words = "hello"
	file = open("badwords.txt", "r")
	for x in file:
		bad_words.append(x[:-1])

	file.close()


	user_input_file = False
	user_output_file = False
	verbose_show = False
	total_words = 0
	input_file = 0
	output_file = 0

	full_cmd_arguments = sys.argv
	argument_list = full_cmd_arguments[1:]
	unix_options = "vi:o:"
	try:
		arguments, values = getopt.getopt(argument_list, unix_options)
		for current_arg, current_value in arguments:
			if current_arg in ("-v"):
				verbose_show = True
				#print("Will display verbose option")
			elif current_arg in ("-i"):
				user_input_file = True
				input_file = current_value
				#print("Will use input file: %s" % curr_value)
			elif current_arg in ("-o"):
				user_output_file = True
				output_fule = current_value
				#print("Will use output file: %s" % curr_value)
	except getopt.error as err:
		print(str(err))
		exit(1)

	if (user_input_file == False):
		input = input("Enter words: ")
		print("\n")
		print("Censored Translation: ")
		std_input = input.split()
		for word in std_input:
			total_words += 1
			if word not in bad_words:
				if (user_output_file == False):
					print(word, end=" ")
			else:
				bad_words_found.append(word)

		print("\n")

	elif user_input_file:
		file_input = open(input_file, "r")
		file_output = 0
		if (user_output_file):
			file_output = open(output_file, "w")

		file_words = file_input.read()
		split_words = file_words.split()
		for word in split_words:
			total_words += 1
			if word not in bad_words:
				if (user_output_file == False):
					print(word, end=" ")
				else:
					file_output.write(word)
			else:
				bad_words_found.append(word)
		print("\n")
		file_input.close()
	
	if verbose_show:
		print("Number of words inputted: %d" % total_words)
		print("Number of words censored: %d" % len(bad_words_found))
		print("Number of words uncensored %d\n" % int(total_words - len(bad_words_found)))

		if (len(bad_words_found) != 0):
			print("Below are the bad words found: ")
			for found in bad_words_found:
				print(found)














	
	