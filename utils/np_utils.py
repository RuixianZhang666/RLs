import numpy as np


def all_equal(x):
    '''
    return whether items in x all equal or not.
    '''
    return (x == x.reshape(-1)[0]).all()


def get_first_item(x):
    '''
    return the first item in numpy array.
    '''
    return x.reshape(-1)[0]


def is_inf_inside(x):
    '''
    return whether np.inf, -np.inf is in x or not.
    '''
    return np.isinf(x).any()


class SMA:
    '''
    Simple Moving Average
    '''

    def __init__(self, n):
        self.n = n
        self.now = 0
        self.r_list = []
        self.max, self.min, self.mean = 0, 0, 0

    def update(self, r):
        assert isinstance(r, (np.ndarray, list)), 'r must have __len__ attr'
        r = np.array(r)
        self.r_list.append(r)
        if self.now >= self.n:
            r_old = self.r_list.pop(0)
            self.max += (r.max() - r_old.max()) / self.n
            self.min += (r.min() - r_old.min()) / self.n
            self.mean += (r.mean() - r_old.mean()) / self.n
        else:
            self.now = min(self.now + 1, self.n)
            self.max += r.max() / self.now
            self.min += r.min() / self.now
            self.mean += r.mean() / self.now

    @property
    def rs(self):
        return dict([
            ['sma_max', self.max],
            ['sma_min', self.min],
            ['sma_mean', self.mean]
        ])