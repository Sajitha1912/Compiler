symbol_table = set()

def insert_symbol(name):
    symbol_table.add(name)

def display_symbol_table():
    print("\nSYMBOL TABLE:")
    for i, symbol in enumerate(symbol_table, start=1):
        print(f"{i}. {symbol}")
