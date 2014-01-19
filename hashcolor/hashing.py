from hashlib import sha1

def _and_with_padding(x, mask):
    ret = hex(x & mask).split('x')[1]
    if len(ret) < 2:
        ret = '0' + ret
    return ret

def string_to_color(string, mask=0xFE):
    x = int(sha1(string).hexdigest()[:6], 16)
    remainder, b = divmod(x, 256)
    r, g = divmod(remainder, 256)
    return ''.join(_and_with_padding(color, mask) for color in (r, g, b))