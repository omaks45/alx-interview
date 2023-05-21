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
    n_bytes = 0

    # Mask to check if the most significant bit (8th bit from the left) is set or not
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6
    for num in data:
        # Get the number of set most significant bits in the byte if
        # this is the starting byte of an UTF-8 character.
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1
                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
        else:
           # If this byte is a part of an existing UTF-8 character, then we
           # simply have to look at the two most significant bits and we make
           # use of the masks we defined before.
           if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
        return True
