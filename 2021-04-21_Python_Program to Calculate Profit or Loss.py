#Program to Calculate Profit or Loss
#ComputerProgramming Tutor_April 19,2021
cost_price =float(input("Enter Cost Product Price[£]:"))
selling_price =float(input("Enter The Sale Price [£]:"))

if(cost_price> selling_price ):
    PLamt = cost_price - selling_price
    print("Total Loss Amount [£] = {0}".format(PLamt))
elif (selling_price > cost_price):
    PLamt =selling_price - cost_price
    print("Total Profit [£] = {0}".format(PLamt))

else:
    print("No Profit No Loss!!!")

