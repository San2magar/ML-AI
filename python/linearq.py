class Linear:
    def __init__(self,size):
        self.queue=[None]*size
        self.size=size
        self.front = -1
        self.rear = -1

    def enqueue(self,item):
        if self.rear == self.size - 1:
            print("linear queue is overflow")
        else:
            if self.front == -1 :
                self.front = 0
            
            self.rear += 1
            self.queue[self.rear] = item
            print(f'{item} is inserted')    

    def dequeue(self):
        if self.front == -1 and self.front > self.rear:
            print(" linear queue is underflow")
        else:
            self.queue[self.front] = None
            self.front += 1
            print(f'the dequeued item is {self.queue[self.front]}')
    
    def display(self):
        if self.front == -1 and self.front > self.rear:
            print('linear queue is underflow')
        else:
            print('queue data')
            for i in range(self.front,self.rear+1):
                print(self.queue[i])
    

def main():

        size = int (input ('enter the size of the queue'))        

        q=Linear(size)

        while True:

            print('\n __ linear queue to be performed on the data')
            print('1. enqueue')
            print('2. dequeue')
            print('3. display')
            print('4. exit')
        

            choice = input('enter the choice')

    

            if choice=='1':
                value=input('enter the value to be pushed into the queue')
                q.enqueue(value)
            elif choice=='2':
                q.dequeue()
            elif choice=='3':
                q.display()
            elif choice=='4':
                print(' we are exiting....')
                break
            else:
                print('invalid choice so choose the value from 1-5')

if __name__ == '__main__':
    main()