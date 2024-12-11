def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  # This will cause ZeroDivisionError to be raised, not caught 
    try:
        result = b / a
        return result
    except TypeError:
        return "Error: Type mismatch"

# Example call that will raise the exception
print(function_with_uncommon_error(0, 10))