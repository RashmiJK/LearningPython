import sys
import bz2

opener = bz2.open
print('out')
if __name__ == '__main__':
    print('in')
    f = bz2.open(sys.argv[1], mode='wt')
    f.write(''.join(sys.argv[2:]))
    f.close()