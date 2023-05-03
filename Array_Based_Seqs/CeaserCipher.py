class CeaserCipher:
    """Class for doing encryption and decryption of ceaser cipher criptography"""
    
    def __init__(self, shift):
        """Construct Ceaser Cipher using the given integer shight for rotation"""
        """shift parameter holds the value for the shifting of the character in the list for the
        encryption"""
        #temp array for encryption
        encoder=[None] * 26 #creates a list containing 26 indices with value None

        #temp array for decryption
        decoder=[None] * 26 #creates a list containing 26 indices with value None

        for k in range(26):
            encoder[k]= chr((k+shift) % 26 + ord('A')) #reamainder of index k + value of shift + Unicode integer value of letter A
            # example: 0+3 % 26 + 65 = 3+65 =68 -> which is letter D so we shift letter A 3 places to the left going to the end of the list

            decoder[k]=chr((k-shift) % 26 + ord('A')) #remainder index k - shift value + the UNICODE value of A (65)
            # example: 3-6 % 26 + 65= -3 +65 = 62 

        self._forward=''.join(encoder) # creates a string object from the list encoder
        self._backward=''.join(decoder) # creates a string object from the list decoder 

    def encrypt(self, message):
        """Function that takes the String message object and applies the function forward to shift the elements of the encoder list"""
        """Returns the string representation of the encrypted message"""
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        """Returns the String of the secret which is the encrypted message"""
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Function to perform transformation based on given code string"""
        msg=list(original) #msg becomes a list of the string object orginal containing on each index a character from string object original 

        """for k in length of the list message that takes original message and encrypts and takes secret message and decrypts"""
        for k in range(len(msg)):
            if msg[k].isupper(): # if letter at msg[k] is an Upper case letter
                j= ord(msg[k]) - ord('A') # object j will hold the value of the UNICODE integer of the character at msg[k] minus UNICODE of A which is 65
                msg[k]= code[j] # We then assign to msg[k] the character that is at position j in the list code which is based on the encoder or decoder list from previous functions
                #giving us the list containing the secret message or the original message
        return ''.join(msg) #returns the list msg in a string object
    
if __name__ == '__main__':
    cipher=CeaserCipher(3)
    message= "DIOGO"
    coded=cipher.encrypt(message)
    print('Secret: ', coded)

    answer= cipher.decrypt(coded)
    print('Message: ', answer)
