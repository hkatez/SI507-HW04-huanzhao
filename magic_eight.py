import random

def random_answer():
	answers = ["it's certain.", "It's decidely so.", "Without a doubt.","Yes, definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.", "Yes.","Signs point to yes.","Reply hazy try again.","Ask again later.","Better not tell you.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.", "My sources say no.","Outlook not so good.","Very doubtful."]
	random_number = random.randint(0,19)
	random_answer = answers[random_number]
	return random_answer

ask = input("what is your question?")

if ask[-1] != "?":
	if ask != "quit":
		print("I'm sorry, I can only answer questions.")
	else:
		exit()
else:
	print(random_answer())






