#! /usr/bin/env python3

from random import randint

# base32 LUT in lowercase
base32 = "0123456789abcdefghijklmnopqrstuv"

# Generate first 3 bits
id_str = base32[randint(0, 7)]

# Generate remaining 125 bits
for i in range(25):
	id_str += base32[randint(0, 31)]

print(id_str)
