# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "uvicorn==0.35.0",
# ]
# ///

import marimo

__generated_with = "0.15.2"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # ⚙️ Python Basic Data Types and Variable Assignment

    In Python, variables are used to store data. You don’t need to declare a variable type explicitly; Python infers the type based on the value you assign.

    ## 1. Integers (`int`)
    Integers are whole numbers, positive or negative, without decimals.

    ```python
    year = 2025
    month = 9
    day = 6
    ```
    ## 2. Floating Point Numbers  (`float`)
    Floats represent numbers with decimal points.

    ```python
    expense = 52.99
    income = 2100.81
    ```
    💡 **Pro Tip:** Python will not let you use commas to represent large numbers. You can use underscores `_` to make large numbers readable.

    ## 3. Strings (`str`)
    Strings are sequences of characters enclosed in single (`'`) or double (`"`) quotes.

    ```python
    category = 'miscellaneous'
    description = 'bowling date'
    ```

    ## 4. Booleans (`bool`)
    Booleans represent truth values: `True` or `False`.

    ```python
    overbudget = True
    ```

    ## 5. Lists (`list`)
    Lists are ordered collections of items, which can be of mixed types. Lists are mutable (you can change their content).

    ```python
    expenses = [10.50, 204.39, 5.00, 120.32]
    name_and_price = ['volleyball', 60.50, 'paper', 10.99]
    ```

    ## 6. Dictionaries (`dict`)
    Dictionaries store data as key-value pairs.

    ```python
    expense = {
        "name": "Chick-fil-a",
        "cost": 14.76,
        "category": "Fast food",
        "overbudget": False
    }
    ```

    ## Summary
    - **int** ➡️ whole numbers
    - **float** ➡️ decimal numbers
    - **str** ➡️ text data
    - **bool** ➡️ True/False values
    - **list** ➡️ ordered, mutable collection
    - **dict** ➡️ key-value pairs
    """
    )
    return


@app.cell
def _():
    """
        Create a list of 6 elements: two integers, two strings, and two floats.
    """

    random_list = []
    return


@app.cell
def _():
    """
        Create a dictionary that has 4 key-value pairs. The keys should all be string types while the values
        should all be float types.
    """

    random_dictionary = {}
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(
        r"""
    # 📋 Lists

    In Python, you often need to **store and retrieve values** from lists. Lists use indexes to store and access elements in the list.

    ---

    ## Accessing Elements in Lists

    Lists are **ordered collections**. Each element has an **index** (a number starting at `0`).

    ### 1. Indexing
    Use square brackets `[]` with the position of the element:

    ```python
    categories = ["groceries", "restaurants", "utilities"]

    print(categories[0])  # "groceries" (first element)
    print(categories[1])  # "restaurants"
    print(categories[2])  # "utilities"
    ```
    ⚠️ If you try to access an index that doesn’t exist, Python raises an `IndexError`.

    ### 2. Negative Indexing
    Negative numbers count from the end of the list:

    ```python
    categories = ["groceries", "restaurants", "utilities"]

    print(categories[-1])  # "utilities" (last element)
    print(categories[-2])  # "restaurants"
    ```

    ### 3. Slicing
    Use `start:end` inside brackets to get a **range of elements**:

    ```python
    categories = ["groceries", "restaurants", "utilities", "subscriptions"]

    print(categories[1:3]) # ["restaurants", "utilities"] (from index 1 up to, but not including 3)
    print(categories[:2])  # ["groceries", "restaurants"] (from start up to, but not including index 2)
    print(categories[2:])  # ["utilities", "subscriptions"] (from index 2 to the end)
    ```

    ## ✅ Summary
    - Lists use **indexes (0, 1, 2, …)** to access elements.
    - **Negative indexes** count from the end of a list.
    - **Slicing** lets you grab ranges of list elements.
    """
    )
    return


@app.cell
def _():
    """
        Using the list that you created in the previous section (random_list), 

        1. Print out the 3rd element in the list.
        2. Print out the 2nd element all the way to the last element.
        3. Print out the last element.
    """

    # Print out the 3rd element in the list
    print()

    # Print out the 2nd all the way to the last element
    print()

    # Print out the last element
    print()
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(
        r"""
    # 📖 Dictionaries

    In Python, you often need to **store and retrieve values** from dictionaries.  
    Dictionaries use key-value pairs to store and retrieve values.

    ---

    ## Accessing Elements in Dictionaries
    Dictionaries are **unordered collections** of key-value pairs. You access elements by their keys, not positions.

    ### 1. Access by Key
    Use the key inside square brackets:

    ```python
    budget_entry = {
        "Type": "Income", 
        "Date": "9/7/2025", 
        "Label": "Kwento Analytics",
        "Amount": 2520.20,
        "Description": "Bi-weekly income from Kwento Analytics"}

    print(budget_entry["Type"]) # "Income"
    print(budget_entry["Amount"]) # 2520.20
    ```

    ⚠️ If the key doesn’t exist, Python raises a `KeyError`.

    ### 2. Using `.get()`
    Use the `.get()` method to safely access values:

    ```python
    budget_entry = {
        "Type": "Income", 
        "Date": "9/7/2025", 
        "Label": "Kwento Analytics",
        "Amount": 2520.20,
        "Description": "Bi-weekly income from Kwento Analytics"}

    print(budget_entry.get("Label")) # "Kwento Analytics"
    print(budget_entry.get("Category")) # None (no error if key is missing)
    print(budget_entry.get("Category", "N/A")) # "N/A" (default value if missing)
    ```

    ### 3. Accessing Keys and Values
    Dictionaries provide ways to access all keys, values, or both:

    ```python
    budget_entry = {
        "Type": "Income", 
        "Label": "Kwento Analytics",
        "Amount": 2520.20}

    print(budget_entry.keys()) # dict_keys(['Type', 'Label', 'Amount'])
    print(budget_entry.values()) # dict_values(['Income', 'Kwento Analytics', 2520.20])
    print(budget_entry.items) # dict_items([('Type', 'Income'), ('Label', 'Kwento Analytics'), ('Amount', 2520.20)])
    ```

    ## ✅ Summary
    - **Dictionaries** use **keys** (strings, numbers, etc.) instead of indexes.
    - Use `.get()` to avoid errors when accessing dictionary keys.
    """
    )
    return


@app.cell
def _():
    """
        Using the dictionary you created in the first section (random_dictionary),

        1. Print out the values associated with the following keys of the "second_entry" dictionary: "Date", "Label", "Amount" 
    """

    print() # Print the date 
    print() # Print the label
    print() # Print the amount
    return


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(
        r"""
    # 💪 CHALLENGE

    It's time to combine what you've learned in this section! In order to create a budgeting app, you need to store the income and expenses of the user. We will use both lists and dictionaries to do this. 

    ---

    ## Create a list of 4 dictionaries for a budget tracker with the following items:

    - "Type": "Expense" or "Income" (str)
    - "Date": "MM/DD/YYYY" (str)
    - "Label" (str)
    - "Amount" (float)
    - "Description" (str)

    ### Here's an example dictionary:

    `{"Type": "Income",`  
    `"Date": "9/7/2025",`  
    `"Label": "Kwento Analytics",`  
    `"Amount": 2520.20,`  
    `"Description": "Bi-weekly income from Kwento Analytics"}`
    """
    )
    return


@app.cell
def _():
    list_of_dictionaries = []

    # Displays the contents of the list "list_of_dictionaries"
    print(list_of_dictionaries)
    return


if __name__ == "__main__":
    app.run()
