def string_combination(char_set, length):
    if length == 0:
        return {''}
    simpler_result = string_combination(char_set, length - 1)
    result = set()
    for character in char_set:
        for simpler_result_entry in simpler_result:
            result.add(character + simpler_result_entry)
    return result


if __name__ == '__main__':
    result = string_combination({'a', 'b', 'c'}, 10)
    print(result)
