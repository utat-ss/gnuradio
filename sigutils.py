'''
Ali Haydaroglu
2018-12-29
Various utility functions for GNURadio and AX.25 processing
'''

def find_all(a_str, sub):
    res = []
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return res
        res.append(start)
        start += len(sub) # use start += 1 to find overlapping matches


def correlate_strings(a,b):
    assert len(a) == len(b)
    str_len = len(a)
    s = 0
    for i in range(str_len):
        if a[i] == b[i]: s+=1
    return s*1.0/(str_len*1.0)

def to_ascii(val, base='hex',  shifted = False,lsb=False):
    bases = {'bin' : 2, 'hex' : 16}
    assert base in bases.keys(), "Input must be binary, hex or integer"
    if base == 'hex':
        val = int(val,16)
        val = '{0:0{1}b}'.format(val,8)
    else: 
        val = str(val)
        if val[:2] == '0b':
            val = val[2:]
        # val is binary string without 0b prefix now
#     print val
    assert len(val) == 8, "Input must be 8 bits or 1 byte"
        
    if lsb:
        val = val[::-1]

    if shifted:
#         if val[7] != '0':
#             print 'WARNING: this might not be shifted!'
        val = '0'+val[:7]
#     print val
    val = int(val,2)
#     print val
    char = chr(val)
    
    return char
            
        
def from_ascii(char, to='hex', shift=False, lsb=False):
    assert to in ('hex', 'bin')
    
    val = ord(char)
    val = '%.7d' % int(bin(val)[2:])
#     print val
    if shift:
        val += '0'
    else:
        val = '0'+val

    if lsb:
        val = val[::-1]
    
    if to =='bin':
        return val
    elif to=='hex':
        return "{0:0{1}X}".format(int(val,2),2)
        
    