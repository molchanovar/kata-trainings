### Solving 1:
def divisors(integer):
    if integer <= 1:
        raise ValueError("Integer only")
    
    divisor_list = [i for i in range(2, integer) if integer % i == 0]
    
    if not divisor_list:
        return f"{integer} is prime"
    
    return divisor_list


### Solving 2:
def divisors(integer):
  return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)


### Solving 3:
def divisors(integer):
  a = []
  for i in range(2, integer):
    if integer % i == 0:
      a.append(i)
  return a if a else str(integer) + " is prime"
