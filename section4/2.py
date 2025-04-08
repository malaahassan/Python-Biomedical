uppercase_range = range(ord("A"), ord("Z") + 1)
lowercase_range = range(ord("a"), ord("z") + 1)
digits_range = range(ord("0"), ord("9") + 1)


strings =  [chr(x) for x in uppercase_range] + [chr(y) for y in lowercase_range] + [chr(z) for z in digits_range]
        
output_string = "".join(strings)

print(output_string)