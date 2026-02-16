def generate_code(tokens):
    print("\nINTERMEDIATE CODE GENERATION:")

    i = 0
    temp_count = 1

    while i < len(tokens):

        if tokens[i][0] == "IDENTIFIER":
            left = tokens[i][1]

            if tokens[i+3][1] in ["+", "-", "*", "/"]:
                op1 = tokens[i+2][1]
                operator = tokens[i+3][1]
                op2 = tokens[i+4][1]

                temp = f"t{temp_count}"
                print(f"{temp} = {op1} {operator} {op2}")
                print(f"{left} = {temp}")

                temp_count += 1
                i += 6
            else:
                i += 4
        else:
            i += 1
