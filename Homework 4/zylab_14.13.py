#Samiha Ashraf
#1884227
def partition(user_ids, i, k):
    global num_calls
    num_calls += 1


    pivot_idx = (i + k) // 2
    pivot_value = user_ids[pivot_idx]

    l = i
    h = k

    while l <= h:

        while user_ids[l] < pivot_value:
            l += 1


        while user_ids[h] > pivot_value:
            h -= 1


        if l <= h:
            user_ids[l], user_ids[h] = user_ids[h], user_ids[l]
            l += 1
            h -= 1

    return l

def fastsort(user_ids, i, k):
    global num_calls
    if i >= k:
        return

    num_calls += 1


    pivot_idx = partition(user_ids, i, k)


    fastsort(user_ids, i, pivot_idx - 1)
    fastsort(user_ids, pivot_idx, k)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()


    num_calls = 1


    fastsort(user_ids, 0, len(user_ids) - 1)


    print(num_calls)

    for user_id in user_ids:
        print(user_id)
