def process_numbers(numbers):
    unique_values = list(set(numbers))

    result = {
        "original_list \n": numbers,
        "unique_values \n": unique_values,
        "count \n": len(unique_values)
    }
    
    return result

numbers = list(map(int, input().split()))

output = process_numbers(numbers)
print(output)