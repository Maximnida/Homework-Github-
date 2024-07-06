def check_function(user_input):
    positive_pairs = []
    negative_pairs = []
    
    user_input = list(map(int, user_input))
    
    i = 0
    while i < len(user_input) - 1:
        if user_input[i] > 0 and user_input[i + 1] > 0:
            positive_pairs.append((user_input[i], user_input[i + 1]))
        elif user_input[i] < 0 and user_input[i + 1] < 0:
            negative_pairs.append((user_input[i], user_input[i + 1]))
        i += 1
    
    return positive_pairs, negative_pairs


user_input = input("Listni kiriting(2,3,4): ").split(',')
positive_pairs, negative_pairs = check_function(user_input)

print("Musbat ishorali:", positive_pairs)
print("Manfiy ishorali:", negative_pairs)
