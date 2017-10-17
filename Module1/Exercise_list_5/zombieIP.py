def verificsIp(ips):
    for ip in ips:
        if int(ip) > 255:
            return False
    return True
ips = open("ips.txt", "r")
valids = open("valids.txt", "w")
invalids = open("invalids.txt", "w")
for line in ips.readlines():
    formatedLine = line.split('.')
    if verificsIp(formatedLine):
        valids.write("%s" %'.'.join(formatedLine))
    else:
        invalids.write("%s" %'.'.join(formatedLine))
ips.close()
valids.close()
invalids.close()
