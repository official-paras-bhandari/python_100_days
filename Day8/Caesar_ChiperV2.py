alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount):
# #     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  

def caesar(start_text,shift_amount,chiper_direction):
    end_text =""
    for letter in start_text:
        position =alphabet.index(letter)
        if(chiper_direction =="decode"):            
            newPostion=position-shift_amount     
            end_text +=alphabet[newPostion]      
        else:
            newPostion=position+shift_amount
            end_text +=alphabet[newPostion]
    print(f"The {chiper_direction}d text is {end_text}")        

caesar(start_text=text, shift_amount=shift,chiper_direction=direction)
    
    
    
   
    
    

