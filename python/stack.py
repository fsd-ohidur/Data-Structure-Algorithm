stack = []


def main():
    print('Implementing my stack in python')
    peek()
    push(2)
    push(5)
    push(10)
    push(20)
    peek()
    pop()
    push(30)
    peek()

    print(stack)


def push(x):
    stack.append(x)
    print(f'Successfully added item {x}')


def pop():
    if len(stack) > 0:
        print(f'Successfully removed item {stack[-1]}')
        stack.remove(stack[-1])
    else:
        print('Sorry! Stack is empty, failed to pop.')


def peek():
    if len(stack) > 0:
        print(f'Peek item {stack[-1]}')
    else:
        print('Sorry! Stack is empty, failed to peek.')


if __name__ == "__main__":
    main()
