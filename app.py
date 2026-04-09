from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Label
from datetime import datetime
import psutil

class SystemTui(App):
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

    timeDiv = """  
██
  
██
  """
    
    timeTriangleLeft = """    ██
  ██  
██    
  ██  
    ██"""

    timeTriangleRight = """██    
  ██  
    ██
  ██  
██    """
    CSS = """
    #container{
        color: #bcb9b2;
    }
    #clock,.comment{
        color: #fac118;
    }
    #clock{
        width: 100%;
        content-align: center middle;
    }
    #stats {
        align-horizontal: center;
    }"""

    def on_mount(self):
        self.clockLabel = self.query_one("#clock")
        self.memLabel = self.query_one("#memory")
        self.cpuLabel = self.query_one("#cpu")

        self.update_stats()
        self.set_interval(1, self.update_stats)

    def compose(self) -> ComposeResult:
        yield Container(
            Label("",id="clock"),
            Horizontal(
                Label("//MEM ", classes="comment"),
                Label("", id="memory"),
                Label("  "),
                Label("//CPU ", classes="comment"),
                Label("", id="cpu"),
            id="stats"
            ),
        id="container"
        )

    def update_stats(self):
        #Clock
        h1, h2 = divmod(datetime.now().hour, 10)
        m1, m2 = divmod(datetime.now().minute, 10)
        self.clockLabel.update(self.format_time(
            self.timeTriangleLeft,
            self.numbers[h1], self.numbers[h2], 
            self.timeDiv,
            self.numbers[m1], self.numbers[m2],
            self.timeTriangleRight)
        )

        #Memory
        self.memLabel.update(self.get_mem_usage())

        #CPU
        self.cpuLabel.update(self.get_cpu_usage())

    def get_mem_usage(self):
        return str(round(psutil.virtual_memory().percent)) + "%"

    def get_cpu_usage(self):
        return str(round(psutil.cpu_percent())) + "%"
    
    def format_time(self, *digits, sep="  "):
        lines = []
        for d in digits:
            lines.append(d.split("\n"))

        rows = zip(*lines)
        joined_rows = []
        
        for row in rows:
            joined_rows.append(sep.join(row))

        return "\n".join(joined_rows)
    
if __name__ == "__main__":
    app = SystemTui()
    app.run()