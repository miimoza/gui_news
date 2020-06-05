import subprocess
import importlib
import gui_news
import display
import time

while True:
	#subprocess.check_call(["git","pull"])
	importlib.reload(gui_news)
	importlib.reload(display)


	gui_news.main()


	display.move_cursor(49, 0)
	print("="*128)
	for i in range(0, 128):
	    print('.',end='', flush=True)
	    time.sleep(0.2)
