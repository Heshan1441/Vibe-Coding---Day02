# Simple Budget Tracker

"""A small script that asks for a monthly budget and three expenses,
then computes and displays the remaining balance.
"""

def main():
    try:
        total = float(input("Enter your total monthly budget: "))
    except ValueError:
        print("Please enter a valid number for the budget.")
        return

    expenses = []
    count = 1
    while True:
        entry = input(f"Enter expense #{count} (or type 'done' to finish): ")
        if entry.strip().lower() == 'done':
            break
        try:
            amt = float(entry)
        except ValueError:
            print("Invalid amount; please enter a number or 'done'.")
            continue
        expenses.append(amt)
        count += 1

    remaining = total - sum(expenses)
    print(f"\nTotal budget : {total:.2f}")
    print(f"Expenses      : {', '.join(f'{e:.2f}' for e in expenses)}")
    print(f"Remaining bal.: {remaining:.2f}")

    # warn if low funds
    if remaining < 500:
        print("Warning: Low Funds")


if __name__ == "__main__":
    main()
