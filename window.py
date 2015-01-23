
class CircBuf(object):

    def __init__(self, n):
        self.buf = [None]*n
        self.ptr = 0
        self.n   = n
        
    def push(self, item):
        self.buf[self.ptr] = item
        self.ptr = (self.ptr + 1) % self.n
    
    def get_tuple(self):
        return tuple(self.buf[(self.ptr + i) % self.n] for i in range(self.n))

def sliding_window(items, n):
    if n < 1:
        raise ValueError('n must be >= 1')
    buf = CircBuf(n)
    for i, item in enumerate(items):
        buf.push(item)
        if i >= n:
            yield buf.get_tuple()

def test():
    items = list(range(10))
    for i in range(1, 10):
        print('%s: %s' % (i, list(sliding_window(items, i))))

if __name__ == '__main__':
    test()
