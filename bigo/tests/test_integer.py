from types_ import Integer as Int


def test_repr():
    vals = [Int() for x in range(10)]
    for v in vals: print(v.power, v.power, v.factor, v.divisor)
    print()
    for v in vals: print(v)

def test_repr_2(iter=25):
    for x in range(iter):
        print(Int())

if __name__ == '__main__':
    # test_repr()
    test_repr_2(50)