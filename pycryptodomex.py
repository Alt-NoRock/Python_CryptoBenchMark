from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import ECC
from Cryptodome.Signature import DSS
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
import time
import numpy

def pycryptodome_ecdsa(count,loop):
    ecc_key = ECC.generate(curve='P-256')
    message = b'I give my permission to order #4355'
    h = SHA256.new(message)

    signer = DSS.new(ecc_key, 'fips-186-3')
    time_list_sign = []
    for l in range(loop):
        start = time.time()
        for c in range (count):
            signature = signer.sign(h)
        end = time.time() - start
        # print("["+str(l)+"th pycryptodomex_ecdsa:sign second is "+ str(end) + "/"+str(count)+" signature")
        time_list_sign.append(end)
    ave_sign = numpy.mean(numpy.array(time_list_sign))

    verifier = DSS.new(ecc_key, 'fips-186-3')
    time_list_vrfy = []
    for l in range(loop):
        start = time.time()
        for c in range (count):
            try:
                verifier.verify(h, signature)
            except ValueError:
                print ("The message is not authentiend")
        end = time.time() - start
        # print("["+str(l)+"th pycryptodomex_ecdsa:vrfy second is "+ str(end) + "/"+str(count)+" signature")
        time_list_vrfy.append(end)
    ave_vrfy = numpy.mean(numpy.array(time_list_vrfy))

    print("pycryptodomex_ecdsa:sign average second is "+ str(ave_sign) + "/"+str(count)+" signature")
    print("pycryptodomex_ecdsa:vrfy average second is "+ str(ave_vrfy) + "/"+str(count)+" signature")
    return time_list_sign, time_list_vrfy


def pycryptodome_rsa(count, loop, keysize):
    key = RSA.generate(keysize)
    message = b'I give my permission to order #4355'
    time_list_sign = []

    for l in range(loop):
        start = time.time()
        for c in range (count):
            h = SHA256.new(message)
            signature = pkcs1_15.new(key).sign(h)
        end = time.time() - start
        # print("["+str(l)+"th pycryptodomex_ecdsa:sign second is "+ str(end) + "/"+str(count)+" signature")
        time_list_sign.append(end)
    ave_sign = numpy.mean(numpy.array(time_list_sign))

    time_list_vrfy = []
    for l in range(loop):
        start = time.time()
        for c in range(count):
            try:
                h = SHA256.new(message)
                pkcs1_15.new(key).verify(h, signature)
            except (ValueError, TypeError):
                print ("The signature is not valid.")
        end = time.time() - start
        # print("["+str(l)+"th pycryptodomex_ecdsa:vrfy second is "+ str(end) + "/"+str(count)+" signature")
        time_list_vrfy.append(end)
    ave_vrfy = numpy.mean(numpy.array(time_list_vrfy))

    print("pycryptodomex_rsa:sign average second is "+ str(ave_sign) + "/"+str(count)+" signature")
    print("pycryptodomex_rsa:vrfy average second is "+ str(ave_vrfy) + "/"+str(count)+" signature")
    return time_list_sign, time_list_vrfy


if __name__ == '__main__':
    pycryptodome_ecdsa(1000,10)

