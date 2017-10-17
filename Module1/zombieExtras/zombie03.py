speedLimit = 110
speedOfCar = int(input('Enter the speed of the car: '))
if speedOfCar <= speedLimit:
    print("You was not fined. Good trip!")
else:
    speedExceeded = speedOfCar - speedLimit 
    valueOfFine = float(speedExceeded * 5)
    print("You are finded!")
    print("You traffic ticket have a value of R$%.2f" %valueOfFine)
