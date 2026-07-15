import random


class NeuralNetwork:
    def dataset(i1, i2, i3):
        data = []
        data[0][0][0] = i1
        data[0][1][0] = i2
        data[0][0][1] = i3
        return

    def train(i1, i2, i3, bias, t):
        w1early = random.randint(-10, 10)
        w2early = random.randint(-10, 10)
        w3early = random.randint(-10, 10)
        u = (
            (float(i1) * float(w1early))
            + (float(i2) * float(w2early))
            + (float(i3) * float(w3early))
            + bias
        )
        if u > 0:
            u = 1
        else:
            u = 0
        e = u - t
        for i in range(10):
            print(i)
