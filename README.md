## Introduction
Hello, Welcome to my Data Engineering Project Assessement for first semester at Altschool. The goal of this assignment is to assess our understanding of object-oriented programming (OOP) concepts in Python. I was tasked with implementing two classes, Expense and ExpenseDatabase to model and manage financial expenses.

Classes Overview:
### Expense Class: Represents an individual financial expense.
- Attributes:
1. id: A unique identifier generated as a UUID string.
2. title: A string representing the title of the expense.
3. amount: A float representing the amount of the expense.
4. created_at: A timestamp indicating when the expense was created (UTC).
5. updated_at: A timestamp indicating the last time the expense was updated (UTC).

- Methods:
1. `__init__`: Initializes the attributes.
2. update: Allows updating the title and/or amount, updating the updated_at timestamp.
3. to_dict: Returns a dictionary representation of the expense.

### ExpenseDB class: Manages a collection of Expense objects.
- Attributes:
1. expenses: A list storing Expense instances.
- Methods:
1. `__init__`: Initializes the list.
2. add_expense: Adds an expense.
3. remove_expense: Removes an expense.
4. get_expense_by_id: Retrieves an expense by ID.
5. get_expense_by_title: Retrieves expenses by title.
6. to_dict: Returns a list of dictionaries representing expenses.

#### Instructions
We were told that for the Expense class:
1. Implement an `__init__` method to initialize the attributes.
2. Implement an update method that allows updating the title and/or amount of the
expense. The updated_at attribute should be automatically set to the current UTC
timestamp whenever an update occurs.
3. Implement a to_dict method that returns a dictionary representation of the expense.

- For the Expense Database class we were told to:
1. Implement an `__init__` method to initialize the expenses list.
2. Implement methods to:
a. Add an expense to the database.
b. Remove an expense from the database.
c. Get an expense by ID.
d. Get expenses by title (returning a list).
3. Create a to_dict method that returns a list of dictionaries representing each expense in
the database.
Github
- Explains how to clone iT

## How to Clone the Repository
Copy the repository's url and open your terminal, cd into where you would like to initialize git and then run `git init`. Once git is initialized then you can run this command `git clone https://github.com/PreciousIbe/Altschool_DE_exam_project.git`.

## To run the Code- 
Once the file has been cloned successfully you can then run python3 name_of_file.py either on the terminal or on your IDE eg- VsCode to test the code.