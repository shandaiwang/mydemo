__author__ = 'pld'


def ip2int(ip):
    """
    将ip转化为一个整数
    :param ip: str ipv4
    :return:
    """
    val = 0
    for part in ip.split('.'):
        val = (val << 8) + int(part)
    return val


def int2ip(val):
    """
    将一个整数转化为ipv4
    :param val: int
    :return:
    """
    part1 = str(val >> 24 & 0xff)
    part2 = str(val >> 16 & 0xff)
    part3 = str(val >> 8 & 0xff)
    part4 = str(val & 0xff)
    return part1 + '.' + part2 + '.' + part3 + '.' + part4


ip = '192.168.1.1'
val = ip2int(ip)
print(val)
print(int2ip(val))