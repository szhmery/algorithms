class ShortInputException(Exception):
    def __init__(self, length, min_length):
        super().__init__()
        self.length = length
        self.min_length = min_length

    def __str__(self):
        return 'The length of your input:{}, minimum length:{}'.format(self.length, self.min_length)


try:
    content = input("Please input:")
    if len(content) < 5:
        raise ShortInputException(len(content), 5)
except ShortInputException as e:
    print(e)
