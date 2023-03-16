import math

def build_heap(input_list):
    swaps = []
    n = len(input_list)

    for i in range(n//2, -1, -1):
        heapify(input_list, i, n, swaps)

    return swaps

def heapify(input_list, i, n, swaps):
    left = 2*i + 1
    right = 2*i + 2

    smallest = i
    if left < n and input_list[left] < input_list[smallest]:
        smallest = left

    if right < n and input_list[right] < input_list[smallest]:
        smallest = right

    if smallest != i:
        input_list[i], input_list[smallest] = input_list[smallest], input_list[i]
        swaps.append((i, smallest))
        heapify(input_list, smallest, n, swaps)

def main():
    mode = input().strip()[0]
    n = 0
    input_list = []
    if mode == "F":
        with open("./tests/" + input().strip()) as file:
            n = int(file.readline().strip())
            input_list = list(map(int, file.readline().split()))
    elif mode == "I":
        n = int(input().strip())
        input_list = list(map(int, input().strip().split()))

    swaps = build_heap(input_list)
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

if __name__ == "__main__":
    main()
