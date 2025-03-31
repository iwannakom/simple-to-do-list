class Expsense:
    def _init_(self,date,description,amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpsenseTracker:
    def _init_(self):
        self.expenses = []

    def add_expense(self,expense):
        self.expenses.append(expense)

    def remove_expsense(self,expense):
        if 0<= index <len(self.expenses):
            del self.expenses[index] 
            print("exosense removes succesfully")
        
        else:
            print('invalid expense index')

    def view_expenses(self):
        if len (self.expenses) ==0:
            print('no expsenses found')

        else:
            print('EXPENSE LIST:')
            for i, expsense in enumerate(self.expsenses, start =1):
                print (f"{i}. date: {expense.date}, description {expense.description}")

    def total_expsenses(self):
        total = sum(expense.amount for expense in self.expsenses)
        print(f'Total expenses: {total:.2f}')

    def main():
        tracker = ExpsenseTracker()

        while True:
            print ('/n Expense Tracker Menu:')
            print (' 1. add expense')
            print ('2. remove expense')
            print ('3. view expenses')
            print ('4. total expenses')
            print ('5. exit')

            choice  =  input ('enter your choice(1-5):')
            if choice == "1":
                date =  input ('enter the date of your expense (yyyy/mm/dd)')
                description = input ('enter your description :')
                amount = float(input('enter the amount :'))
                expense = expense(date,description,amount )
                tracker.add_expense(expense)
                print ('expense added succesfully')

            elif choice == '2':
                index = int(input('enter the expense index to remove:')) -1
                tracker.remove_expense(index)
            
            elif choice == '3':
                tracker.view_expsenses()

            elif choice =='4':
                tracker.total_expsenses()

            elif choice =='5':
                print('goodbye')
                break 

            else:
                print('invalid choice please try again with a valid number')

    if __name__=='_main_':
        main()
        



