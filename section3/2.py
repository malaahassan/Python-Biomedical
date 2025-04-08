fl_num = 1234.5678
bef_int_num = 2
aft_int_num = 3

fl_num_string = str(fl_num)

fl_num_string_decimal = fl_num_string.find(".")

fl_num_new_string = fl_num_string[fl_num_string_decimal - bef_int_num : fl_num_string_decimal + aft_int_num + 1]

print("result = ", fl_num_new_string)
    