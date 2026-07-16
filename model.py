import random


class NeuralNetwork:

    def __init__(self):
        self.data = []

    def dataset(self,i1, i2, i3):
        self.data[0][0][0] = i1
        self.data[0][1][0] = i2
        self.data[0][0][1] = i3
        return

    def train(self,i1, i2, i3, bias, t):
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
        while e < len(self.data):
            updw1 = w1early+bias*self.data[0][0][0]*e
            updw2 = w2early+bias*self.data[0][1][0]*e
            updw3 = w3early+bias*self.data[0][0][1]*e
