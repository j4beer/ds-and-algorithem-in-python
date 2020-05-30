def search(data,key,low,high):
    if low >= high:
        return -1
    else:
        mid = (low+high)//2;
        if data[mid] == key:
            return mid;
        elif key < data[mid]:
            return search(data,key,low,mid-1)
        else:
            return search(data,key,mid+1,high)

    return -1;


def main():

    arr = [22,33,44,55,66,77,88,89]
    key = int(input('enter the key to search :'))

    result = search(arr,key,0,len(arr)-1)

    if result == -1:
        print(key,' not found')
    else:
        print('key found at index of', result+1)

main()

