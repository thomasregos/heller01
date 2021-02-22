import random

from multiprocessing import Pool, cpu_count, Queue, Process, current_process
from statistics import mean
from datetime import datetime
import time
import concurrent.futures


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


def random_coordinates_inside(radius=1, iterations=1):
    result = {'Inside': 0,
              'Outside': 0}

    proc_name = current_process().name

    wait_time = random.randrange(0, 2)

    print('{proc} is waiting: {ti}'.format(proc=proc_name, ti=wait_time))
    time.sleep(wait_time)

    for _ in range(0, iterations):
        y_coor = random.randrange(0, radius*100000)/100000
        x_coor = random.randrange(0, radius*100000)/100000

        if y_coor**2 + x_coor**2 < radius**2:
            result['Inside'] += 1
        else:
            result['Outside'] += 1

    # queue.put(result['Inside'])

    print('Process {} ended'.format(proc_name))



    return result


def pi_approx(n: int) -> float:

    start = datetime.now()
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

    # processes = [Process(target=random_coordinates_inside, args=(queue, 1, n)) for _ in range(10)]
    # # processes = [Process(target=random_coordinates_inside, args=(queue, 1, n)) for _ in range(cpu_count()-1)]
    #
    # for p in processes:
    #     p.start()
    #
    # for p in processes:
    #     p.join()
    #
    # results = [queue.get() for _ in processes]


    # DIFFERENT MULTI
    # results = {}
    # # values = (queue, 1, n)
    # values = (( 1, n), ( 1, n), ( 1, n), ( 1, n), ( 1, n), ( 1, n))
    # with Pool() as pool:
    #     # res = pool.map(random_coordinates_inside, values)
    #     res = pool.starmap(random_coordinates_inside, values)
    #
    # # Queue objects should only be shared between processes through inheritance
    # for i in res:
    #     results.update(i)

    # At work
    #

    futures_list = []
    result = []


    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for i in range(1, 20):
            futures = executor.submit(random_coordinates_inside, radius=1, iterations=n)
            futures_list.append(futures)

        for future in concurrent.futures.as_completed(futures_list):
            result = future.result()

    # results = [queue.get() for _ in processes]
# ___________________________________

    in_points = mean(result)

    end = datetime.now()
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
