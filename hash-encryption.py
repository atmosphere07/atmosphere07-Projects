import hashlib

file = input("name:")

def md5(filename):

    with open(filename, "rb") as f:

        data1 = f.read()

    data2 = hashlib.md5(data1)

    return data.hexdigest()

print md5(file)
