import random
import time

def gen_questions ():
    operations = ['+', '-', '*', '/']
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    op = random.choice(operations)

    if op == "/":
        n1 = n2 * random.randint(1, 10)  # Ensure n1 is a multiple of n2
        answer = n1 / n2
    if 
