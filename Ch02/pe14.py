
def main():
#INPUT
  initial_principle_deposited = float(input("Enter the principal amount that was originally deposited into the account: "))#p
  annual_interest_rate = float(input("Enter the annual interest rate:"))#r
  times_per_year_interest_compounded = int(input("Enter the number of times per year that the interest is compounded:"))#n
  year_account_left_to_gain_interest = int(input("Enter the specified number of years account will be left to gain interest:"))#t
  
  
  answer = calc_money_left_after_years(initial_principle_deposited,annual_interest_rate,times_per_year_interest_compounded,year_account_left_to_gain_interest)
  #OUTPUT
  print("The amount of money left after the specified number of years is: $",format(answer, '.2f'), sep ='')
  
#PROCESS
def calc_money_left_after_years(initial_principle_deposited,annual_interest_rate,times_per_year_interest_compounded,year_account_left_to_gain_interest):

  money_left_after_years = initial_principle_deposited*(1+annual_interest_rate/times_per_year_interest_compounded )**(times_per_year_interest_compounded*year_account_left_to_gain_interest)

  return money_left_after_years


  

main()

