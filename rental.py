# ROI Calculator 
# Gives a return of investment
Investment = 60000  # (Capital Cost of the Building)
Rent = 1250
Loss = 1000 # (Electricty, Repairs, Water, etc)

def ROI(Investment, Rent, Loss):
    NetProfit = Rent *12 - Loss
    ROI = (NetProfit/Investment)*100
    print(ROI)

ROI(Investment, Rent, Loss)



# Expense Calculator

def main(): 
    endProgram = 'no'
    integerchoice = 0
    totalBudget = 4000
    while endProgram == 'no':
        print
        print ('Welcome to the Personal Budget Program')
        print ('Menu Selection:')
        print ('1- Add an Expense:')
        print ('2- Remove an Expense:')
        print ('3- Add Revenue:')
        print ('4- Remove Revenue')
        print ('5- Check Budget Balance')
        print ('6- Exit')
        print
        choice= int(input('Enter your selection: '))
        if choice == 1:
            totalBudget = addExpense (totalBudget)
        elif choice == 2:
            totalBudget = removeExpense (totalBudget)
        elif choice == 3:
            totalBudget = addRevenue (totalBudget)
        elif choice == 4:
            totalBudget = removeRevenue (totalBudget)
        elif choice == 5: 
            print ('Your balance is ', totalBudget)
        elif choice == 6:
            endProgram = 'yes'
            print ('Thank you for using this budget program, Goodbye')
        elif choice > 6:
            print ('Invalid Selection, try again')

def addExpense(totalBudget):
    expense = input ('Enter your expense amount: $')
    monthly = input ('How many times per month: ')
    totalExpense = expense * monthly
    totalBudget= totalBudget - totalExpense
    if totalExpense >= totalBudget:
        print ('The expenses was rejected because the budget exceeded.'),totalBudget
        totalBudget >= totalExpense  
    else:
        print ('The expenses was accepted, your remaining budget is: $'),totalBudget
    choice=int(input('enter your selection: '))
    return totalBudget
     
 
def removeExpense (totalBudget):
    expense = input ('Enter expense amount you want to remove: $')
    monthly = input ('How many times per month: ')
    totalExpense = expense * monthly
    totalBudget=totalExpense+totalBudget
    print('your remaining budget is: $%.2f' )%totalBudget
    return totalBudget
 
def addRevenue (totalBudget):
    revenue = input ('Enter new monthly income: $')
    totalBudget = totalBudget+revenue
    print ('your new budget is: $%.2f') %totalBudget
    return totalBudget 
 
def removeRevenue (totalBudget):
    revenue = input ('Enter monthly income amount to be removed: $')
    totalBudget = totalBudget - revenue
    if revenue >=totalBudget:
        print ('You owe :$%.2f')  %totalBudget
    else:
            print ('Your new budget is: $%.2f') %totalBudget
    return totalBudget
    
main()

    
