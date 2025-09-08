import marimo

__generated_with = "0.15.2"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _():
    import marimo as mo
    from data_types import app
    return app, mo


@app.cell(hide_code=True)
async def _(app):
    # Execute the data_types notebook; app.embed() can't be called in the cell that imported it!
    result = await app.embed()

    # Bring in "list_of_entries from the data_types.py notebook"
    list_of_entries = result.defs["list_of_entries"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Conditional Statements in Python

    Conditional statements allow your program to **make decisions**.  
    They check whether a condition is `True` or `False`, and run code accordingly.

    ---

    ## 🟢 The `if` Statement
    The simplest conditional is `if`.  
    If the condition is true, the indented code block runs.

    ```python
    amount = 2500.29

    if amount >= 2000.0:
        print("You are making quite a bit of money!")
    ```

    ## 🟡 The if...else Statement
    Use `else` to run a block of code when the condition is not true.

    ```python
    amount = 2500.29

    if amount >= 2000.0:
        print("You are making quite a bit of money!")
    else:
        print("You are making enough money.")
    ```

    ## 🔵 The if...elif...else Chain
    Use `elif` (“else if”) to check multiple conditions in sequence.

    ```python
    amount = 2500.29

    if amount >= 2000.0:
        print("You are making quite a bit of money!")
    elif amount >= 1000.0:
        print("You are making enough money.")
    elif amount >= 500.0:
        print("It's time to get a promotion.")
    elif amount > 0.0:
        print("It's time to find a new job")
    else:
        print("You should get a job.")
    ```

    ## 🔍 Comparison Operators
    Conditions usually compare values. Common operators:

    | Operator   | Meaning                  | Example     |
    |:-----------|:------------------------:|------------:|
    | ==         | Equal to                 | x == 5      |
    | !=         | Not equal to             | x != 5      |
    | >          | Greater than             | x > 5       |
    | <          | Less than                | x < 5       |
    | >=         | Greater than or equal to | x >= 5      |
    | <=         | Less than or equal to    | x <= 5      |

    ## 🔗 Logical Operators
    You can combine conditions using `and`, `or`, and `not`:

    ```python
    amount = 500.0
    category = "Restaurant"

    if amount >= 200.0 and category == "Restaurant":
        print("Did you happen to go to a Michelin star restaurant?")
    ```

    ```python
    label = "Baja Cafe"

    if label == "La Frida" or label == "Baja Cafe":
        print("La Frida and Baja Cafe are some of my favorite restaurants!")
    ```

    ```python
    overbudget = False

    if not overbudget:
        print("Good job on not going overbudget!")
    ```

    ## 🔎 The in Operator
    The in operator checks if a value is present in a sequence (list, tuple, set, string)
    or as a key in a dictionary.

    ### 1. In Lists
    ```python
    categories = ["fast food", "utilities", "miscellaneous"]

    if "fast food" in categories:
        print("Fast food is a category!")
    ```

    ### 2. In Strings
    ```python
    text = "Have you had a chance to eat at La Frida?"

    if "La Frida" in text:
        print("La Frida is soooo good!")
    ```

    ### 3. In Dictionaries
    When used with dictionaries, in checks keys, not values:
    ```python
    entry = {"Type": "Expense", "Amount": 25.40, "Label": "Chick-fil-a"}

    if "Amount" in entry:
        print("Key 'Amount' exists in the dictionary.")

    if "Expense" in entry:
        print("This will NOT run, because 'Expense' is a value, not a key.")
    ```

    ✅ To check values in a dictionary:
    ```python
    if "Chick-fil-a" in entry.values():
        print("Found Chick-fil-a as a value!")

    ```

    ### 4. With `not in`
    You can combine with `not` to check absence:
    ```python
    categories = ["utilities", "restaurants", "fast food"]

    if "subscriptions" not in categories:
        print("Subscriptions is not a category.")
    ```

    ## 🧭 Nested Conditionals
    You can place conditionals inside other conditionals:

    ```python
    amount = 50.0
    label = "McDonald's"

    if amount >= 25.0:
        if label == "McDonald's":
            print("McDonald's is way too expensive.")
        else:
            print("Where did you spend $50?")
    ```

    ## ✅ Summary
    - Use `if` to check a condition.
    - Use `else` to handle the opposite case.
    - Use `elif` to check multiple conditions.
    - Conditions rely on **comparison**, **logical**, and **membership** (`in`) operators.
    - You can **nest** conditionals for more complex logic.
    """
    )
    return


@app.cell(column=1)
def _():
    """
        Check if "list_of_entries" is empty. If so, then print out a message saying that the list is empty.
        If the list is NOT empty, then assign the first item in the list to a new variable called "first_entry".
        Then, create an if...elif...else chain that does the following checks:
            1. if the keys of first_entry include "Category", then print out a message that says that the "Category" key was found
            2. else if the keys of first_entry include "Account", then print out the message that says that the "Account" key was found
            3. else, then print out a message that says that neither the "Category" nor "Account" keys were found

        Here's some pseudocode to help:

        if list_of_entries is empty:
            print message that says the list is empty
        else:
            assign the first element of list_of_entries to first_entry
            if "Category" is in the keys of first_entry:
                print message that says "Category" was found
            elif "Account" is in the keys of first_entry:
                print message that says "Account" was found
            else:
                print message that says neither keys were found

        NOTE: To check if a list is empty, you can check the length of a list:
        print(len(list_of_entries)) # This will show you the number of elements in that list. If it's zero, then it means the list is empty.
    """

    return


if __name__ == "__main__":
    app.run()
