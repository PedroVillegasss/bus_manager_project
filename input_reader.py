class InputReader:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        file = open(self.filename, "r", encoding = "utf-8")
        input_commands = []
        for line in file:
            command = line.strip().split(" ")
            input_commands.append(command)
        return input_commands
    
