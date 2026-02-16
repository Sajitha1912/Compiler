symbol_types = {}

def semantic_analysis(tokens):
    print("\nSEMANTIC ANALYSIS:")

    i = 0
    while i < len(tokens):

        # Variable Declaration
        if tokens[i][0] == "KEYWORD":
            var_type = tokens[i][1]
            var_name = tokens[i+1][1]

            if var_name in symbol_types:
                print(f"Error: Variable '{var_name}' already declared")
                return False
            else:
                symbol_types[var_name] = var_type
                print(f"Declared {var_name} as {var_type}")

            i += 5

        # Assignment Check
        elif tokens[i][0] == "IDENTIFIER":
            var_name = tokens[i][1]

            if var_name not in symbol_types:
                print(f"Error: Variable '{var_name}' not declared")
                return False

            print(f"Assignment to declared variable '{var_name}'")
            i += 6
        else:
            i += 1

    print("Semantic Analysis Successful ✅")
    return True
