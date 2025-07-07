# random number game 
import random  
secret = random.radint(1,5)
guess = int(input("guess my number (1-5): "))
print("correct!" if guess == secret else f"wrong! It was {secret}" )
