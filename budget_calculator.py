Budget=float(input("please enter your budget for this month: "))

totalExpenses=0

moreExpenses='y'

while (moreExpenses == 'y'):
    Expense=float(input("\nEnter an expense: "))
    totalExpenses=totalExpenses+Expense
    moreExpenses= input("\nDo u have more expenses? type y for yes n for no: ")

print()

while (moreExpenses == 'n'):
    if totalExpenses>Budget:
        print("\nYou were over your budget of Rs.", Budget, "by Rs.", totalExpenses-Budget)

    elif Budget>totalExpenses:
        print("\nYou were under your budget of Rs.", userBudget, "by Rs.", Budget-totalExpenses)

    else:
        print("\nYou used your budget of Rs.", Budget, ".")
    break
print()
