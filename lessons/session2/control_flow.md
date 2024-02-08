# Flow control
We use flow control to do exactly what the name suggests - we want to control the flow of the programme. 

Note that if you're coming from an ```R``` background, some of this might seem a little bit unusual. Don't worry, it gets to be second nature!

## For loops
```python
    colours = ["red", "green", "blue"]
    # for each colour in the list called colours
    for colour in colours:
        print(colour)
```
### Increment decrement

In python we can use ```+=``` and ```-=``` to increment and decrement variables. This is useful if we want to count how many times we have gone through a loop.

```python
    # create variable
    i = 0
    i += 1
    print(i)
```
### Comprehensions

In the above example, we are just printing each entry in a list. But let's say we wanted to do something to each of those entries and save the modified values to a new list:
```python
    shouty_colours = []
    for colour in colours:
        upper_string = colour.upper()
        shouty_colours.append(upper_string)
    print(shouty_colours)
```
This can be made much more concise by using list comprehensions:
```python
    # one liners baby!
    shouty_colours = [colour.upper() for colour in colours]
```
### Enumerate()

```python
    for idx,i in enumerate(range(0,10)):
        print(f"Index:{idx}, Value:{i}")

    for idx,i in enumerate(range(0,10,2)):
        print(f"Index:{idx}, Value:{i}")
```
### while
```python
    i = 10
    while i >= 5:
        print(i)
        i -= 1
        print("still counting...")
        if i < 5:
            print("done!")
            break
```
### if, elif, else

In python we use ```if``` statements to check if a condition is true. If it is, we do something. If it isn't, we do something else. We can also use ```elif``` and ```else``` to do something else if the first condition is not met.

```python
    for i in range(0,20):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

    for colour in colours:
        if colour == "red":
            pass
        elif colour == "green":
            print("ugly colour!")
        else:
            print("whatever")
```
## Exception handling
We can use exception handling to catch errors and do something with them. This is useful if you are working with a large dataset and you want to skip over any errors and continue with the rest of the data.

https://docs.python.org/3/tutorial/errors.html
```python
    for colour in colours:
        try:
            print(colour//2)
        except:
            print("Wrong data type, ya jabrony!")

    for colour in colours:
        try:
            print(word)
        except NameError:
            print("No name, loser")
```

## Defining functions

A function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.


```python
    def hello():
        print("Hello, world!")

    def hello(name="Ross"):
        print(f"Hello, {name}!")

    def hello(name:str="Ross") -> str:
        print(f"Hello, {name}!")
```
## Return values
We can add return values using the following syntax:

```python
    def hello(name = "Ross", age= 31):
        return f"Hello, my name is {name}. I am {age} years old!"
```

## Type hints:
We can also provide type hints to make our code more readable. This is especially useful if you are working in a team and you want to make sure that everyone knows what type of data is being passed around.

```python
    def hello(name: str = "Ross", age: int = 31) -> str:
        return f"Hello, my name is {name}. I am {age} years old!"
```
Here the type hints state that `name` is a string, `age` is an integer and the function returns a string.

## Docstrings
Furthermore we can add a docstring to the function, that describes what the function does:

```python
def hello(name: str = "Ross", age: int = 31) -> str:
    """
    This function takes a name and an age and returns a string
    """
    return f"Hello, my name is {name}. I am {age} years old!"
```

## Importing packages
```python
    import os
    inpath = os.path.join("..", "data")
    folder = os.listdir(inpath)
```
### Task

Create a function which does the following:

Task 1

- Take the list of user_data

```python
user_data = [
    ["Ross", 31, 1.8],
    ["Rachel", 29, 1.6],
    ["Joey", 32, 1.9],
    ["Phoebe", 30, 1.7],
    ["Chandler", 33, 1.75],
    ["Monica", 28, 1.65]
]
```

- Go through each entry in the list
  - Add to dictionary
    - key = name : values = (age, height)

The expected output should be:
```python
{
    "Ross": (31, 1.8),
    "Rachel": (29, 1.6),
    "Joey": (32, 1.9),
    "Phoebe": (30, 1.7),
    "Chandler": (33, 1.75),
    "Monica": (28, 1.65)
}
```

Task 1.1

- Create a function that will do this for any similar list

Task 2 

- Take the list of bad_user_data

```python
bad_user_data = [
    ["Ross", 31, 1.8],
    ["Rachel", 29, 1.6],
    ["Joey", 32, 1.9],
    ["Phoebe", 30, 1.7],
    ["Chandler", 33, 1.75],
    ["Monica", 28, 1.65],
    [1, 2, 3],
    [30, 1.7],
    ["Janice", 33, 1.75],
    ["Richard", 28, 1.65]
]
```

- Go through each entry in the list
  - If first entry is not string:
    - Raise an error and continue
  - If first entry is a string
    - Add to dictionary
      - key = name : values = (age, height)

Task 2.1

- Create a function that will do this for any similar list e.g.:

```
bad_user_data = [
    ["Jim",  32, 1.65],
    ["Jimmy",  102, 1.55],
    [202],
]
```

What if you get a bad input like:

```
bad_user_data = [
    ["Jim"],
    ["Jimmy", 102, None],
    ["John", "102", "1.55"],
]
```

Can you write a function that will handle this? (optional)

Task 3 
- Go to the folder called "data"
- For each file in a sorted list
  - check it is a csv
  - print the index and the filename
  - create a dictionary where keys=index and values = filename
  - return the dictionary to a variable

### Solution
```python
    # just an example - notice use of type hints
    def parser(inpath:str) -> dict:
        """
        Takes an input filepath and returns a dict of filenames

        inpath:     The target filepath
        dictionary: A dict of {index:filename} pairs
        """
        # initialise empty dict
        dictionary = {}
        # get list of files in inpath folder
        folder = os.listdir(inpath)
        # get index and filename for each file
        for idx,file in enumerate(sorted(folder)):
            # if it is a csv file
            if file.endswith(".csv"):
                # print to display
                print(f"Working on {idx} called {file}")
                # update dictionary
                dictionary[idx] = file
            # if not csv, ignore
            else:
                pass
        return dictionary
```
