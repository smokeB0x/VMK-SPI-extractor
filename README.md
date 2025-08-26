# VMK-SPI-extractor
Script to extract the TPM header and key from .csv-files generated using the DSview software. 

TPM data must be captured and interpreted using a SPI decoder.

The .csv is then saved using the save button under decoding results and saving the MISO data.

The script takes the last column in the .csv and creates a ong string with the data and then finds the TPM CMK header using regex and extracting the fixed lenght data that comes after - and that is the VMK.
