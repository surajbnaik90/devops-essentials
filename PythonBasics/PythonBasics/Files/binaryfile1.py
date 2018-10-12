#Create a binary file
with open("binary", "bw") as binary_file:
    for i in range(20):
        binary_file.write(bytes([i]))


#Read a binary file
with open("binary", "br") as binary_file:
    for item in binary_file:
        print(item)


a = 65534
b = 65535

with open("binary2", "bw") as binary_file:
    binary_file.write(a.to_bytes(2, 'big'))
    binary_file.write(b.to_bytes(2, 'big'))


with open("binary2","br") as binary_file:
    c = int.from_bytes(binary_file.read(2),'big')
    d = int.from_bytes(binary_file.read(2),'big')
    print(c)
    print(d)