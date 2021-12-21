def insertionSort(arr):
    # Traverse through 1 to len(arr)
    print("przed sortowaniem:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    print("\n")
    x = 1
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"po {x} sortowaniu")
        for i in range(len(arr)):
            print("%d" % arr[i], end = " ")
        print("\n")
        x += 1

# Driver code to test above
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    print("posortowana:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")