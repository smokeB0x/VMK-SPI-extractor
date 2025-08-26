# VMK-SPI-extractor
Script to extract the TPM header and key from .csv-files generated using the DSview software. 



Creating the .csv file:

Using a logical analyzer connect to the following pins of an SPI chip:
MOSI, MISO, CS, CLK

Use DSview to capture data when the computer is booting

Use a generic SPI decoder to decode the data

Under decoding result click save > MISO data > Save to csv


Usage:
python3 VMK-SPI-extractor.py file.csv

