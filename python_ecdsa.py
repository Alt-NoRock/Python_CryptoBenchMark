from ecdsa import SigningKey , NIST256p
import time
import numpy

def python_ecdsa(count,loop):

    sk = SigningKey.generate(curve=NIST256p) # uses NIST192p
    vk = sk.get_verifying_key()

    time_list_sign = []
    for l in range(loop):
        start = time.time()
        for c in range (count):
            signature = sk.sign(b"message")
        end = time.time() - start
        # print("["+str(l)+"th python_ecdsa:sign second is "+ str(end) + "/"+str(count)+" signature")
        time_list_sign.append(end)
    ave_sign = numpy.mean(numpy.array(time_list_sign))

    time_list_vrfy = []
    for l in range(loop):
        start = time.time()
        for c in range (count):
            assert vk.verify(signature, b"message")        
        end = time.time() - start
        # print("["+str(l)+"th python_ecdsa:vrfy second is "+ str(end) + "/"+str(count)+" signature")
        time_list_vrfy.append(end)
    ave_vrfy = numpy.mean(numpy.array(time_list_vrfy))

    print("python_ecdsa:sign average second is "+ str(ave_sign) + "/"+str(count)+" signature")
    print("python_ecdsa:vrfy average second is "+ str(ave_vrfy) + "/"+str(count)+" signature")
    return time_list_sign, time_list_vrfy

if __name__ == '__main__':
    python_ecdsa(1000,10)

