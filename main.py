import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# How many times symbol occurs
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# How much value multiplies
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winngs = 0
    winng_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winngs += values[symbol] * bet
            winng_lines.append(line + 1)
    
    return winngs, winng_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns


def print_slot_machine(columns):
    for row in range(ROWS):
        for i, column in enumerate(columns):
            print(column[row], end=" | " if i != len(columns) - 1 else "")
        print()


def deposit():
    while True:
        amount = input("How much $ would you like to deposit?\n$")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amont must be grater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on.\n(1-{MAX_LINES})")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        bet = input("How much $ would you like to bet on each line?\n$")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amont must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Your total bet was ${total_bet} and your current balance is ${balance}. You do not have enough $.")
        else:
            break
   
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${bet * lines}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print(f"You won ${winnings}.")
    if winnings:
        print("You won on lines:", *winning_lines)
    
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press 'enter' to play, 'q' to quit.")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")



main()