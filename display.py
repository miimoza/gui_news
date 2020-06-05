import os
import re

def move_cursor(y, x):
	os.system("tput cup " + str(y) + " " + str(x))

def print_n(w, n, s):
	move_cursor(n, w)
	print(s)

	return n+1

# w = 0, n = 2, width=80, n_max = 5, text=""
def breakline_n(w, n, width, n_max,  text):
	if n >= n_max:
		return n;
	#print("l:", w, n, width, n_max, text)
	#return
	lines = []
	for i in range(0, len(text), width):
		lines.append(text[i:i+width])

	for l in lines:
		print_n(w, n,l)
		n += 1
		if n + 1 > n_max:
			return n;

	return n

    #return '\n'.join(lines)
	#return re.sub("(.{" + str(width) + "})", "\\1\n", text, 0, re.DOTALL)

def remove_link(text):
	return re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
