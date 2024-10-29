1. Credit Card Mask: 
Python function called `maskify` that replaces all but the last four characters of a given string with `#`:
```
def maskify(cc):
    return "#" * (len(cc)-4) + cc[-4:]
```
