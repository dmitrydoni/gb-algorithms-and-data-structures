import sys


def get_var_memory():
    all_v = 0
    for v in list(vars().keys()):
        if not v.startswith('_'):
            print(f'Variable: {v}, Memory: {sys.getsizeof(v)} bytes')
            all_v += sys.getsizeof(v)
    print(f'Total memory: {all_v}')

    details = input("Show detailed report? (y/n) ")
    if details == 'y':
        show_size()
    else:
        pass


def show_size(v, level = 0):
    print('\t' * level, f'Type: {v.__class__}, Size: {sys.getsizeof(v)}, Value: {v}')

    if hasattr(v, '__iter__'):
        if hasattr(v, 'items'):
            for xx in v.items():
                show_size(xx, level + 1)
        elif not isinstance(v, str):
            for xx in v:
                show_size(xx, level + 1)
