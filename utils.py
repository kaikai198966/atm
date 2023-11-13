import os  # NOTE: can be omitted
import time

timestamp = lambda: time.strftime("%Y/%m/%d_%H:%M:%S")

clear_console = lambda: os.system(
    "cls" if os.name == "nt" else "clear"
)  # NOTE: may be omitted, also omit line 1
