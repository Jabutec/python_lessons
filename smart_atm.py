
balance = 500

money = int(input("Enter the amount to withdraw: "))

if money <= balance:
    balance -= money
    print(f"Withdrawal successful. Your new balance is: {balance}")
elif money <= 0:
    print("Invalid amount.")
else:
    print("Declined, Insufficient funds.")