import os
import time

timestamp = lambda: time.strftime("%Y/%m/%d_%H:%M:%S")

clear_console: lambda: os.system("cls" if os.name == "nt" else "clear")