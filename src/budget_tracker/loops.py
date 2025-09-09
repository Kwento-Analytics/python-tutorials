import marimo

__generated_with = "0.15.2"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _():
    import marimo as mo
    from conditional_statements import app
    return app, mo


@app.cell(hide_code=True)
async def _(app):
    # Execute the conditional_statements notebook; app.embed() can't be called in the cell that imported it!
    result_conditional_statements = await app.embed()
    return (result_conditional_statements,)


@app.cell(hide_code=True)
def _(result_conditional_statements):
    list_of_entries = result_conditional_statements.defs["list_of_entries"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Loops in Python

    Loops allow you to run a block of code **multiple times** until a condition is met. In Python, the two main types are:

    - **`for` loops** → iterate over a sequence  
    - **`while` loops** → repeat until a condition is false  

    ---

    ## 🔁 `for` Loops

    `for` loops are used to **iterate over sequences** (lists, tuples, strings, dictionaries, ranges).

    ### 1. Example with a List
    ```python
    categories = ["miscellaneous", "fast food", "utilities"]

    for category in categories:
        print(category)
    ```

    Output:
    ```
    miscellaneous
    fast food
    utilities
    ```

    ### 2. Example with a String
    ```python
    for letter in "Label":
        print(letter)
    ```

    Output:
    ```
    L
    a
    b
    e
    l
    ```

    ### 3. Using `range()`
    The `range()` function generates numbers.
    It's often used in `for` loops.

    ```python
    for i in range(5):
        print(i)
    ```

    Output:
    ```
    0
    1
    2
    3
    4
    ```

    👉 `range(start, stop, step)`

    `start` → beginning (default 0)

    `stop` → end (exclusive)

    `step` → increment (default 1)

    Example:
    ```python
    for i in range(2, 10, 2):
        print(i)
    ```

    Output: `2 4 6 8`

    ### 4. Iterating Over a Dictionary
    To iterate over the keys in a dictionary:

    ```python
    entry = {"Type": "Income", "Amount": 3050.21}

    for key in entry:
        print(key, ":", entry[key])
    ```

    Output:
    ```
    Type: Income
    Amount: 3050.21
    ```

    It is also possible to iterate through both the keys and values of a dictionary:

    ```python
    entry = {"Type": "Income", "Amount": 3050.21}

    for key, value in entry:
        print(key, ":", value)
    ```

    Output:
    ```
    Type: Income
    Amount: 3050.21
    ```

    ## 🔄 while Loops
    A while loop runs as long as a condition is true.

    ### Example

    ```python
    count = 0

    while count < 5:
        print("Count is:", count)
        count += 1
    ```

    Output:
    ```
    Count is: 0
    Count is: 1
    Count is: 2
    Count is: 3
    Count is: 4
    ```

    ### ⚠️ Beware of Infinite Loops
    If the condition never becomes false, the loop will run forever.

    ```python
    # This will run forever!
    while True:
        print("Press Ctrl+C to stop")
    ```
    **Always make sure your loop changes a variable or has a way to break.**

    ## 🟦 Controlling Loops
    - `break` → exit the loop early
    - `continue` → skip the rest of the current iteration and go to the next

    ### Example with `break`

    ```python
    for i in range(10):
        if i == 5:
            break
        print(i)
    ```

    Output: `0 1 2 3 4`

    ### Example with `continue`

    ```python
    for i in range(5):
        if i == 2:
            continue
        print(i)
    ```

    Output: `0 1 3 4`

    ## 🔂 Nested Loops
    You can put one loop inside another.

    ```python
    for i in range(3):
        for j in range(2):
            print(f"i={i}, j={j}")
    ```

    Output:
    ```
    i=0, j=0
    i=0, j=1
    i=1, j=0
    i=1, j=1
    i=2, j=0
    i=2, j=1
    ```

    ## ✅ Summary
    - Use `for` loops to iterate over sequences.
    - Use `while` loops to repeat while a condition is true.
    - Use `break` and `continue` to control the flow.
    - Be careful with infinite loops when using `while`.
    - Loops can be nested for complex iterations.
    """
    )
    return


@app.cell(column=1)
def _():
    """
        1. Loop through "list_of_entries" and print out the "Label" from each dictionary entry. 
        2. Loop through "list_of_entries" and sum up the total amount of "Expense" and "Income" types. 

        A good way to do #2 is to create two unique variables: one for the total sum of expenses and one for the income.
        Set them both equal to zero, then add the expense or income amount to each variable as you loop through each entry.
    """

    # Lopp through "list_of_entries" and print out the "Label" from each entry


    # Loop through "list_of_entries" and print out the total amount for expenses and income separately

    return


if __name__ == "__main__":
    app.run()
