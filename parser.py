def syntax_check(tokens):
    print("\nSYNTAX CHECKING:")

    i = 0
    while i < len(tokens):
        if tokens[i][0] == "KEYWORD":
            if (tokens[i+1][0] == "IDENTIFIER" and
                tokens[i+2][1] == "=" and
                tokens[i+3][0] in ["NUMBER", "IDENTIFIER"] and
                tokens[i+4][1] == ";"):
                print("Valid Declaration Statement")
                i += 5
            else:
                print("Syntax Error in Declaration")
                return
        elif tokens[i][0] == "IDENTIFIER":
            if (tokens[i+1][1] == "=" and
                tokens[i+2][0] in ["NUMBER", "IDENTIFIER"] and
                tokens[i+3][1] in ["+", "-", "*", "/"] and
                tokens[i+4][0] in ["NUMBER", "IDENTIFIER"] and
                tokens[i+5][1] == ";"):
                print("Valid Assignment Statement")
                i += 6
            else:
                print("Syntax Error in Assignment")
                return
        else:
            i += 1

    print("Program Parsed Successfully ✅")
