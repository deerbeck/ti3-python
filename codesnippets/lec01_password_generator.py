'''In this example, we first import the random module and the string module. 
We then define the length of the password we want to generate (in this case, 12 characters) 
and create separate strings for letters, numbers, and symbols using the ascii_letters, digits, 
and punctuation constants from the string module, respectively.

Next, we combine all the characters into a single string using the + operator, 
and use the join method and a for loop to select random characters from the combined string 
and build the password one character at a time. Finally, we print the generated password to the console.
'''

import random
import string

# Define the length of the password
password_length = 12

# Define the characters to include in the password
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# Combine the characters into a single string
all_chars = letters + numbers + symbols

# Generate a random password by selecting characters at random
password = ''.join(random.choice(all_chars) for i in range(password_length))

# Print the password
print(f"Your new password is: {password}")