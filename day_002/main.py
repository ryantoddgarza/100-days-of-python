#~/usr/bin/env python3
"""Split bill with tip amount between `n` number of people."""

bill_amount = float(input("What is the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? "))
n_people = int(input("How many people are splitting the bill? "))

tip_amount = bill_amount * (tip_percent / 100)
due = (bill_amount + tip_amount) / n_people
due_formatted = "{:.2f}".format(due)
message = f"Each person owes ${due_formatted}"

print(message)
