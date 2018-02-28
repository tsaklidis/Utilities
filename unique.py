import hashlib
import datetime


def unique_id(length=8):
    salt = hashlib.sha1(str(datetime.datetime.now())).hexdigest()[:5]
    return hashlib.sha1(salt).hexdigest()[:length]

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
