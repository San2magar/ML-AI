class Circular:
    def __init__(self,size):
        self.queue=[None]*size
        self.size=size
        self.front = -1
        self.rear = -1

    def enqueue(self,item):
        if (self.rear+1)% self.size == self.front:
            print('circular queue is full')
        else:
            if self.front == -1:
                self.front = self.rear =0
            else:
                self.rear =(self.rear + 1)%self.size
            self.queue[self.rear] = item
            print(f'{item} is required')

    def dequeue(self):
        if self.front == -1:
            print('the queue is empty')
            return
        else:
            removed=self.queue[self.front]
            self.queue[self.front]=None
            if self.front == self.rear:
               self.front = self.rear = - 1
            else:
                self.front = (self.front+1) % self.size

            print(f'{removed} is dequeued from the queue')

    def display(self):
        if self.front == -1:
            print('the queue is empty')
        else:
            print('circular queue data :')
            i=self.front
            while True:
                print(self.queue[i],end='  ')
                if i==self.rear:
                    break
                i=(i+1)%self.size
            print( )
                

def main():

        size = int (input ('enter the size of the queue :'))        

        q=Circular(size)

        while True:

            print('\n __ linear queue to be performed on the data :')
            print('1. enqueue')
            print('2. dequeue')
            print('3. display')
            print('4. exit')
        

            choice = input('enter the choice')

    

            if choice=='1':
                value=input('enter the value to be pushed into the queue :')
                q.enqueue(value)
            elif choice=='2':
                q.dequeue()
            elif choice=='3':
                q.display()
            elif choice=='4':
                print(' we are exiting....')
                break
            else:
                print('invalid choice so choose the value from 1-4')

if __name__ == '__main__':
    main()                
            

