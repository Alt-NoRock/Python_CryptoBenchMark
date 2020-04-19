from fastecdsa import curve, ecdsa, keys
from hashlib   import sha256
import time
import numpy

def fast_ecdsa(count,loop):
    private_key = keys.gen_private_key(curve.P256)
    public_key = keys.get_public_key(private_key, curve.P256)
    # standard signature, returns two integers

    with open("message.txt","rb")as f:
        m = f.read()

    time_list_sign = []
    for l in range(loop):
        start = time.time()
        for c in range (count):
            r, s = ecdsa.sign(m, private_key)
        end = time.time() - start
        # print("["+str(l)+"th fast_ecdsa:sign second is "+ str(end) + "/"+str(count)+" signature")
        time_list_sign.append(end)
    ave_sign = numpy.mean(numpy.array(time_list_sign))

    time_list_vrfy = []
    for l in range(loop):
        start = time.time()
        for c in range (count):
            valid = ecdsa.verify((r, s), m, public_key)
        end = time.time() - start
        # print("["+str(l)+"th fast_ecdsa:vrfy second is "+ str(end) + "/"+str(count)+" signature")
        time_list_vrfy.append(end)
    ave_vrfy = numpy.mean(numpy.array(time_list_vrfy))

    print("fast_ecdsa:sign average second is "+ str(ave_sign) + "/"+str(count)+" signature")
    print("fast_ecdsa:vrfy average second is "+ str(ave_vrfy) + "/"+str(count)+" signature")
    return time_list_sign,time_list_vrfy


if __name__ == '__main__':
    fast_ecdsa(1000,10)