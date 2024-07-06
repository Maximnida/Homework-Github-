def my_sort(lst):
    
    for num in lst:
        if not isinstance(num, int) or num <= 0:
            raise ValueError("Barcha elementlar musbat bo'lishi kerak.")
    
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))

    sorted_lst = sorted(lst, key=lambda x: sum_of_digits(x))
    
    return sorted_lst

try:
    print(my_sort([14, 30, 103]))  
    print(my_sort([5, 31, 123, 80, 11]))
except ValueError as e:
    print(e)
