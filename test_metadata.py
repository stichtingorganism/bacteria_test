import sys
sys.path.insert(0, "./strobe-code/python")
from Strobe.Strobe import Strobe

I,A,C,T,M,K = 1<<0, 1<<1, 1<<2, 1<<3, 1<<4, 1<<5
s = Strobe("metadatatest", security=128)
m = s.key("key", meta_flags=A|T|M, metadata="meta1")
m += s.prf(10, meta_flags=I|A|C|M, metadata=10)
m += s.send_enc("pt", meta_flags=A|T|M, metadata="meta3")
print("accumulated metadata == [{}]".format(', '.join(map("0x{:02x}".format, m))))
print("state == [{}]".format(', '.join(map("0x{:02x}".format, s.st))))