# lexer.py
from tokens import Token

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def get_next_token(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

        if self.pos >= len(self.text):
            return None

        if self.text[self.pos].isdigit():
            token = self.get_number()
            return token

        if self.text[self.pos] == '+':
            self.pos += 1
            return Token('PLUS', '+')

        if self.text[self.pos] == '-':
            self.pos += 1
            return Token('MINUS', '-')

        if self.text[self.pos] == '*':
            self.pos += 1
            return Token('TIMES', '*')

        if self.text[self.pos] == '/':
            self.pos += 1
            return Token('DIVIDE', '/')

        if self.text[self.pos] == '(':
            self.pos += 1
            return Token('LPAREN', '(')

        if self.text[self.pos] == ')':
            self.pos += 1
            return Token('RPAREN', ')')

        raise Exception('Invalid character: ' + self.text[self.pos])

    def get_number(self):
        num = ''
        while self.pos < len(self.text) and self.text[self.pos].isdigit():
            num += self.text[self.pos]
            self.pos += 1
        return Token('NUMBER', num)

    def tokenize(self):
        tokens = []
        while True:
            token = self.get_next_token()
            if token is None:
                break
            tokens.append(token)
        return tokens
