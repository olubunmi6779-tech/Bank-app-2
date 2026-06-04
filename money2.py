# Bank App Part 2

credit = float(input("Enter credited amount: "))
debit = float(input("Enter debited amount: "))

balance = credit - debit

print("\n----- Bank Account Summary -----")
print("Credit Amount:", credit)
print("Debit Amount:", debit)
print("Balance:", balance)

if balance > 0:
    print("You have some money left in your account.")
elif balance == 0:
    print("Your account balance is zero.")
else:
    print("Warning!!!!!!! Expenses exceed income.")