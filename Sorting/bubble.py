arr_list = [1, 10, 2, 8, 3, 26, 20]
def Bubble(arr):
    for lastElement in range(len(arr)-1, 0, -1):
        for posx in range(lastElement):
            if arr[posx] > arr[posx+1]:
                arr[posx], arr[posx+1] = arr[posx+1], arr[posx]
    return arr


if __name__ == '__main__':
    sorted_array = Bubble(arr_list)
    print(sorted_array)

