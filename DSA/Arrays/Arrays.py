"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this

"""

expense = [
    ["January", 2200],
    ["February", 2350],
    ["March", 2600],
    ["April", 2130],
    ["May", 2190],
]

# 1. In Feb, how many dollars you spent extra compare to January?
diffInFeb = expense[1][1] - expense[0][1]
print("Extra dollars spend in February is :", diffInFeb)

# 2. Find out your total expense in first quarter (first three months) of the year.
quarterExpense = expense[0][1] + expense[1][1] + expense[2][1]
print("Expense of 3 months is: ", quarterExpense)

#3. Find out if you spent exactly 2000 dollars in any month
print("Have i spent 2000$?", 2000 in expense)

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense.append(["June", 1980])
print(expense)

#5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

aprilRefund = expense[3][1] - 200
expense[3][1] -= 200
print(expense)