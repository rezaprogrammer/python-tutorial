'''
Created on Apr 9, 2014

@author: vsa
'''

def evaluate_polish(stack):
    history = []
    while(len(stack) > 1):
        v1 = int(stack.pop(0))
        v2 = int(stack.pop(0))
        op = stack.pop(0)
        
        if op == '+':
            stack.insert(0, v1 + v2)
        elif op == '-':
            stack.insert(0, v1 - v2)
        elif op == '*':
            stack.insert(0, v1 * v2)
        elif op == '/':
            stack.insert(0, float(v1 / v2))
        elif op == '%':
            stack.insret(0, v1 % v2)
        else:
            raise RuntimeError()

        history.append((v1, op, v2))

    print(history)
    
    return stack[0]

if __name__ == '__main__':
    stack = ['3', '2', '+', '8', '/', '7', '+']
    val = evaluate_polish(stack)
    print(val)
