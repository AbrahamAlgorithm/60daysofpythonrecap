#!/usr/bin/python3

#user should enter investment amount and expected interest
inv_amount = input("Enter your investment amount: ")
interest = input("Enter your expected interest: ")

#convert value to float
inv_amount = float(inv_amount)
interest = float(interest)

#convert value to float and round up to 2 digits
interest = float(interest) * .01

#cycle through 10 years using a for loop and range from 0 to 9
for i in range(10):
    inv_amount = inv_amount + (inv_amount * interest)

#print result
print("Investment after 10 years is : {:.2f}".format(inv_amount))
