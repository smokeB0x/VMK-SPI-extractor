# VMK-SPI-extractor
Script to extract the TPM header and key from .csv-files generated using the DSview software. 



Creating the .csv file:

Using a logical analyzer connect to the following pins of an SPI chip:
MOSI, MISO, CS, CLK

Use DSview to capture data when the computer is booting

Use a generic SPI decoder to decode the data

Under decoding result click save > both MISO and MOSI data > Save to csv

The header and key is in the MISO data, but the MOSI data contains values for the data chunks that is used to filter out the key.
The header and key is sent in chunks of TPM data FIFO. This is represented by MOSI data "80 D4 00 24 00", but there may be TPM STS data being sent "at the same time". This is represented by MOSI data "80 D4 00 18 00".



Usage:
python3 VMK-SPI-extractor.py file.csv

