# Anatomy of a keygen!
# A quick lesson in keygen creation for those that always wondered how it's done
# Version 1.0 by MillenniumWare

# This program creates a simple AAA-BBBB format product key. The AAA part is any three digit number
# between 000-999 and isn't 256, 384 or 192. The BBBB part is any four digit number that is between
# 0000-2566 and is divisible by 3. This is a simple example algorithm I created. In the real world,
# often times you'll need to perform revrse engineering of a target program (extremely difficult!),
# or use extensive trial and error to at least figure out enough about it to make your own algorithm
# that puts out keys that work.

# As a disclaimer I must say: Please do not use this knowledge for illegal activities, and I take no responsibility
# if you do use it for illegal purposes and get into trouble. DO NOT blame me, as this has its legit uses too.

import random #imports random library, used for random number generation (we're generating random keys so...)


#Part 1: Generate a random three digit number that meets the above mentioned criteria for the AAA
#portion of the key. This is done by first repeatedly randomizing integers 0-999 until you get one that isn't
# either 192, 256 or 384. Then you add zeros to it if it is less than the required three digits,
# using numerical to string conversion f"{numerical value/variable}"", and store the result to a variable.

excluded_values = {256, 384, 192}  # Set of excluded values

x = random.randint(0, 999) # Generate a random three-digit number

while x in excluded_values: 
    x = random.randint(0, 999) # Keep generating a new number until it meets the criteria

# Now that our integer is saved, let's measure the digit count so we can
# see if it needs any prefixed zeros to make it a three digit number for our key

xlen = len(f"{x}") # Measures length of integer "x" by converting the numerical value into a string and measuring its length 

if xlen == 1: # If it is only one digit, prefix two zeros by adding them alongside the converted numerical-to-string
    AAA = f"00{x}"
elif xlen == 2: # If it is only two digits, prefix one zero by adding it alongside the converted numerical-to-string
    AAA = f"0{x}"
else:           # If it is already three digits, just convert to string 
    AAA = f"{x}"

# Hooray! We now have the AAA portion of our key, let's move on!

# 

# Part 2: Here we need to create a random number that fits the criteria for BBBB as mentioned in the introduction, between 0000-2566
# and divisble by three 

b = False # Set b as False for the random number loop, same purpose as in part 1
while b == False: # Keeps the loop going as long as b is False, same looping as part 1
    y = random.randint(0,2566) # Generate random number between 0-2566
    if y%3 == 0: # Use % (modulus) operator to see if number is divisible by 3 by comparing the remained to zero
        b = True # If divisble by three, end the loop and save the number
    else: # If not, continue and pass back to the start of the loop
        pass


# The following code checks the length of the random condition-fulfilling number and prefixes zeros,
# same as second part of part 1 but souped up for 4 digits
ylen = len(f"{y}")

if ylen == 1: 
    BBBB = f"000{y}"
elif ylen == 2: 
    BBBB = f"00{y}"
elif ylen == 3: 
    BBBB = f"0{y}"
else:           
    BBBB = f"{y}"

# Print out the final key :)

print(f"Your freshly created key: {AAA}-{BBBB}") # Print out the final key :)

# And boom, you've just learnt how a key algorithm can be turned into software that can
# make all the random keys you could desire. Copy protection has long since evolved past
# being able to be exploited with something like this. Making the keygen is the easy part,
# as reverse engineering is increbily difficult even for very skilled hackers as previously mentioned.
