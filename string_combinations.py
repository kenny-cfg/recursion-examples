def string_combination(char_set, length):
    if length == 1:
        return char_set
    raise NotImplementedError
"""
Exit condition:
* If length = 0, return [ '' ]
{ 'a', 'b' }, length = 0 -> [ '' ]

Recursion:
* Work out the combinations with length as length - 1
* Prepend in turn the elements of char_set
* Add all those resulting strings to a new set

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