import sys
sys.path.insert(0, "./strobe-code/python")

from Strobe.Strobe import Strobe,I,A,C,T,M,K

s = Strobe("bigtest", security=128)

# Just a big number and a big slice of data
big_n = 9823
big_data = [0x34] * big_n
# Run these bad boys through every operation and meta-operation we can
s.ad(big_data, meta_flags=A|M, metadata=big_data)
s.key(big_data, meta_flags=A|C|M, metadata=big_data)
s.send_clr(big_data, meta_flags=A|T|M, metadata=big_data)
s.recv_clr(big_data, meta_flags=I|A|T|M, metadata=big_data)
s.send_enc(big_data, meta_flags=A|C|T|M, metadata=big_data)
s.recv_enc(big_data, meta_flags=I|A|C|T|M, metadata=big_data)
# We have to do meta_recv_mac and recv_mac separately, because if we do it as the ops above, it'll
# panic on meta_recv_mac (which is called inside recv_mac) and never reach the rest of the recv_mac
try: s.operate(I|C|T|M, big_data)
except: pass
try: s.operate(I|C|T, big_data)
except: pass
s.ratchet(big_n, meta_flags=C|M, metadata=big_n)
s.prf(big_n, meta_flags=I|A|C|M, metadata=big_n)
s.send_mac(big_n, meta_flags=C|T|M, metadata=big_n)
print("[{}]".format(', '.join(map("0x{:02x}".format, s.st))))