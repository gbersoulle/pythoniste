import struct

octets = b"\x00\x00\x00\x2A"

big_endian = struct.unpack("!I", octets)[0]
little_endian = struct.unpack("<I", octets)[0]
inverse_big_endian = struct.unpack("!I", octets[::-1])[0] # Inverser les octets puis lire en big-endian donne le même résultat que lire directement en little-endian

print(f"big-endian (network) : {big_endian}")
print(f"little-endian        : {little_endian}")
print(f"inversé puis big-end : {inverse_big_endian}")

assert little_endian == inverse_big_endian
