import sys
sys.path.insert(0, "./strobe-code/python")
from Strobe.Strobe import Strobe
s = Strobe("seqtest", security=128)
s.prf(10)
s.ad("Hello")
s.send_enc("World")
s.send_clr("foo")
s.ratchet()
s.recv_clr("bar")
s.recv_enc("baz")
for i in xrange(100):
    s.send_enc("X"*i)
s.prf(123)
s.send_mac()
print("[{}]".format(', '.join(map("0x{:02x}".format, s.st))))