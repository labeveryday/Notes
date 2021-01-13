# Python Notes

Examples

```
# Tuples
x = (1,)
y = 1,
```

Sets

```
x = {4}
```

List comprehensions
```
numbers = [1, 2, 4, 5, 7, 8, 10]
even_numbers = [x for x in numbers if (x %) == 0]
```

Lambda functions - used to return outputs (Think of a function)
- Normally given an assigned name
- Single line
[x,y are params:  x + y are return values]

sequence = [79, 3]
double = [(lambda x: x * 2)(2) for x in sequence]

```
add = lambda x, y: x + y
add(2, 4)
```

Unpacking arguments

```
numbers = [1, 9]
num_dict = {"x": 5, "y": 9}

def add(x, y):
    return x + y

add(*numbers)

add(**num_dict)


def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

def apply(*apply(*args, operator)):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(*args)
    else:
        return "No valid operator provided to apply()"

apply(1, 3, 5, 8, operator="+")
```


Unpacking Keywork arguments

```
def named(**kwargs):
    print(kwags)

named(name="Du'An", contact="@labeveryday")


def named(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

named(**details)
```

