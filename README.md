# CRYPTO Benchmark For Python
## What's this
Python has many ECC&RSA Library.
I try to benchmark Sign&Verify Signature

## Result
### For Ubuntu 19.04(64Bit)
* CPU: Intel® Core™ i7-5500U CPU @ 2.40GHz × 4 
* Memory : 8GB

Library|Suite |Sign/Verify|Average-time(per 10000 Sign/Verify)
|:---: |:---: |:---:      |:---
python_ecdsa|P256|Sign|8.533|
python_ecdsa|P256|Verify|33.201|
starkbank_ecdsa|P256|Sign|31.177|
starkbank_ecdsa|P256|Verify|62.705|
fast_ecdsa|P256|Sign|19.0189|
fast_ecdsa|P256|Verify|16.036|
pycryptodomex|P256|Sign|5.162|
pycryptodomex|P256|Verify|14.274|
pycryptodomex|RSA-2048|Sign|17.618|
pycryptodomex|RSA-2048|Verify|5.338|
pycryptodomex|RSA-3072|Sign|46.837|
pycryptodomex|RSA-3072|Verify|9.542|
