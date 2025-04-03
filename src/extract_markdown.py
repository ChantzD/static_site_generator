import re

def extract_title(markdown):
    for line in markdown.split("\n"):
        if re.match(r"^# ", line):
            return line.strip("# ")
