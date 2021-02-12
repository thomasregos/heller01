import random

from multiprocessing import Pool, cpu_count, Queue, Process
from statistics import mean
from datetime import datetime

# Fibonacci counter
def fibonacci(n: int, cache: list = (1, 1)) -> int:
    if n == 1:
        return cache[0]
    if n == 2:
        return cache[1]

    count = 3

    n1, n2 = cache

    while True:
        nth = n1 + n2
        if count == n:
            return nth

        count += 1
        n1 = n2
        n2 = nth


def random_coordinates_inside(queue, radius=1, iterations=1):
    result = {'Inside': 0,
              'Outside': 0}
    for _ in range(0, iterations):
        y_coor = random.randrange(0, radius*100000)/100000
        x_coor = random.randrange(0, radius*100000)/100000

        if y_coor**2 + x_coor**2 < radius**2:
            result['Inside'] += 1
        else:
            result['Outside'] += 1

    queue.put(result['Inside'])

    return result


def pi_approx(n: int) -> float:

    start=datetime.now()
    queue = Queue()
    result = random_coordinates_inside(queue=queue, radius=1, iterations=n)

    in_points = result['Inside']

    results = [queue.get() for _ in range(0, 1)]
    # not used just needed to run

    end=datetime.now()
    print(end-start)

    return (4*in_points)/n


def pi_approx_par(n: int) -> float:

    start = datetime.now()
    queue = Queue()

    processes = [Process(target=random_coordinates_inside, args=(queue, 1, n)) for _ in range(cpu_count()-1)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [queue.get() for _ in processes]

    in_points = mean(results)

    end=datetime.now()
    print(end-start)

    return (4*in_points)/n





if __name__ == '__main__':

    iter = 100000
    # 10000000
    pi_parallel = pi_approx_par(iter)
    print(pi_parallel)
    # the overhead of the multiprocessing is still bigger than the advantage of it

    pi_normal = pi_approx(iter)
    print(pi_normal)

    # Fibonacci
    print(fibonacci(4))
