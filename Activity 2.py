Withdrawal_Amount=int(input("Enter the withdrawal amount: "))

Number_Of_50dollar_notes=(Withdrawal_Amount//50)
Number_of_10dollar_notes=(Withdrawal_Amount%50)//10
Number_of_5dollar_notes=((Withdrawal_Amount%50)%10)//5

print("Number of 50 dollar notes:", Number_Of_50dollar_notes)
print("Number of 10 dollar notes:", Number_of_10dollar_notes)
print("Number of 5 dollar notes:", Number_of_5dollar_notes)

