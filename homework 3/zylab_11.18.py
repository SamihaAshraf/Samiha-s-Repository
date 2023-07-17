#Samiha Ashraf
#1884227

def is_non_negative(num):
    return num >= 0

list_input = list(map(int, input().split()))

non_negative_list = list(filter(is_non_negative, list_input))
non_negative_list.sort()

print(*non_negative_list, end='')