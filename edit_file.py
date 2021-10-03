import sys

if len(sys.argv) != 3:
    print("Requires two arguments: <filename> <\'middle\' or \'end\'>")
    exit(0)
elif not (sys.argv[2] == "middle" or sys.argv[2] == "end"):
    print(sys.argv[2])
    print("Incorrect argument provided. Argument two should be \'middle\' or \'end\'")
    exit(0)

file = sys.argv[1]
with open(file, "rb") as f:
    bytes_arr = []
    byte = f.read(1)
    while byte:
        bytes_arr.append(byte)
        byte = f.read(1)

print("Size of the array is ", len(bytes_arr))

if sys.argv[1] is "middle":
    index = int(len(bytes_arr)/2)
else:
    index = len(bytes_arr) - 1

print(bytes_arr[index])
k = '{0:08b}'.format(ord(bytes_arr[index]))
print(k)

bytes_arr[index] = b'\xaa'
# k1 = '{0:08b}'.format(ord(bytes_arr[middle]))
# print(k1)


with open(file, "rb+") as f:
    for byte in bytes_arr:
        f.write(byte)