import hashlib
import sys

help2 = """hash-en-sh v1.5
Copyright (c) 2022-2023 by atmosphere07
hash-en-sh [OPINION] [FILENAME]
hash-em-sh --help show all help"""
help  ="""hash-en-sh v1.5
Copyright (c) 2022-2023 by atmosphere07
Homepage: https://github.com/atmosphere07/atmosphere07-Projects
hash-en-sh [OPINION] [FILENAME]
Usage:
    -md5
    -sha1
    -sha224
    -sha256
    -sha384
    -sha512
    -h(--help, -help) you are watching it now"""
help3 = "helloword"


try:
    opinion = sys.argv[1]
    def sha256(filename):
        with open(filename, 'rb') as f:
            data = f.read()
        return hashlib.sha256(data)
    def md5(filename):
        with open(filename, 'rb') as f:
            data = f.read()
        return hashlib.md5(data)
    def sha1(filename):
        with open(filename, 'rb') as f:
            data = f.read()
        return hashlib.sha1(data)
    def sha224(filename):
        with open(filename, 'rb') as f:
            data = f.read()
        return hashlib.sha224(data)
    def sha384(filename):
        with open(filename, 'rb') as f:
            data = f.read()
        return hashlib.sha384(data)
    def sha512(filename):
        with open(filename, 'rb') as f:
            data = f.read()
        return hashlib.sha512(data)
    file = sys.argv[2]
    try:
        if opinion == "-md5":
            data2 = md5(file)
            print(data2.hexdigest())
        elif opinion == "-sha1":
            data2 = sha1(file)
            print(data2.hexdigest())
        elif opinion == "-sha256":
            data2 = sha256(file)
            print(data2.hexdigest())
        elif opinion == "-sha384":
            data2 = sha384(file)
            print(data2.hexdigest())
        elif opinion == "-sha224":
            data2 = sha224(file)
            print(data2.hexdigest())
        elif opinion == "-sha512":
            data2 = sha256(file)
            print(data2.hexdigest())
        elif opinion == "--help":
            print(help)
        elif opinion == "-h":
            print(help)
        elif opinion == "-help":
            print(help)
    except(FileNotFoundError):
        print("No file named", sys.argv[2], "in this directory")
except:
    print(help2)    
