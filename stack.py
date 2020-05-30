class Stack:

    def __init__(self):
        self._data = []

    def push(self,num):
        self._data.append(num)
        print('[+] ' ,num) 

    def length(self):
        print('[length] :',len(self._data))

    def isEmpty(self):
        return len(self._data) == 0

    def pop(self):

        if self.isEmpty():
            print('no element to pop')
        else:
            print('[-] ',self._data.pop())


def main():

    S = Stack()

    S.push(10)
    S.push(20)
    S.push(30)

    S.length()

    S.pop()

main()

        


