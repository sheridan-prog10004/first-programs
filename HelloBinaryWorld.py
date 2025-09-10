#convert 'H' to its number value
hNumValue = ord('H')

#translate the number value into binary
hBinValue = bin(hNumValue)[2:]

#convert 'e' to its number value
eNumValue = ord('e')

#translate the  number value into binary
eBinValue = bin(eNumValue)[2:]

#convert 'l' to its number value
lNumValue = ord('l')

#translate the number value into binary
lBinValue = bin(lNumValue)[2:]

#convert 'o' to its number value
oNumValue = ord('o')

#translate the numver value into binary
oBinValue = bin(oNumValue)[2:]

#print the binary translation
print(hBinValue, eBinValue, lBinValue, lBinValue, oBinValue)

#concatanate all the binary values together using the concatenation (+) operator for strings
binTranslation = hBinValue + ' ' + eBinValue + ' ' + lBinValue + ' ' + lBinValue + ' ' + oBinValue

#output the result
print(binTranslation)

