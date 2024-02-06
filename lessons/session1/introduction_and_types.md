# Introduction

## Defining variables

Python variables are assigned using the ```=``` sign:
```python
    # Note that snake_case is best practice
    new_variable = 4
    print(new_variable)
```
We can also assign strings to variable names:
```python
    # Note the need for consistent single and double quotation marks
    different_variable = "I'm a different variable!"
    print(different_variable)
```
Be careful with the sign you use to assign variables! There's a difference between ```=``` and ```==```:
```python
    # This will return an error
    wrong_variable == 4
```
The symbol ```==``` is used to make an assertion which can be either ```True``` or ```False```:
```python
    # Test an assertion using numbers - should be True
    2*2 == 4
    # Test a different assertion - this should return False
    2*2 == 5
```
These kind of assertion statements will be useful later on. For now, we continue with variables.

There are some restrictions around which characters you can and cannot use when defining variable names:
```
    Can use:
        - upper and lower case letters (A-Z,a-z)
        - digits (0-9)
        - underscores (_)

    Cannot use:
        - any other punctuation (-.,!? etc)
        - whitespaces( )
        - 'reserved words'
```
## Data types

Python works with a reasonably tightly defined set of ```types```. You are most likely to encounter the following types:
```
    - Text type (```str```)
    - Numeric types (```int```, ```float```, ```complex```)
    - Sequence types (```lists```, ```tuples```, ```ranges```)
    - Map types (```dict```)
    - Set types (```set```)
    - Boolean types (```bool```)
```
We can find out the type of a specific variable or object by using the ```type()``` function:
```python
    # type() is a different colour - a reserved word!
    type(new_variable)
    type(different_variable)
```
Different types are used for different purposes. Moreover, different types have different ```methods``` which can used on them. These are usually extremely useful, so it's worth looking at them in detail.

## String types

Let's start by testing something we know to be a valid string:
```python
    # Define a string variable
    test_string = "This is a string!"
    # Check type
    type(test_string)
    # Assert type
    type(test_string) == str
```
## String methods

### Indexing

In order to return the character at a specific point in a string, we follow the string variable name with ```[n]``` where n is the index of the specific character to be returned:
```python
    # Define a string variable
    text_snippet = "It was the best of times, it was the worst of times"
    # Return first character
    print(text_snippet[0])
```
Notice that Python uses 0-based indexing, rather than 1-based indexing used in ```R```. Think of Python indexing as referring to the distance from the starting point. So the first letter is ```[0]``` because it is the starting point; the second letter is +1 away from the starting point so it's ```[1]```; the third character is +2 away from the starting point, so ```[2]```. And so on.

### Slicing

Let's say we want to return the first 10 characters of a string. Remember that we have 0-based indexing, so we're starting at ```[0]```. So we can try the following:
```python
    # get first 10 characters...?
    target_string = "It was the"
    target_string == text_snippet[0:9]
```
Oops! Something has gone wrong! This is because the syntax of ```a[start:stop]``` means *go from the start index up to **but not including** the stop index*. In other words, slice from ```start``` to ```stop-1```. So the correct values are:
```python
    # Test correct indexing
    target_string == text_snippet[0:10]
```
Programming is hell! But some useful shortcuts might help:
```
    a[start:stop]  # items from start through to stop-1
    a[start:]      # items from start to the end of the object
    a[:stop]       # items from the start through to stop-1
    a[:]           # all items from start to end (i.e. a copy of a)
    a[-1]          # last entry in string
```
### Concatenating

Strings can be added to other string types. This is known as concatenation:
```python
    # concatenate two string
    print(text_snippet + ", it was an age of wisdom, it was an age of foolishness")
    # also valid
    text_snippet2 = ", it was an age of wisdom, it was an age of foolishness")
    print(text_snippet + text_snippet2)
```
Notice how the plus sign functions differently here from regular addition. This is known as operator overloading and I hate it.

Texts can also be multiplied!
```python
    # 'multiplying' text
    print(text_snippet * 4)
```
But not divided:
```python
    print(text_snippet / 4)
```
### Useful string methods

Strings have a couple of methods which are (sometimes) useful, particularly in the case of NLP.
```python
    # upper case
    print(text_snippet.upper())
    
    # lower case
    print(text_snippet.lower())
    
    # split on specific character - no character means whitespace
    print(text_snippet.split())

    # left strip
    print("    Hello!"[0])
    print("    Hello!".lstrip()[0])

    # right strip
    print("Hello!    "[-1])
    print("Hello!    ".rstrip()[-1])
```

### F strings

One final, extremely useful thing related to strings is the ```f-string``` or formatted string. This allows you to insert variables or even expressions into a string without explicitly evaluating them. For example:
```python
    # define name variable
    name = "Ross"
    print(f"My name is  {name}")

    # expressions in f-strings
    print(f"The sum 2+3 is equal to {2+3}")
```
These can be useful when used alongside other string processing methods, especially when printing information to output or creating filenames.
```python
    # input file name
    infile = "2021-12-01.raw_data.csv"
    date = infile.split(".")[0]
    outfile = f"{date}.processed_data.csv"
    print(outfile)

    # More concise; less readable?
    outfile_concise = f"{infile.split('.')[0]}.processed_data.csv"
    outfile == outfile_concise
```

### Exercise: Remember quotation marks!

Try running the following:

```python
outfile_concise = f"{infile.split(".")[0]}.processed_data.csv"
outfile == outfile_concise
```

You will note that it does not run. Can you explain why?

## Sequence types

Sequence types are some of the most useful of Python's fundamental data types. If you write a Python program without some kind of sequence type, you're probably doing it wrong.

### Lists

