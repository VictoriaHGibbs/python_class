# code03.py
# A Bit (binary digit) represents the most basic unit of data and can be either 0 or 1.
# it is represented by 2^0
# A Byte consists of 8 bits is 2^3 or 8 bytes. 
# A Kilobyte (KB) is 2^10 bytes or 1024 bytes.
# A Megabyte (MB)  is 2^20 bytes or 1024 kilobytes.
# A Gigabyte (GB) is 2^30 bytes or 1024 megabytes.
# A Terabyte (TB) is 2^40 bytes or 1024 gigabytes.
# Note the ^ means a power raised to the next value.
# 
# Write variables for the bit, byte, kilobyte, megabyte, gigabyte, and terabyte.
# Display each of them. Your output should look like
#
# Bit: 1 (2^0)
# Byte: 8 bytes (2^3)
# Kilobyte: 1024 bytes (2^10)
# Megabyte: 1048576 bytes (2^20)
# Gigabyte: 1073741824 bytes (2^30)
# Terabyte: 1099511627776 bytes (2^40)

bit = (2**0)
byte = (2**3)
kilobyte = (2**10)
megabyte = (2**20)
gigabyte = (2**30)
terabyte = (2**40)

print(f"Bit: {bit} byte (2^0)\nByte: {byte} bytes (2^3)\nKilobyte: {kilobyte} bytes (2^10)\nMegabyte: {megabyte} bytes (2^20)\nGigabyte: {gigabyte} bytes (2^30)\nTerabyte: {terabyte} bytes (2^40)")
