import pycryptodomex
import fast_ecdsa
import python_ecdsa
import starbank_ecdsa
import numpy
import csv

def make_log(name, suite, time_list_sign, time_list_vrfy):
    result_all = []
    fn = "bench_result.csv"
    ave_sign = numpy.mean(numpy.array(time_list_sign))
    ave_vrfy = numpy.mean(numpy.array(time_list_vrfy))
    result = [name, suite, "Sign", ave_sign]
    result.extend(time_list_sign)
    result_all.append(result)
    result = [name, suite, "Verify", ave_vrfy]
    result.extend(time_list_vrfy)
    result_all.append(result)

    with open(fn, 'a')as f:
        csvwriter = csv.writer(f,lineterminator='\n')
        csvwriter.writerows(result_all)


count = 10000
loop  = 10

time_list_sign, time_list_vrfy = python_ecdsa.python_ecdsa(count,loop)
make_log("python_ecdsa","P256",time_list_sign, time_list_vrfy)

time_list_sign, time_list_vrfy = starbank_ecdsa.starbank_ecdsa(count,loop)
make_log("starkbank_ecdsa","P256",time_list_sign, time_list_vrfy)

time_list_sign, time_list_vrfy = fast_ecdsa.fast_ecdsa(count,loop)
make_log("fast_ecdsa","P256",time_list_sign, time_list_vrfy)

time_list_sign, time_list_vrfy = pycryptodomex.pycryptodome_ecdsa(count,loop)
make_log("pycryptodomex","P256",time_list_sign, time_list_vrfy)

time_list_sign, time_list_vrfy = pycryptodomex.pycryptodome_rsa(count,loop,2048)
make_log("pycryptodomex","RSA-2048",time_list_sign, time_list_vrfy)

time_list_sign, time_list_vrfy = pycryptodomex.pycryptodome_rsa(count,loop,3072)
make_log("pycryptodomex","RSA-3072",time_list_sign, time_list_vrfy)

