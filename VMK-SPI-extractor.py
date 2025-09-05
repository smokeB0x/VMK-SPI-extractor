# -*- coding: utf-8 -*-
"""
VMK-SPI-extractor

Created: 26.08.25
Updated: 05.09.25
Version: 1.1

@author: smokeB0x
"""
import sys
import pandas
import re


if len(sys.argv) != 2:                                                                                                                          # Check if the script is used with correct arguments
    print(f"Usage: python3 VMK-SPI-extractor.py file.csv")
    sys.exit(1)

csv_path = sys.argv[1]
df = pandas.read_csv(csv_path)                                                                                                                  # Use pandas to read the .csv into a dataframe (df)                       
miso_data = "".join(df['0:SPI: MISO data'].tolist()).lower()                                                                                    # Add the relevant column into a list in python and then join that list into a single lower case string 
vmk_header_regex = re.compile(r"0{7}12c0{7}1000{7}10[0-6]0{7}1000{7}10[1-9]0{7}1000{7}10[0-1]0{7}1000{7}10[0-5]0{7}1200{7}1000{7}100")          # The regex for the VMK header (here with padding as it appears in the DSview extraction)
                                                                                                                                                # Each byte is padded with a prefix of 4 bytes. The relevant byte 4c looks like this: 000000014c. 

match = vmk_header_regex.search(miso_data)
start_of_vmk = match.end()                                                                                                                      # The start of the vmk is at the end of the header

if match:
    header_padded = match.group()
    header_bytes = [header_padded[i:i+2] for i in range(0, len(header_padded), 2)]
    vmk_header = ''.join(header_bytes[4::5])
    print("VMK header:", vmk_header)


    vmk_padded = miso_data[start_of_vmk:start_of_vmk+32*10]                                                                                      # padded_vmk is the 32x10 bytes after the header
    vmk_bytes = [vmk_padded[i:i+10] for i in range(0, len(vmk_padded), 10)]
    vmk = ''.join(vmk_byte[-2:] for vmk_byte in vmk_bytes)
    print("VMK:", vmk)
    

else:
    print("VMK header not found :(")
    



