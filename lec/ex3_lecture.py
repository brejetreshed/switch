def extract_str(s):
    str_with_number = s[-2:]
    try:
        return int(str_with_number)
    except ValueError:
        return 0

def add(a, b):
    return a + b

str1 = "my number is 26"
str2 = "my number is 11"
sum1 = add(extract_str(str1), 4)
sum2 = add(extract_str(str2), 9)
result = add(sum1, sum2)
print(f"Result: {result}")  # Expected: 50, but...