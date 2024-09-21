hex_data = [
    "0x0000 fffd 25",                                 
    "0x0000 fffc 25",                                 
    "0x0000 fffb 26ff fd18 fffd 20ff fd23 fffd 27ff",
    "0x0010 fd24",                                   
    "0x0000 fffe 26ff fb18 fffb 20ff fb23 fffb 27ff", 
    "0x0010 fc24",                                    
    "0x0000 fffa 2001 fff0 fffa 2301 fff0 fffa 2701", 
    "0x0010 fff0 fffa 1801 fff0",                     
    "0x0000 fffa 2000 3338 3430 302c 3338 3430 30ff", 
    "0x0010 f0ff fa23 0053 6f64 6143 616e 3a30 fff0", 
    "0x0020 fffa 2700 0044 4953 504c 4159 0153 6f64", 
    "0x0030 6143 616e 3a30 fff0 fffa 1800 7874 6572", 
    "0x0040 6dff f0",                                 
    "0x0000 fffb 03ff fd01 fffd 22ff fd1f fffb 05ff", 
    "0x0010 fd21",                                    
    "0x0000 fffa 2201 03ff f0",                       
    "0x0000 fffa 2103 fff0 fffb 01ff fd00 fffe 22",   
    "0x0000 fffa 2203 03e2 0304 820f 07e2 1c08 8204", 
    "0x0010 09c2 1a0a 827f 0b82 150f 8211 1082 1311", 
    "0x0020 82ff ff12 82ff ffff f0",                  
    "0x0000 0d0a 4c69 6e75 7820 322e 362e 3338 2d38", 
    "0x0010 2d67 656e 6572 6963 2d70 6165 2028 3a3a", 
    "0x0020 6666 6666 3a31 302e 312e 312e 3229 2028", 
    "0x0030 7074 732f 3130 290d 0a0a 0100 7777 7762", 
    "0x0040 7567 7320 6c6f 6769 6e3a 20",             
    "0x0000 fffd 03ff fc01 fffb 22ff fa22 0301 0000", 
    "0x0010 0362 0304 020f 0500 0007 621c 0802 0409", 
    "0x0020 421a 0a02 7f0b 0215 0f02 1110 0213 1102", 
    "0x0030 ffff 1202 ffff fff0 fffb 1fff fa1f 00b1", 
    "0x0040 0031 fff0 fffd 05ff fb21",                
    "0x0000 fffa 2201 07ff f0",                       
    "0x0000 fffd 01ff fb00 fffc 22",                  
    "0x0000 6c",                                      
    "0x0000 006c",                                    
    "0x0000 65",                                      
    "0x0000 0065",                                    
    "0x0000 76",                                      
    "0x0000 0076",                                    
    "0x0000 65",                                      
    "0x0000 0065",                                    
    "0x0000 6c",                                      
    "0x0000 006c",                                    
    "0x0000 58",                                      
    "0x0000 0058",                                    
    "0x0000 0d",                                      
    "0x0000 01",                                      
    "0x0000 000d 0a50 6173 7377 6f72 643a 20",        
    "0x0000 66",                                      
    "0x0000 74",                                      
    "0x0000 5f",                                      
    "0x0000 77",                                      
    "0x0000 61",                                      
    "0x0000 6e",                                      
    "0x0000 64",                                      
    "0x0000 72",                                      
    "0x0000 7f",                                      
    "0x0000 7f",                                      
    "0x0000 7f",                                      
    "0x0000 4e",                                      
    "0x0000 44",                                      
    "0x0000 52",                                      
    "0x0000 65",                                      
    "0x0000 6c",                                      
    "0x0000 7f",                                      
    "0x0000 4c",                                      
    "0x0000 30",                                      
    "0x0000 4c",                                      
    "0x0000 0d",                                      
    "0x0000 000d 0a",                                 
    "0x0000 01",                                      
    "0x0000 000d 0a4c 6f67 696e 2069 6e63 6f72 7265", 
    "0x0010 6374 0d0a 7777 7762 7567 7320 6c6f 6769", 
    "0x0020 6e3a 20",  
]
for line in hex_data:
    # Skip the address and convert hex values to bytes
    byte_values = []
    for hex_value in line.split()[1:]:
        try:
            value = int(hex_value, 16)
            if 0 <= value <= 255:  # Ensure it's a valid byte
                byte_values.append(value)
        except ValueError:
            continue  # Skip invalid hex values
    
    byte_data = bytes(byte_values)
    try:
        # Decode bytes to string
        decoded_string = byte_data.decode('utf-8', errors='replace')
        
        # Print characters or their ASCII codes for unprintable chars
        for char in decoded_string:
            if char.isprintable():
                print(char, end='')  # Print printable characters
            else:
                print(f'\\x{ord(char):02x}', end='')  # Print hex code for unprintable chars

        print()  # New line for each original line
    except Exception as e:
        print(f"Error decoding line: {e}")
        
        
#\x7f ---? del
# \x0d : Carriage Return (CR)
# \x0d\x0a : Carriage Return followed by Line Feed (CRLF), commonly used as a newline in Windows environments.
# \x01 : Start of Heading (SOH), a control character often used in communication protocols.
# \x0d : Again, Carriage Return (CR).


# ft_wandrNDRelL0L