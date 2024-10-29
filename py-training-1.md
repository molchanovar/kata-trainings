1. Credit Card Mask: 
Python function called `maskify` that replaces all but the last four characters of a given string with `#`:
```
def maskify(cc):
    l = len(cc)
    if l <= 4: return cc
    return (l - 4) * '#' + cc[-4:]

Or even:

def maskify(cc):
    return "#" * (len(cc)-4) + cc[-4:]
```
