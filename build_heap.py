def swap(data, i, res):
    left = 2*i + 1
    right = 2*i + 2
    n = len(data) 
    
    if left >= n:
        return
    
    x = left
    if right < n and data[left] > data[right]:
        x = right

    if data[i] > data[x]:  
        res.append([i, x]) 
        data[i], data[x] = data[x], data[i]
        swap(data, x, res) 

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(int((n - 2)/2), -1, -1):
        swap(data, i, swaps)

    return swaps

def main():
    mode = input()

    if mode.startswith("F"):
        name = input()
        if name != "a":
            with open(f"./tests/{name}") as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))

    elif mode.startswith("I"):
        n = int(input()) 
        data = list(map(int, input().split()))

    else:
        return
    
    assert len(data) == n

    swaps = build_heap(data) 
    assert len(swaps) < 4*len(data)

    print(len(swaps))
    for i, j in swaps: 
        print(i, j)
