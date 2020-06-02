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
        if hashh == "SHA-2":
                break
        elif hashh == "SHA-3":
                break
        elif hashh == "BLAKE2":
                break
        
        
