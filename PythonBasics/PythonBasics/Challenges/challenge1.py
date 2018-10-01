#Create a program that takes an IP address entered at the keyboard and
#prints out the number of segments it contains, and the length of each segment.

#An IP address consists of 4 numbers, separated from each other with a full stop.
#But your program should just count however many are entered
#Examples of the input you may get are:
# 127.0.0.1
# .192.168.0.1
# 10.0.123456.255
# 172.16
# 255

#So your program work even with invalid IP addresses. We're just interested in the number
#of segments and how long each one is.

#Once you have a working program, here are some more suggestions for invalid input to test:
#   .123.45.678.91
#   123.4567.8.9
#   123.156.289.10123456
#   10.10t.10.10
#   12.9.34.6.12.90
#   '' - that is, press enter without typing anything

input_prompt = ("Please enter an IP address. An IP address consists of 4 numbers, "
                "separated from each other with a full stop: ")
ipAddress = input(input_prompt)

if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segment_length = 0

#char = ""
for char in ipAddress:
    if char=='.':
        print("segment {} contains {} characters".format(segment,segment_length))
        segment+=1
        segment_length =0
    else:
        segment_length+=1

#if char!='.':
#    print("segment {} contains {} characters".format(segment,segment_length))
    