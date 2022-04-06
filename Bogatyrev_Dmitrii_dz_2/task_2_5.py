original_list = [57.8, 46.51, 97, 84.4, 35.5, 28.45, 15, 76.05, 2.5]


# A
def print_formated_price(price):
    digit_before_comma = int(price)
    digit_after_comma = int(price * 100) - int(digit_before_comma * 100)
    print(f'{digit_before_comma} руб {digit_after_comma:02d} коп')


for i in original_list:
    print_formated_price(i)

# B
print(id(original_list))
original_list.sort()
print(original_list)
print(id(original_list))
# C
original_list = [57.8, 46.51, 97, 84.4, 35.5, 28.45, 15, 76.05, 2.5]
print(id(original_list))
sorted_list = sorted(original_list, reverse=True)
print(sorted_list)
print(id(sorted_list))
# D
original_list = [57.8, 46.51, 97, 84.4, 35.5, 28.45, 15, 76.05, 2.5]
original_list.sort(reverse=True)
for i in range(0, 5):
    print_formated_price(original_list[i])
