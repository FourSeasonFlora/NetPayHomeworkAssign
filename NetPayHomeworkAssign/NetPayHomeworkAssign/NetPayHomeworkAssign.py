
#===========================================================
#
#  Title:       Net Pay.py
#  Course:      CPS 120 Section 03
#  Homework:    Two
#  Author:      Lauren Acton
#  Date:        January 19, 2021
#  Description:
#       < Calculated a pay stub with Taxes and Net/Gross Pay>
#
#===========================================================

# Declare and Initialize Variables

HourlyRate = 0
TimeWorked = 0
GrossPay = 0
FederalTax = 0
FICAtax = 0
StateTax = 0
NetPay = 0

# Input 

HourlyRate = float(input("Hourly Rate: "))
TimeWorked = float (input("Time Worked: "))

# Processing Section 

GrossPay =(HourlyRate*TimeWorked) 
FederalTax = (GrossPay*0.15)
FICAtax = (GrossPay*0.0765)
StateTax = (GrossPay*0.0435)
NetPay = (GrossPay - FederalTax - FICAtax - StateTax)

# Output Section

print("\n" * 40)  # This is needed to clear the screen
print("Net Pay Calculator")
print("--------------------------\n")
print()
print("Gross Pay:   ${0:10.2f}".format(GrossPay))
print("Federal Tax: ${0:10.2f}".format(FederalTax))
print("FICA Tax:    ${0:10.2f}".format(FICAtax))
print("State Tax:   ${0:10.2f}".format(StateTax))
print("NetPay:      ${0:10.2f}".format(NetPay))

# End of Application
print("\nThank you")
