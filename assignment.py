# Importing our modules
import uuid
from datetime import datetime, timezone

# The function initializes all our attributes in our class Expense and uses the datetime module to get time in utc
class Expense:
    def __init__(self, title, amount):
        self.title = title
        self.amount = amount
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

# The function allows us to be able to update or change the title and amount of an expense 
# and returns the time it was changed 
    def update(self, title=None, amount=None):
        if title != None:
            self.title = title
        if amount != None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)
        print(f"{id, title} has been updated successfully")

# .isoformat() converts a datetime object to a string representation
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(), 
            'updated_at': self.updated_at.isoformat()
        }

# The method below returns the string representation of an Object 
    def __repr__(self):
        return f"id {self.id}"

# This initalizes the attribute in our ExpenseDatabase class, creates an empty list
class ExpenseDatabase:
    def __init__(self):
        self.expenses = []
    
# The method adds expense to out Expense Database and displays what the database looks like after each addition
    def add_expense(self, expense):
        self.expenses.append(expense)
        print(f"{expense} has been added successfully!")
        print("Database after adding expense:")
        return expense.id
    
# This method removes an expense from our database with using the unique identifier in expense_id
    def remove_expense(self, expense_id):
        self.expenses = [x for x in self.expenses if x.id != expense_id]
        print(f"Financial expense with id {expense_id} has been removed")
    
# This returns an expense using its unique id and returns None when it is not found
    def get_expense_by_id(self, expense_id):
        for x in self.expenses:
            if x.id == expense_id:
               return x
        return None

# This method fetches our expense by its title and put them in a list called titles
    def get_expense_by_title(self, expense_title):
        titles = []
        for x in self.expenses:
            if x.title == expense_title:
                titles.append(x)
        return titles if titles else None
        
# This to_dict method creates a dictionary representation of our expenses database
    def to_dict(self):
        return {
        'expenses': [
            {
                'id': x.title,
                'title': x.title,
                'amount': x.amount,
                'created_at': x.created_at.isoformat(),
                'updated_at': x.updated_at.isoformat()
            }
            for x in self.expenses
        ]
    }