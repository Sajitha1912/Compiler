from lexer import lexical_analysis
from parser import syntax_check
from semantic import semantic_analysis
from optimizer import optimize
from codegen import generate_code
from symbol_table import display_symbol_table

def main():
    with open("input.txt", "r") as file:
        code = file.read()

    print("LEXICAL ANALYSIS:\n")
    tokens = lexical_analysis(code)

    syntax_check(tokens)

    if semantic_analysis(tokens):
        optimized_tokens = optimize(tokens)
        generate_code(optimized_tokens)

    display_symbol_table()

if __name__ == "__main__":
    main()
