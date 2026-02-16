import re
from symbol_table import insert_symbol

KEYWORDS = {"int", "float", "char"}

def lexical_analysis(code):
    tokens = []
    token_pattern = r'\bint\b|\bfloat\b|\bchar\b|[a-zA-Z_]\w*|\d+|[=+\-*/;]'

    matches = re.findall(token_pattern, code)

    for match in matches:
        if match in KEYWORDS:
            print(f"KEYWORD: {match}")
            tokens.append(("KEYWORD", match))

        elif match.isdigit():
            print(f"NUMBER: {match}")
            tokens.append(("NUMBER", match))

        elif re.match(r'[a-zA-Z_]\w*', match):
            print(f"IDENTIFIER: {match}")
            insert_symbol(match)
            tokens.append(("IDENTIFIER", match))

        elif match in "=+-*/":
            print(f"OPERATOR: {match}")
            tokens.append(("OPERATOR", match))

        elif match == ";":
            print(f"SPECIAL SYMBOL: {match}")
            tokens.append(("SEMICOLON", match))

    return tokens
