import subprocess
import importlib
import gui_news
import display
import time
import button_wrapper


importlib.reload(button_wrapper)
button_wrapper.main()

while True:
	#subprocess.check_call(["git","pull"])
	importlib.reload(gui_news)
	importlib.reload(display)


	gui_news.main()


	display.move_cursor(28, 0)
	print("="*80)
	for i in range(0, 80):
	    print('.',end='', flush=True)
	    time.sleep(0.2)
