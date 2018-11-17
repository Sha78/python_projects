#Ch 02   pe12
#Description: This program calculates and displays the transaction of the buying and selling of stocks.

TRANSACTION_COMMISSION_PRICE = .03
INITIAL_PRICE_PER_SHARE = 40
SOLD_SHARE_SALES_PRICE = 42.75
NUMBER_SHARES_BOUGHT = 2000

amount_paid = NUMBER_SHARES_BOUGHT*INITIAL_PRICE_PER_SHARE 
comission_paid_when_bought = amount_paid*TRANSACTION_COMMISSION_PRICE 
amount_received_when_sold = SOLD_SHARE_SALES_PRICE*NUMBER_SHARES_BOUGHT
comission_paid_when_sold = amount_received_when_sold*TRANSACTION_COMMISSION_PRICE
total_commision = comission_paid_when_sold + comission_paid_when_bought

money_left_after_sale_plus_commision = amount_received_when_sold - comission_paid_when_sold - amount_paid

print('\nAmount paid for stocks: $', format(amount_paid, '.2f'))
print('\nCommission paid on stocks when bought: $', format(comission_paid_when_bought, '.2f'))
print('\nGross amount received when sold stocks: $', format(amount_received_when_sold, '.2f'))
print('\nCommission paid on stocks when sold: $', format(comission_paid_when_sold, '.2f'))
print('\nProfit from stock transaction including commission fees: $',format(amount_received_when_sold -amount_paid -total_commision, '.2f'))