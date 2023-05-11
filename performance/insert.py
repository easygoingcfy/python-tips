"""测试常用数据类型插入性能"""
import time
import random

LENGTH = 10 ** 6

def test_list(data):
    l = []
    ts = time.time()
    for i in data:
        l.append(i)
    print(f"list append {LENGTH} data use {time.time() - ts:.6f} s")


def test_set(data):
    l = set()
    ts = time.time()
    for i in data:
        l.add(i)
    print(f"tuple add {LENGTH} data use {time.time() - ts:.6f} s")


if __name__ == "__main__":
    data = range(LENGTH)
    test_list(data)
    test_set(data)