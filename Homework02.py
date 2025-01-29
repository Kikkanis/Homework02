from random import choice

print("hello Bogdan, this is homework 2 from session 5 and 6")
def calculate_net_salary(gross, num_children):

    gross = input("Please tell me your gross salary again sir. This is so the tax authority can be completely sure that we tax you the right amount:")
    gross = int(gross)
    if gross<1000:
        tax_rate = 10
    elif gross<2000:
        tax_rate = 12
    elif gross<4000:
        tax_rate = 14
    elif gross>4000:
        tax_rate = 18

    if gross<2000:
        tax_cut = num_children * 1 # 1% per child
    if gross>2000:
        tax_cut = num_children * 0.5 # 0.5% per child

        final_tax_rate = max(0, tax_rate - tax_cut)

        # Calculate net salary
        salarynet = gross * (1 - final_tax_rate / 100)
        return salarynet
        
try:
        # Read user inputs
        gross_salary = float(input("Enter gross salary: "))
        num_children = int(input("Enter number of children: "))

        # Calculate and print net salary
        net_salary = calculate_net_salary(gross_salary, num_children)
        print(f"After we have taken your money through tax, you will be left with: {net_salary:.2f} We will put your tax money in our pockets mwahahaha")

except ValueError:
        print("Invalid input. Please enter numeric values.")