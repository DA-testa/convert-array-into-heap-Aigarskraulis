# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        j = i
        while 2*j+1 <n:
            k = 2*j+1
            if k+1 < n and data[k+1] < data[k]:
                k+= 1
                if data[j] <= data[k]:
                    break
                    swaps.append((j,k))
                    data[j], data[k] = data[k],data[j]
                    j = k

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
