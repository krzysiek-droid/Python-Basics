
array = [13, 'string', 2.34, 0, 'e', True, False, [], {'key': 3}]
collected_errors = []
result = 0
for element in array:
    try:
        result = 10/element
    except TypeError as te:
        result = 0
        collected_errors.append(te)
    except ZeroDivisionError as zde:
        result = 0
        collected_errors.append(zde)

    print(result)

for error in collected_errors:
    print(f'- {error}')