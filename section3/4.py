sequence = [10, 20, 30, 40, 50, 60]
sequence = enumerate(sequence)
even_sum = 0
odd_sum = 0

for i, n in sequence: 
    if(i % 2 == 0):
        even_sum+= n
    else:
        odd_sum+= n
        
print(f"Even sum = {even_sum}, Odd sum = {odd_sum}")