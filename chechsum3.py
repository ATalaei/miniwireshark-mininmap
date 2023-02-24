def header_checksum(header, size):
    cksum = 0
    pointer = 0

    # The main loop adds up each set of 2 bytes. They are first converted to strings and then concatenated
    # together, converted to integers, and then added to the sum.
    while size > 1:
        cksum += int((str("%02x" % (header[pointer],)) +
                      str("%02x" % (header[pointer + 1],))), 16)
        size -= 2
        pointer += 2
    if size:  # This accounts for a situation where the header is odd
        cksum += header[pointer]

    cksum = (cksum >> 16) + (cksum & 0xffff)
    cksum += (cksum >> 16)

    return (~cksum) & 0xFFFF

def cs(data):
    data = data.split()
    data = [int(item,16) for item in data]
    return  "%04x" % (header_checksum(data, len(data)),)


#a="4500002807c3400040060000c0a80108b065349b"
#print(cs(a)+"exampl")