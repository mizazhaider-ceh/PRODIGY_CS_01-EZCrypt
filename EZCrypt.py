"""
 EZCrypt - Secure Your Text with Ease!

Developed by: Muhammad Izaz Haider  
Internship Project at: Prodigy InfoTech  
Description: EZCrypt is a simple yet powerful encryption & decryption tool that utilizes the Caesar Cipher Algorithm to encode or decode messages securely.

 How EZCrypt Works:  
This program is based on the Caesar Cipher Algorithm, a type of substitution cipher where each letter in the text is shifted by a fixed number of positions in the alphabet.  
- Encryption: Moves letters forward by a given shift value.  
- Decryption: Moves letters backward by the same shift value to restore the original message.  
- Improvement: Uses `shift % 26` to handle large shift values effectively.

 Why I Built This:  
I created EZCrypt during my internship to apply cryptographic concepts in Python and develop a practical security tool. It helped me understand how encryption algorithms work in real-world applications.

 What I Learned:  
- Cipher Algorithms & Cryptography Basics  
- Python String Manipulation & ASCII Character Handling 
- Handling Large Shift Values Efficiently (`shift % 26`) 
- Enhancing User Experience with Colored Terminal Outputs  
- Debugging & Error Handling for Secure Input Processing  

 My Experience:  
This project was a great way to bridge theory and practice. Working on cryptography and optimizing the algorithm deepened my interest in ethical hacking, cybersecurity, and secure coding.

 Special Thanks:  
A huge thanks to Prodigy InfoTech for providing this incredible internship opportunity. Their mentorship allowed me to explore encryption techniques and improve my problem-solving skills.

"""

print("""\033[33m
/==========================================\\
||  _____ _________                  _    ||
|| | ____|__  / ___|_ __ _   _ _ __ | |_  ||
|| |  _|   / / |   | '__| | | | '_ \\| __| ||
|| | |___ / /| |___| |  | |_| | |_) | |_  ||
|| |_____/____\\____|_|   \\__, | .__/ \\__| ||
||                       |___/|_|         ||
\\==========================================/
\033[0m""")
print("\033[33mWelcome to EZCrypt – Secure Your Text with Ease!\033[0m")
print("\033[32mDeveloped by Muhammad Izaz Haider – A Project from Internship\033[0m")
#=================== Function =========================

# Function to perform encryption or decryption based on the mode/choice
def tool(text,shift,mode): 
    
    result = ""  # Initialize an empty string to store the transformed text
    
    for char in text :
        if 'A' <= char <= 'Z' :
            cipher_char = chr(ord(char)+shift) if mode == 1  else chr(ord(char)-shift)
            if cipher_char > 'Z' :
                cipher_char = chr(ord(cipher_char)-26)
            elif cipher_char < 'A': 
                cipher_char = chr(ord(cipher_char) + 26)
            result += cipher_char # Append the transformed character to the result
           
        elif 'a' <= char <= 'z' :
            cipher_char = chr(ord(char)+shift) if mode ==1 else chr(ord(char)-shift)
            if cipher_char > 'z' :
                cipher_char = chr(ord(cipher_char)-26)
            elif cipher_char < 'a' :  
                cipher_char = chr(ord(cipher_char) + 26)
            result += cipher_char # Append the transformed character to the result 
            
        else:
             result += char  # Special characters unchanged like space,@,# etc 

            
    return result # Return the final encrypted or decrypted text,its based on user choice

#======================== Main Program ===============================

print("\033[34mSelect one option below\033[0m")
print("\n\033[36m1:Encrypt\033[0m")
print("\033[36m2:Decrypt\033[0m")

try:
    choice = int(input("\n\033[32mEnter your choice:\033[0m  "))
    if choice not in [1,2]:
        print("\033[31mWrong Choice Exiting.....\033[0m\n")
        exit()
    #===========   
    text = input("\033[35mEnter your Text:\033[0m   ")
    shift = int(input("\033[35mEnter the shift value:\033[0m  "))
    
    shift = shift % 26 if shift >=0 else (shift % 26) + 26 # Ensures shift remains within the valid range of 0-25 for the Caesar Cipher
    
    result = tool(text,shift,choice)
    print("\n\033[36mThe result is:\033[0m  ",result)
    #===========
except ValueError: # Handle the case where the user enters an invalid (non-numeric) input like ,ab,@,# etc 
    print("\033[31mTotally wrong Input:...........Expected number only ( 1 or 2)\033[0m\n")

#The Project End.........But the Journey Begins









