import queue

def fun(expression):
    stack = queue.LifoQueue()
    splited = expression.split()

    for char in splited:
        if char.isnumeric():
            stack.put(int(char))
        elif char in "+-*/":
            second = stack.get()
            first = stack.get()
            if char == '+':
                stack.put(first + second)
            elif char == '-':
                stack.put(first - second)
            elif char == '*':
                stack.put(first*second)
            elif char == '/':
                stack.put(first/second)

    return stack.get()

print(f"{fun(f"{fun("2 3 +")} {fun("2 3 +")} *")}")