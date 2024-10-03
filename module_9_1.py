def apply_all_func(int_list, *functions):
    result ={}
    for func in functions:
        try:
            result[func.__name__] = func(int_list)
        except Exception as e:
            result[func.__name__] = str(e)
    return result
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
