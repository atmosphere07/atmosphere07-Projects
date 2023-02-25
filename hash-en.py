import hashlib

file = input("Enter file name: ")
mod = input("Mod:")

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

try:
    if mod == "md5":
        data2 = md5(file)
    elif mod == "sha1":
        data2 = sha1(file)
    elif mod == "sha256":
        data2 = sha256(file)
    elif mod == "sha384":
        data2 = sha384(file)
    elif mod == "sha224":
        data2 = sha224(file)
    elif mod == "sha512":
        data2 = sha256(file)
    print(data2.hexdigest())
except(NameError):
    print("No mod")
except(FileNotFoundError):
    print("No such file or directory")
