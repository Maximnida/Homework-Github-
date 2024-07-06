def naqsh(colors):
    if not colors:
        return 0
    
    time = 2  
    
    for i in range(1, len(colors)):
        if colors[i] != colors[i - 1]:
            time += 3  
        else:
            time += 2  
    
    return time

print(naqsh(["Red", "Blue", "Red", "Blue", "Red"])) 
print(naqsh(["Blue"]))  
print(naqsh(["Red", "Yellow", "Green", "Blue"]))  
print(naqsh(["Blue", "Blue", "Blue", "Red", "Red", "Red"])) 
