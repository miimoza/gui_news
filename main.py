import subprocess
import importlib
import gui_news
import display
import time

while True:
    #subprocess.check_call(["git","pull"])
    importlib.reload(gui_news)
    importlib.reload(display)


    #gui_news.main()


    display.move_cursor(49, 0)
    print("="*128)
    for i in range(0, 128):
        display.move_cursor(50, i)
        print('.',end='', flush=True)
        if i % 10 == 0:
            gui_news.printTC()
        time.sleep(30)
