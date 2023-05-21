#!/usr/bin/python3
"""
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you 
only need to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    :type: List[int]
    :rtype: bool
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    #iterate each integer in the array
    for i in data:
        # Get the binary representation. We only need the least significant 8 bits
        # for any given number.
        bin_form = format(i, '#010b')[-8:]
	# process a new UTF-8 character.
        if num_bytes == 0:
            # Get the number of 1s in the beginning of the string.
            for bit in bin_form:
                if bit == '0': break
                num_bytes += 1

                # 1 byte characters
                if num_bytes == 0:
                    continue
                 # Invalid scenarios according to the rules of the problem.
                if num_bytes == 1 or num_bytes > 4:
                    return False
        else:
            # Else, we are processing integers which represent bytes which are a part of
            # a UTF-8 character. So, they must adhere to the pattern `10xxxxxx`.
            if not (bin_form[0] == '1' and bin_form[1] == '0'):
                return False
        num_bytes -= 1
        return True
