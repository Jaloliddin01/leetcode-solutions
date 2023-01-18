import random

def average(a, b):
    return (a + b) / 2

def running_avg(nums):
    avgs = []
    total = 0

    for i, num in enumerate(nums):
        total += num
        curr = average(total, i + 1)
        avgs.append(curr)

    return avgs

def highest(nums):
    res = running_avg(nums)
    return max(res)

def generator(n):
    return random.sample(range(1, 300), n)

if __name__ == '__main__':
    nums = generator(10)
    print('Numbers: ', nums)
    print('Running average: ', running_avg(nums))
    print('Highest running average: ', highest(nums))