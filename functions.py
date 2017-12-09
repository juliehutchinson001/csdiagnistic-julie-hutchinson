#Solution to Problem 6: Functions

def fibonacci_iterative(num):

    numb = 1
    fibo = []

    index = 0
    for counter in range(num):
        if counter < 2:
            fibo.append(numb)
            numb += 1
            continue

        previous_num = fibo[-2]
        current_num = fibo[-1]

        fibo.append(previous_num + current_num)

    for number in fibo:
        print(number)

fibonacci_iterative(7)