n = int(input("Enter a number: "))
guess = input("Guess the binary number: ")

input("Not - Reverse every bit in a binary number. press enter.")
print("binary of 12: ", bin(12)[2:])
print("not 12 binary: ", ~12 & 0xFF)

input("XOR gives different bits the value of 1, press enter to continue.")
print("12^10 is: ", 12 ^ 10)

input("Left shift will move all binary numbers to the left and replace the last with a 0.")
print("left shift of: ", n , "<< 1 =", n << 1, "your guess: ", guess)

input("Right shift will move all binary numbers to the right and replace the last with a 0.")
print("Right shift of: ", n , ">> 1 =", n >> 1, "your guess: ", guess)

