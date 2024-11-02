import numpy as np
import numpy.random as random


a = np.random.rand(10)

def slope(m):
    return (m[1,1]-m[0,1])/(m[1,0]-m[0,0])
# considering that column 0 is x and column 1 is y
def main():
    b = a.reshape(5, 2)
    print(b)
    print(slope(b))


if __name__ == '__main__':
    main()