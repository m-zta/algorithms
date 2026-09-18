def swap(arr, i, j):
    # TODO: Input validation
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def bubble_sort(arr):
    length = len(arr)

    if length < 2:
        print("Da array is too fakin short dawg...")
        return
    
    swapped = True
    while swapped:
        swapped = False
        i = 0
        j = 1
        while j < length:
            if arr[j] < arr[i]:
                swap(arr, i, j)
                swapped = True
            i += 1
            j += 1
    return arr

def main():
    arr = [9, 4, 6, 2, 7, 1]
    print(arr)
    print(swap(arr, 0, 5))
    print(bubble_sort(arr))


if __name__ == "__main__":
    main()
