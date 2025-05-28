class Stack:
    def __init__(self,size):
        self.stack=[None]*size
        self.size=size
        self.top=-1

    
    def push(self,item):
        if self.top == self.size-1:
            print('stack is overflow')
        else:
            self.top+=1
            self.stack[self.top]=item
            print(f'{item} is pushed into the stack')

    def pop(self):
        if self.top == -1:
            print('stack is underflow !!!')
        else:
            removed = self.stack[self.top]
            self.stack[self.top]=None
            print(f'the popped item is{removed}')

    def peek(self):
        if self.top == -1:
            print('stack is underflow we cannot display the last element in the stack')   
        else:
            print(f'The last element in the stack is {self.stack[self.top]}')


    def display(self):
        if self.top == -1:
            print('stack is underflow we cannot display the last item in the stack')
        else: 
            print('stack data')
            for i in range(self.size,-1,-1):
                print(self.stack[i])
    
    def sum_stack(self):
        if self.top == -1:
            print('stack is empty sum is 0')
        else:
            total = 0
            for i in range (self.top + 1):
                try: 
                    total = float(self.stack[i])
                except (ValueError,TypeError):
                    print(f'skipping non-numeric value: {self.stack[i]}')  
            print(f'the sum of elements of stack is{total}')              


def main():

    size = int (input('enter the size of the stack'))

    s=Stack(size)

    while True:

        print('\n __ stack to be performed on the data')
        print('1. push')
        print('2. pop')
        print('3. peek')
        print('4. display')
        print('5. exit')
        print('6. sum')

        choice = input('enter the choice')

    

        if choice=='1':
            value=input('enter the value to be pushed into the stack')
            s.push(value)
        elif choice=='2':
            s.pop()
        elif choice=='3':
            s.peek()   
        elif choice=='4':
            s.display() 
        elif choice=='5':
            print(' we are exiting....')
            break
        elif choice=='6':
            s.sum_stack()

        else:
            print('invalid choice so choose the value from 1-5')


if __name__ == '__main__':
    main()        



        


