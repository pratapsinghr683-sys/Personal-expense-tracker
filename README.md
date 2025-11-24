
 Simple Expense Tracker
 Hey! So this is a little command-line app I built to help track expenses. It's got emojis, it's friendly, and honestly
 it just makes keeping track of your money a bit less boring.
 What does it do?
 Pretty straightforward stuff:
 Add expenses when you buy things
 Look at everything you've spent money on
 See the total (prepare yourself emotionally first)
 Filter by category so you can see exactly how much you're spending on coffee
 Delete expenses if you added something by mistake
 Has a nice menu with emojis because why not
 Getting it running
 You just need Python 3 installed. That's it. No fancy libraries or complicated setup.
 Download the file and run it:
 bash
 python 
python "Simple Expense Tracker.py"
 "Simple Expense Tracker.py"
 How it works
 When you start it up, you'll see a menu with 6 options. Just type the number for what you want to do:
 Adding an expense is easy - it'll ask you what you bought, how much it cost, and what category it falls under.
 The app will make sure you enter a real number (I learned the hard way that validation is important).
 Viewing expenses shows you everything in a nice table with IDs, so you can keep track of stuff.
 The total gives you the damage, plus some commentary depending on how much you've spent. Under $100?
 You're doing great. Over $500? Maybe slow down a bit.
 Filtering lets you see spending by category - really useful when you want to know if you're spending too much
 on takeout (spoiler: you probably are).
 Deleting removes expenses by their ID number. Useful for fixing mistakes.
 Categories you can use
 food
transport
 entertainment
 bills
 other
 Pretty self-explanatory. Type them in lowercase when adding expenses.
 Quick example
 What would you like to do? (1-6): 1
 What would you like to do? (1-6): 1
 💸
 Let's add a new expense!
 What did you spend on? Coffee
 💸
 Let's add a new expense!
 What did you spend on? Coffee
 How much did it cost? $4.50
 How much did it cost? $4.50
 Category: food
 Category: food
 ✅
 Got it! Expense added (ID: 1)
 💭
 'Coffee' for $4.50 - every penny counts!
 ✅
 Got it! Expense added (ID: 1)
 💭
 'Coffee' for $4.50 - every penny counts!
 Important stuff to know
 The expenses only live in memory while the program is running. Close it, and they're gone. I know, I know - I
 should add a way to save things. That's on the todo list.
 Also, you can type any category name you want, but the app suggests the main five to keep things organized.
 Things I might add later
 If I get around to it (or if you want to add them yourself):
 Actually saving data so it doesn't disappear
 Export to CSV or something
 Dates and timestamps
 Budget warnings
 Maybe some graphs if I'm feeling ambitious
 That's it
 This was a fun little project to practice Python basics - functions, lists, input validation, all that good stuff. Feel
 free to use it, modify it, break it, whatever you want.
 The whole point is just to make expense tracking less of a chore. Hope it helps!
Made with Python and too much coffee 
☕
