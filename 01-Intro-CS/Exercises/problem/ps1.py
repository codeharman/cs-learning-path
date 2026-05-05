# Part A Saving for a House

yearly_salary = float(input("Enter your salary: "))
portion_saved = float(input('Enter the portion of salary to save (as a decimal): '))
cost_of_dream_home = float(input('enter the cost of the house: '))
semi_annual_raise = float(input('enter the raise: '))

portion_down_payment = 0.25
amount_saved = 0
r = .05
amount_req = cost_of_dream_home * portion_down_payment

months = 0

while amount_saved < amount_req:
  months += 1
  amount_saved += amount_saved * (r/12)
  amount_saved += portion_saved * (yearly_salary/12)
  if months % 6 == 0:
    yearly_salary += yearly_salary * semi_annual_raise 

print(months)

