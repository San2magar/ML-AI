class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1

    def push(self, item):
        if self.top == self.size - 1:
            print("Stack overflow: Cannot push, the stack is full.")
        else:
            self.top += 1
            self.stack[self.top] = item
            print(f"{item} pushed onto the stack.")

    def pop(self):
        if self.top == -1:
            print("Stack underflow: Cannot pop from an empty stack.")
        else:
            removed = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f"Popped item: {removed}")

    def peek(self):
        if self.top == -1:
            print("Stack is empty: No top element to peek.")
        else:
            print(f"Top element: {self.stack[self.top]}")

    def display(self):
        if self.top == -1:
            print("Stack is empty: Nothing to display.")
        else:
            print("Stack elements from top to bottom:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

    def sum_stack(self):
        if self.top == -1:
            print("Stack is empty: Cannot compute sum.")
        else:
            total = 0
            for i in range(self.top + 1):
                try:
                    total += int(self.stack[i])
                except ValueError:
                    print(f"Non-numeric value '{self.stack[i]}' encountered, skipping.")
            print(f"Sum of stack elements: {total}")

    def check_prime(self):
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        print("Prime elements in the stack:")
        found = False
        for i in range(self.top + 1):
            try:
                val = int(self.stack[i])
                if is_prime(val):
                    print(val)
                    found = True
            except ValueError:
                continue
        if not found:
            print("No prime numbers found.")

    def even_odd(self):
        print("Even/Odd classification:")
        for i in range(self.top + 1):
            try:
                val = int(self.stack[i])
                kind = "Even" if val % 2 == 0 else "Odd"
                print(f"{val} is {kind}")
            except ValueError:
                print(f"{self.stack[i]} is not a number")

    def reverse_stack(self):
        if self.top == -1:
            print("Stack is empty: Cannot reverse.")
        else:
            print("Reversed stack elements:")
            for i in range(0, self.top + 1):
                print(self.stack[i])

    def alternate_elements(self):
        if self.top == -1:
            print("Stack is empty: No alternate elements to show.")
        else:
            print("Alternate elements from top to bottom:")
            for i in range(self.top, -1, -2):
                print(self.stack[i])


def main():
    size = int(input("Enter the size of the stack: "))
    s = Stack(size)

    while True:
        print("\nStack Operations Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Sum")
        print("6. Prime Numbers")
        print("7. Even/Odd")
        print("8. Reverse")
        print("9. Alternate Elements")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            value = input("Enter the value to push: ")
            s.push(value)
        elif choice == '2':
            s.pop()
        elif choice == '3':
            s.peek()
        elif choice == '4':
            s.display()
        elif choice == '5':
            s.sum_stack()
        elif choice == '6':
            s.check_prime()
        elif choice == '7':
            s.even_odd()
        elif choice == '8':
            s.reverse_stack()
        elif choice == '9':
            s.alternate_elements()
        elif choice == '10':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()