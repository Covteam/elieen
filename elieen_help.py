def error(msg):
	print("\033[1;35m[!]"+str(msg)+"\033[0m")

def succed(msg):
	print("\033[1;32m[*]\033[0m"+msg)

def warn(msg):
	print("\033[1;34m[*]\033[0m"+msg)

def tips(msg):
	print("\033[0;32m[*]\033[0m"+msg)