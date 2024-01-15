import hashlib
import sys
import os

help_msg1 = """
Hash-en-sh v1.6
Copyright (c) 2022-2024 by atmosphere07
Homepage: https://github.com/atmosphere07/atmosphere07-Projects
Usage:
    python hash-en-sh.py [Opinion] [File]

Options:
    -md5        calculate MD5 hash value
    -sha1       calculate SHA1 hash value
    -sha224     calculate SHA224 hash value
    -sha256     calculate SHA256 hash value
    -sha384     calculate SHA384 hash value
    -sha512     calculate SHA512 hash value
    -h, --help  display this help
"""

help_msg2 = """
Hash-en-sh v1.6 by atmosphere07
Usage:
    python hash-en-sh.py [OPTION] [FILE]

Use -h or --help option to display the help message.
"""

# use hashlib
HASH_ALGORITHM = {
    "-md5": hashlib.md5,
    "-sha1": hashlib.sha1,
    "-sha224": hashlib.sha224,
    "-sha256": hashlib.sha256,
    "-sha384": hashlib.sha384,
    "-sha512": hashlib.sha512
}

# sys.argv[1, 2]
def parse_args():
    if len(sys.argv) != 3:
        print("Error: Invalid arguments.")
        prin
        
        help_msg2)
        sys.exit(1)
    option = sys.argv[1]
    file_path = sys.argv[2]
    if option not in HASH_ALGORITHM:
        print("Error: Invalid option:", option)
        prin
        
        help_msg2)
        sys.exit(1)
    if not os.path.isfile(file_path):
        print("Error: File not found:", file_path)
        sys.exit(1)
    return option, file_path

# calculate hash
def calculate_hash(option, file_path):
    algorithm = HASH_ALGORITHM[option]
    with open(file_path, 'rb') as f:
        data = f.read()
    return algorithm(data).hexdigest()

# main()
def main():
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        prin
        
        help_msg1)
        sys.exit(0)
    elif len(sys.argv) == 1:
        print("Error: Missing arguments.")
        prin
        
        help_msg2)
        sys.exit(1)

    option, file_path = parse_args()
    hash_value = calculate_hash(option, file_path)
    print(hash_value)

if __name__ == '__main__':
    main()
