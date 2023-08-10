def string_combination(char_set, length):
    pass
"""
Exit condition:
* If length = 1, return the letters back
{ 'a', 'b' }, length = 1 -> [ 'a', 'b' ]

OR (if you're really clever):

* If length = 0, return [ '' ]
{ 'a', 'b' }, length = 0 -> [ '' ]

Recursion:
* Work out the combinations with length as length - 1


Concrete example:
char_set = {'a', 'b'}, length = 3

length = 2 gives:
  aa
  ab
  ba
  bb

Prepend with each of char_set in turn:
  a + aa
  a + ab
  a + ba
  a + bb
  
  b + aa
  b + ab
  b + ba
  b + bb
"""