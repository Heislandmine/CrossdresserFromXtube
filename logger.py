class Logger:
    def __init__(self, output=None):
        self.output = output

    def logging(self, message):
        if self.output:
            with open(self.output, "w") as f:
                print(message, file=f)
        else:
            print(message)
