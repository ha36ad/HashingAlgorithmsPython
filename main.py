import hashlib
import secrets 
import uuid

#Global constants
X = 0 

#message to encode
message=input("Input a message: ")

#encode the message
encoded_message = message.encode()

#pick your type of hash algorithm
while X == 0:
        hashh = input("Input hash type (SHA-2,SHA-3,BLAKE2): ")
        
        #converts from string to bytes, then to hexadecimal
        if hashh == "SHA-2":
                print("Your hash is: ", hashlib.sha256(encoded_message).hexdigest())
                break
        elif hashh == "SHA-3":
                print ("Your hash is ", hashlib.sha3_512(encoded_message).hexdigest())
                break
        elif hashh == "BLAKE2":
                print ("Your hash is ", hashlib.blake2s(encoded_message).hexdigest())
                break
        
        
