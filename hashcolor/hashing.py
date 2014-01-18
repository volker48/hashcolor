from hashlib import sha1

def _and_with_padding(x, mask):
    ret = hex(x & mask).split('x')[1]
    if len(ret) < 2:
        ret = '0' + ret
    return ret

def string_to_color(string):
    x = int(sha1(string).hexdigest()[:6], 16)
    r, remainder = divmod(x, 256)
    g, remainder = divmod(remainder, 256)
    b, remainder = divmod(remainder, 256)
    return r + g + b