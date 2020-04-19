from unittest.case import TestCase
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.signature import Signature
import time
import numpy

def starbank_ecdsa(count,loop):
    privateKey = PrivateKey()
    publicKey = privateKey.publicKey()
    message = "This is the right message"
    message_f = b"This is the right messages"

    time_list_sign = []
    for l in range(loop):
        start = time.time()
        for c in range (count):
            signature = Ecdsa.sign(message, privateKey)
        end = time.time() - start
        # print("["+str(l)+"th starbank_ecdsa:sign second is "+ str(end) + "/"+str(count)+" signature")
        time_list_sign.append(end)
    ave_sign = numpy.mean(numpy.array(time_list_sign))

    time_list_vrfy = []
    for l in range(loop):
        start = time.time()
        for c in range (count):
            if (Ecdsa.verify(message, signature, publicKey) == False):
                print ("err")
        end = time.time() - start
        # print("["+str(l)+"th starbank_ecdsa:vrfy second is "+ str(end) + "/"+str(count)+" signature")
        time_list_vrfy.append(end)
    ave_vrfy = numpy.mean(numpy.array(time_list_vrfy))

    print("starbank_ecdsa:sign average second is "+ str(ave_sign) + "/"+str(count)+" signature")
    print("starbank_ecdsa:vrfy average second is "+ str(ave_vrfy) + "/"+str(count)+" signature")
    return time_list_sign, time_list_vrfy


if __name__ == '__main__':
    starbank_ecdsa(10000,10)
