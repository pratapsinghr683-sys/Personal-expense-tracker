def display_menu():
    print("\n💰 ===== YOUR EXPENSE TRACKER ===== 💰")
    print("1. 💸 Add a new expense")
    print("2. 📋 See all my expenses")
    print("3. 🧮 Show me the total damage")
    print("4. 🔍 Filter by category")
    print("5. 🗑️  Delete an expense")
    print("6. 👋 Exit")
    print("====================================")

def add_expense(expenses):
    print("\n💸 Let's add a new expense!")
    description = input("What did you spend on? ")
    
    while True:
        amount_str = input("How much did it cost? $")
        valid = True
        dot_count = 0
        for char in amount_str:
            if char == '.':
                dot_count += 1
            elif char < '0' or char > '9':
                valid = False
                break
        
        if valid and dot_count <= 1 and len(amount_str) > 0:
            amount = float(amount_str)
            if amount > 0:
                break
        
        print("Oops! That doesn't look right. Please enter a valid amount (like 25.50)")
    
    category = input("Category (food/transport/entertainment/bills/other): ").lower()
    
    expense = {
        'id': len(expenses) + 1,
        'description': description,
        'amount': amount,
        'category': category
    }
    
    expenses.append(expense)
    print(f"\n✅ Got it! Expense added (ID: {expense['id']})")
    print(f"💭 '{description}' for ${amount:.2f} - every penny counts!")

def view_expenses(expenses):
    if len(expenses) == 0:
        print("\n🎉 Good news! No expenses yet. Your wallet is safe... for now.")
        return
    
    print("\n📋 Here's what you've spent so far:")
    print(f"{'ID':<5} {'What you bought':<25} {'Cost':<12} {'Category':<15}")
    print("-" * 57)
    
    for expense in expenses:
        print(f"{expense['id']:<5} {expense['description']:<25} ${expense['amount']:<11.2f} {expense['category']:<15}")

def view_total(expenses):
    if len(expenses) == 0:
        print("\n🎉 No expenses yet! Your bank account thanks you.")
        return
    
    total = 0.0
    for expense in expenses:
        total += expense['amount']
    
    print(f"\n🧮 Total Money Spent: ${total:.2f}")
    
    if total < 100:
        print("💚 Not bad! You're keeping it under control.")
    elif total < 500:
        print("💛 That's a decent amount. Watch your budget!")
    else:
        print("💸 Whoa! Maybe time to slow down a bit?")

def view_by_category(expenses):
    if len(expenses) == 0:
        print("\n😊 No expenses to filter yet!")
        return
    
    category = input("\n🔍 Which category do you want to check? ").lower()
    
    found = False
    total = 0.0
    
    print(f"\n💳 Expenses for '{category}':")
    print(f"{'ID':<5} {'Description':<25} {'Amount':<12}")
    print("-" * 42)
    
    for expense in expenses:
        if expense['category'] == category:
            print(f"{expense['id']:<5} {expense['description']:<25} ${expense['amount']:<11.2f}")
            total += expense['amount']
            found = True
    
    if not found:
        print(f"😅 Nothing found in '{category}'. Lucky you!")
    else:
        print(f"\n💰 Total for '{category}': ${total:.2f}")

def delete_expense(expenses):
    if len(expenses) == 0:
        print("\n😊 Nothing to delete here! Clean slate.")
        return
    
    view_expenses(expenses)
    
    while True:
        id_str = input("\n🗑️  Which expense ID do you want to remove? (0 to go back): ")
        
        # Validate input is a number
        valid = True
        for char in id_str:
            if char < '0' or char > '9':
                valid = False
                break
        
        if valid and len(id_str) > 0:
            expense_id = int(id_str)
            
            if expense_id == 0:
                print("👌 Alright, keeping everything as is!")
                return
            
            found = False
            for i in range(len(expenses)):
                if expenses[i]['id'] == expense_id:
                    deleted = expenses[i]
                    new_expenses = []
                    for j in range(len(expenses)):
                        if j != i:
                            new_expenses.append(expenses[j])
                    
                    while len(expenses) > 0:
                        expenses.pop()
                    
                    for expense in new_expenses:
                        expenses.append(expense)
                    
                    print(f"\n✅ Deleted! '{deleted['description']}' is gone. More money for you! 🎉")
                    found = True
                    break
            
            if found:
                break
            else:
                print("🤔 Hmm, I can't find that ID. Try again?")
        else:
                            print("❌ That's not a valid number. Please try again!")

def main():
    expenses = []
    
    print("\n👋 Hey there! Welcome to your personal Expense Tracker!")
    print("💡 Let's keep track of where your money goes...")
    
    while True:
        display_menu()
        choice = input("\n🤔 What would you like to do? (1-6): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_total(expenses)
        elif choice == '4':
            view_by_category(expenses)
        elif choice == '5':
            delete_expense(expenses)
        elif choice == '6':
            print("\n💙 Thanks for using Expense Tracker!")
            print("💪 Remember: Tracking expenses is the first step to financial freedom!")
            print("👋 See you later!")
            break
        else:
            print("\n❌ Oops! Please pick a number between 1 and 6.")

if __name__ == "__main__":
    main()
