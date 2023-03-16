def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        j = i
        while 2 * j + 1 < n:
            k = 2 * j + 1
            if k + 1 < n and data[k + 1] < data[k]:
                k += 1
            if data[j] <= data[k]:
                break
            swaps.append((j, k))
            data[j], data[k] = data[k], data[j]
            j = k
    return swaps


if __name__ == "__main__":
    input_type = input().upper()
    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))
    elif input_type == "F":
        try:
            file_name = input()
            with open(file_name, 'r') as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found")
            exit(0)
    else:
        print()
        exit(0)

   
    if len(data) != n:
        print()
        exit(0)

    swaps = build_heap(data)

    # output 
    num_swaps = len(swaps) + 1
    if num_swaps >= 4 * n:
        print()
    else:
        print(num_swaps)

    # output all swaps
    for i in range(len(swaps)):
        j, i = swaps[i]
        print(j, i)
