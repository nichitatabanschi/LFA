# main.py
from lexer import Lexer

text = "3 + 4 * ( 2 - 1 )"
lexer = Lexer(text)
tokens = lexer.tokenize()
print(tokens)
