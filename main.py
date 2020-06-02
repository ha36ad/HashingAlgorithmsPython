import hashlib
import secrets 
import uuid

#Global constants
X = 0 
SECRET=secrets.tokenhex(16)
#message to encode
message=input("Input a message: ")

#encode the message
encoded_message = message.encode()

#pick your type of hash algorithm
while X == 0:
        hashh = input("Input hash type (SHA-2,SHA-3,BLAKE2): ")
#pick between 256 and 512 bytes
        hash_type = input ("Input byte size (256 or 512): ")
        
        #SHA2
        if hashh == "SHA-2" and hash_type == "256":
                #Combine the hash and secret
                combination = hashlib.sha256(encoded_message).hexdigest()+ SECRET
                print ("Your hash in hexadecimal is:", combination)                
                break
        elif hashh == "SHA-2" and hash_type == "512":
                #Combine the hash and secret
                combination = hashlib.sha512(encoded_message).hexdigest()+ SECRET
                print ("Your hash in hexadecimal is:", combination)                
                break
        
        #SHA3
        elif hashh == "SHA-3" and hash_type == "256":
                #Combine the hash and secret
                combination = hashlib.sha3_256(encoded_message).hexdigest()+ SECRET
                print ("Your hash in hexadecimal is:", combination)
                break
        elif hashh == "SHA-3" and hash_type == "512":
                #Combine the hash and secret
                combination = hashlib.sha3_512(encoded_message).hexdigest()+ SECRET
                print ("Your hash in hexadecimal is:", combination)
                break
            
        #BLAKE2b(256) or BLAKE2s(512)
        elif hashh == "BLAKE2" and hash_type == "256":
                #Combine the hash and secret
                combination = hashlib.blake2s(encoded_message).hexdigest()+ SECRET
                print ("Your hash in hexadecimal is:", combination)
                break
        elif hashh == "BLAKE2" and hash_type == "512":
                #Combine the hash and secret
                combination = hashlib.blake2b(encoded_message).hexdigest()+ SECRET
                print ("Your hash in hexadecimal is:", combination)
                break

        

        
        