The simplest kind of sequence type is the ```list```. Lists are most commonly used to create a sequential collection of objects of the same type - a ```list``` of ```str``` for example. But in principle, a list can comprise any assortment of objects.
```python
    # same types
    colours = ["blue", "green", "red"]
    # different types - name, age, height
    user_data = ["mary", 42, 1.65]
    # lists can be embedded (yuck)
    big_list = [user_data, colours]
```
But be careful!
```python
    big_list == user_data + colours
    [user_data, colours] == [colours, user_data]
```
### Slicing, indexing, sorting

We can slice and index lists in exactly the same way as we did with strings:
```python
    # get first colour
    print(colours[0])
    # check type
    print(type(colours[0]))
    # get first character of first colour
    print(colours[0][0])
```
Sometimes, indexing like this is a little complex; sometimes we want to do something to every object in a list. We'll see a couple of ways that we can do that later.

We can also sort a lists alphabetically *or* numerically, assuming there are not mixed data types!
```python
    # sort colours
    print(sorted(colours))
    print(sorted(user_data))
```
### Appended, removing

We can easily add and remove new elements from a list:
```python
    # add new element
    colours.append("black")
    print(colours)
    # remove an item
    colours.remove("green")
```

Notice how append and remove modify the object in-place. That is to say, we don't assign a new variable - instead the ```list``` object is modified by the method called. This could have unpredictable effects!

Similarly, be careful with trying to assign lists to new variables:
```python
    # problem!
    new_list = colours
    # remove at item
    colours.remove("red")
    # new_list should now be different from colours...
    new_list == colours
```
Lists are incredibly simple but powerful data structures. Use them wisely! 

### Exercise

Find fifth word in a sentence. (Str->List, index list)

**Example**:
For instance the sentence "hello my name is kenneth" -> ["hello", "my", "name", "is", "kenneth"] -> "kenneth"

### Tuples

```Tuples``` are essentially identical to lists but with one important difference, namely that ```tuples``` are immutable. That is to say, they can't be modified when they've been created:
```python
    # create tuple
    colours = ("red", "green", "blue")
    # try to append
    colours.append("black")
    # try to remove
    colours.remove("red")
```
So ```tuples``` are identical to lists, in that they can store heterogeneous types of objects in a sequential manner.

Be careful if decide to sort a ```tuple```!
```python
    # check type of sorted tuple...
    colours = ("red", "green", "blue")
    print(type(sorted(colours)))
```
### Exercise

Create a tuple comprising the first, fifth and last word of the text_snippet

### Ranges

The last (perhaps simplest) kind of sequential type is the ```range``` type. This can be used to generate a range of numbers between a lower and upper limit: 
```python
    # print range
    print(range(0,10))
```
Notice how the range is not evaluated for the sake of efficiency. We can evaluate this by storing all of the values as a list:
```python
    # get range
    values = range(0,10)
    print(list(values))
```
Note that we can also define the step size for a range of values:
```python
    # increment in steps of 2
    values = range(0,10,2)
    print(list(values))
```
## Map types (dictionaries)

One of the most dramatically undervalued data types in the whole Python programming language is the ```dict``` or dictionary type. Dictionaries are constructed around combinations of {key:value} pairings. So unlike sequence types which are indexed by a range of numbers, ```dict``` objects are indexed by a specific *key*.
```python
    # dictionary of users
    users = {"mary" : 42, "john" : 31}
    # get value for Mary
    users["mary"]
    # add new user
    users["adam"] = 50
```
Pretty much anything can be a key except for sequence types. Values can be anything, including sequence types and even including other dictionaries.

### Exercise

Create a dict with the following key-value pairs - mary=(42,1.65), john=(50,1.8), adam=(32,1.83)
Print Adam's height
```python
    # using a different syntax
    new_users = dict(mary=(42,1.65), john=(50,1.8), adam=(32,1.83))
    print(new_users)
    # get adam's age
    print(f"Adam is {new_users["adam"][0]} years old")
```

## Numeric types

There are a few numeric types which are likely to be of use. These are ```int```, ```float```, and ```complex```.

### Int and Floats

The fundamental difference between these two types is that ```int``` does not have a decimal part; ```float``` does have a decimal part which can equal 0.
```python
    # int
    type(2)
    # float
    type(2.0)
```
Python is clever enough to recognize equivalence, even where types differ: 
```python
    # test equivalence
    2 == 2.0
```
We can explicitly convert ```int``` to ```float```:
```python
    # conver int to float
    print(float(2))
```
We can also go the other way but be super careful!
```python
    # convert float to int
    print(int(2.5))
```
And be aware of other gotchas!
```python
    # division - always float!
    10/5 == 2
    # floor division - always integer
    10//5 == 2
    # remainder left over from floor division
    print(f"11/5 = {11//5} remainder {11%5}")
```
### Complex (Optional)

The ```complex``` type may come in handy for advanced mathematical calulations. There are two ways to create objects with ```complex``` type:
```python
    # directly
    z = 3 + 7j
    # with a function
    z = complex(3,7)
    # test equivalence
    3 + 7j == complex(3,7)
```
### Sets and bools

The ```set``` type is pretty simple. It simply gives us an unordered set of unique entities present in a sequence or map type object. For instance:
```python
    # list
    student_names = ["mary", "anne", "john", "anne"]
    print(set(student_names))

    # tuples
    print(set(colours))
```
```Bool``` types have two possible values - ```True```/```1``` and ```False```/```0```. We can test equivalence here:
```python
    # Test true
    True == 1
    # Test false
    False == 0
```
Notice how the returned object from an equivalence test is itself a ```Bool```!
```python
    # test for bool
    print(type(True==1)) 
```
