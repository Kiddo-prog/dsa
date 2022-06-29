arr_list = [1, 10, 2, 8, 3, 26, 20]

def Merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        Merge(left)
        Merge(right)

        a, b, c = 0, 0, 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                arr[c] = left[a]
                a += 1
            else:
                arr[c] = right[b]
                b += 1
            c += 1

        while a < len(left):
            arr[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            arr[c] = right[b]
            b += 1
            c += 1

    return arr

if __name__ == '__main__':
    sorted_array = Merge(arr_list)
    print(sorted_array)


        