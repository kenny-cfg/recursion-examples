def string_combination(char_set, length):
    if length == 1:
        return char_set
    simpler_result = string_combination(char_set, length - 1)
    result = set()
    for character in char_set:
        for simpler_result_entry in simpler_result:
            result.add(character + simpler_result_entry)
    return result

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