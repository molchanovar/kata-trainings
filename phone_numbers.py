# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# My resolving: 
def create_phone_number(n):
    string1 = ' '.join(map(str, n[0:3]))
    string2 = ' '.join(map(str, n[3:6]))
    string3 = ' '.join(map(str, n[6:11]))
    return '(' + string1.replace(" ", "") + ')' + ' ' + string2.replace(" ", "") + '-' + string3.replace(" ", "")

### Another: 
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def create_phone_number(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])

  return '({}) {}-{}'.format(str1, str2, str3)


def create_phone_number(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"


def create_phone_number(n):
    return "(" + str(n[0]) + str(n[1]) + str(n[2]) + ") " + str(n[3]) + str(n[4]) + str(n[5]) + "-" + str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])

