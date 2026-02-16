def optimize(tokens):
    print("\nOPTIMIZATION:")

    optimized = []
    i = 0

    while i < len(tokens):
        # Constant Folding
        if (i+5 < len(tokens) and
            tokens[i][0] == "IDENTIFIER" and
            tokens[i+1][1] == "=" and
            tokens[i+2][0] == "NUMBER" and
            tokens[i+3][1] in ["+", "-", "*", "/"] and
            tokens[i+4][0] == "NUMBER"):

            num1 = int(tokens[i+2][1])
            op = tokens[i+3][1]
            num2 = int(tokens[i+4][1])

            result = eval(f"{num1}{op}{num2}")

            print(f"Optimized: {num1} {op} {num2} → {result}")

            optimized.extend([
                tokens[i],
                tokens[i+1],
                ("NUMBER", str(result)),
                tokens[i+5]
            ])
            i += 6
        else:
            optimized.append(tokens[i])
            i += 1

    return optimized
