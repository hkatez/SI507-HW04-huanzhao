def question():
	ask = input("what is your question?")
	if ask[-1] != "?":
		if ask != "quit":
			print("I'm sorry, I can only answer questions.")
		else:
			exit()

		else: