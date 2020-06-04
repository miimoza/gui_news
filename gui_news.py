import display
import os
import datetime

def main():
	display.move_cursor(0,0)
	gui_news()
	for i in range(0, 28):
		display.move_cursor(i, 48)
		print("|")


def gui_news():
    # GET NEWS


	os.system('clear')

	print("="*13 + "[" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).center(20) + "]" + "="*13)
	print("-"*14 + " NEWS VITRY ".center(20,"-") + "-"*5 + "-(94)-")
