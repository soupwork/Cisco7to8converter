#cisco7decrypt
#by richard strnad
#2019 oct 26th -retrieved from
# https://github.com/richardstrnad/cisco7decrypt

def decode  (pw):
    print("inside decode method")
   
    salt = 'dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87'
    # The first 2 digits represent the salt index salt[index]
    index = int(pw[:2])
    # The rest of the string is the encrypted password
    enc_pw = pw[2:].rstrip()
    # Split the pw string into the hex chars, each cleartext char is two hex chars
    hex_pw = [enc_pw[i:i+2] for i in range(0, len(enc_pw), 2)]
    # Create the cleartext list
    cleartext = []
    # Iterate over the hex list
    for i in range(0, len(hex_pw)):
        '''
        The current salt index equals the starting index + current itteration
        floored by % 53. This is to make sure that the salt index start at 0
        again after it reached 53.
        '''
        cur_index = (i+index) % 53
        # Get the current salt
        cur_salt = ord(salt[cur_index])
        # Get the current hex char as int
        cur_hex_int = int(hex_pw[i], 16)
        # XOR the 2 values (this is the decryption itself, XOR of the salt + encrypted char)
        cleartext_char = cur_salt ^ cur_hex_int
        # Get the char for the XOR'ed INT and append it to the cleartext List
        cleartext.append(chr(cleartext_char))
    
    #print(''.join(cleartext) ," is inside decode")
    return (''.join(cleartext))
    #   print(decrypt_type7(pw))
    #return("blanktext")

