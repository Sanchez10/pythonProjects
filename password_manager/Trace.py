import datetime

class TraceLogger:
    def __init__(self, trace_file, default_color="white") -> None:
        self.trace_file = trace_file
        self.default_color = default_color
        self.write_trace("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<title>Trace Log</title>\n<style>\nbody {\nfont-family: Arial, sans-serif;\ncolor: white;\nbackground-color: black;\n}\n\n.error {\ncolor: red;\n}\n</style>\n</head>\n<body>\n<h1>Trace Log</h1>\n<div id=\"log\">\n")

    def write_trace(self, message, is_error=False, color=None) -> None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"[{timestamp}] {message}"
        text_color = color if color else (self.default_color if not is_error else "red")  # Definir cor baseada no erro ou padrão
        
        with open(self.trace_file, "a") as f:
            f.write(f"<p style='color: {text_color};'>" + formatted_message + "</p>\n")

    def close(self) -> None:
        with open(self.trace_file, "a") as f:
            f.write("</div>\n</body>\n</html>")
            