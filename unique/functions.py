import hashlib
import datetime

# Create a random string based on timestamp
# Don't overload your system over get_random_string(1000000)
def get_random_string(length=8, prefix='', suffix='', valid_chars=False):
    u = ''
    while True:
        if len(u) < length:
            salt = hashlib.sha256(str(datetime.datetime.now())).hexdigest()
            if valid_chars:
                pass
            else:
                u += hashlib.sha1(salt).hexdigest()
        else:
            break
    return '{0}{1}{2}'.format(prefix, u[:length], suffix)


# import string, time, math, random

# def unique_id(prefix='', more_entropy=False):
#     m = time.time()
#     uniqid = '%8x%05x' %(math.floor(m),(m-math.floor(m))*1000000)
#     if more_entropy:
#         valid_chars = list(set(string.hexdigits.lower()))
#         entropy_string = ''
#         for i in range(0,10,1):
#             entropy_string += random.choice(valid_chars)
#         uniqid = uniqid + entropy_string
#     uniqid = prefix + uniqid
#     return uniqid
