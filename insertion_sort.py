def sort(data):

    for k in range(1,len(data)):
        cur = data[k]
        j = k
        while j > 0 and data[j-1] > cur :
            data[j] = data[j-1]
            j -= 1;
            data[j] = cur

def main():

    array = [3,5,2,6,1,9]
    print(array)
    sort(array)

    print(array)

main()
