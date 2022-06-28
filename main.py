import random

# of a number
def gen_cisel(cislo):
    return [int(i) for i in str(cislo)]
      
  
# Returns True if number has 
# no duplicate digits 
# otherwise False      
def neDuplicitni(cislo):
    cislo_je = gen_cisel(cislo)
    if len(cislo_je) == len(set(cislo_je)):
        return True
    else:
        return False
  
  
# Generates a 4 digit number 
# with no repeated digits    
def vystup_cisel():
    while True:
        num = random.randint(1000,9999)
        if neDuplicitni(num):
            return num
  
  
# Returns common digits with exact 
# matches (bulls) and the common 
# digits in wrong position (cows)
def pocet_bull_cows(cislo,hadej):
    bull_cow = [0,0]
    cislo_je= gen_cisel(cislo)
    hadej_je = gen_cisel(hadej)
      
    for i,j in zip(cislo_je,hadej_je):
          
        # common digit present
        if j in cislo_je:
          
            # common digit exact match
            if j == i:
                bull_cow[0] += 1
              
            # common digit match but in wrong position
            else:
                bull_cow[1] += 1
                  
    return bull_cow

      
# Secret Code
num = vystup_cisel()
tries =int(input('Enter number of tries: '))
  
# Play game until correct guess 
# or till no tries left
while tries > 0:
    hadej = int(input("Enter your guess: "))
      
    if not neDuplicitni(hadej):
        print("Number should not have repeated digits. Try again.")
        continue
    if hadej < 1000 or hadej > 9999:
        print("Enter 4 digit number only. Try again.")
        continue
      
    bull_cow = pocet_bull_cows(num,hadej)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -=1
      
    if bull_cow[0] == 4:
        print("You guessed right!")
        break
else:
    print(f"You ran out of tries. Number was {num}")
