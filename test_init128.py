import sys

sys.path.insert(0, "./strobe-code/python")
from Strobe.Strobe import Strobe
s = Strobe("", security=128)

print("[{}]".format(', '.join(map("0x{:02x}".format, s.st))))
