import curses
import os
import time
from datetime import datetime

import psutil
from rich.live import Live
from rich.text import Text

numbers = [
    """██████
██  ██
██  ██
██  ██
██████""",
    """████  
  ██  
  ██  
  ██  
██████""",
    """██████
    ██
██████
██    
██████""",
    """██████
    ██
██████
    ██
██████""",
    """██  ██
██  ██
██████
    ██
    ██""",
    """██████
██    
██████
    ██
██████""",
    """██████
██    
██████
██  ██
██████""",
    """██████
    ██
    ██
    ██
    ██""",
    """██████
██  ██
██████
██  ██
██████""",
    """██████
██  ██
██████
    ██
██████""",
]

time_div = """  
██
  
██
  """

tri_left = """    ██
  ██  
██    
  ██  
    ██"""

tri_right = """██    
  ██  
    ██
  ██  
██    """


def format_time(*digits, sep="  "):
    lines = [d.split("\n") for d in digits]
    return "\n".join(sep.join(row) for row in zip(*lines))


def get_mem_usage():
    return str(round(psutil.virtual_memory().percent)) + "%"


def get_cpu_usage():
    return str(round(psutil.cpu_percent())) + "%"


def get_clock():
    now = datetime.now()
    h1, h2 = divmod(now.hour, 10)
    m1, m2 = divmod(now.minute, 10)
    return format_time(
        tri_left,
        numbers[h1],
        numbers[h2],
        time_div,
        numbers[m1],
        numbers[m2],
        tri_right,
    )


def center_block(text: str) -> str:
    cols = os.get_terminal_size().columns
    rows = os.get_terminal_size().lines
    lines = text.split("\n")
    v_pad = max((rows - len(lines)) // 2, 0)
    centered = [line.center(cols) for line in lines]
    return "\n" * v_pad + "\n".join(centered)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    try:
        initial = (
            get_clock() + f"\n\n//MEM {get_mem_usage()}    //CPU {get_cpu_usage()}"
        )
        with Live(
            Text.from_markup(center_block(initial)), refresh_per_second=1
        ) as live:
            while True:
                content = (
                    get_clock()
                    + f"\n\n//MEM {get_mem_usage()}    //CPU {get_cpu_usage()}"
                )
                live.update(Text.from_markup(center_block(content)))
                time.sleep(1)

    except KeyboardInterrupt:
        os.system("cls" if os.name == "nt" else "clear")
