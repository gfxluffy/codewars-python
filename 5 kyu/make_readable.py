def make_readable(seconds):
    return '{:0>2d}:{:0>2d}:{:0>2d}'.format(seconds // 3600, seconds % 3600 // 60, seconds % 3600 % 60)