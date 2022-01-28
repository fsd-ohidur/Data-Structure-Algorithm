queue = []


def main():
    print('Implementing my queue in python')
    dequeue()
    enqueue(2)
    enqueue(5)
    enqueue(10)
    enqueue(20)
    dequeue()
    dequeue()

    print(queue)


def enqueue(x):
    queue.append(x)
    print(f'Successfully added item {x}')


def dequeue():
    if len(queue) > 0:
        print(f'Successfully removed item {queue[0]}')
        queue.remove(queue[0])
    else:
        print('Sorry! Stack is empty, failed to pop.')


if __name__ == "__main__":
    main()
