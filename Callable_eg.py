class Stuff(object):
    def __init__(self, x, y, range):
        super(Stuff, self).__init__()
        self.x = x
        self.y = y
        self.range = range

    def __call__(self, x, y):
        self.x = x
        self.y = y
        print('__call__ with (%d,%d)' % (self.x, self.y))

    def __del__(self):
        del self.x
        del self.y
        del self.range
