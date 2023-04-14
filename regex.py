import re

phonenumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phonenumber.search('My number is 415-555-4242')

print(mo.group())










