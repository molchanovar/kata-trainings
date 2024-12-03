# Creating a new listpopulate it with elements of data (elm)
# that meet the condition after the if
# which is checking if element is instance of an int: 
def filter_list(l):
    integers = [elm for elm in l if isinstance(elm, int)]
    return integers

# Or in one string: 
def filter_list(l):
  return [x for x in l if type(x) is not str]
