#(total = total + new_expense)

#Create a script where users enter an expense amount (e.g., 100, 50, 20). The program adds them up and displays the Total Spent.
total = 0

expense_1 = float(input("Enter expense 1: "))
total = total + expense_1

expense_2 = float(input("Enter expense 2: "))
total = total + expense_2

expense_3 = float(input("Enter expense 3: "))
total = total + expense_3

print("Total Spent:", total)