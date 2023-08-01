def calculate_income_statement(revenue, cost_of_goods_sold, operating_expenses, depreciation, interest_expense,  tax_rate, libor):
  #Calculate Gross Profit
  gross_ptofit = revenue - cost_of_goods_sold

  #Calculate Operating Income
  operating_income = gross_ptofit - operating_expenses

  #Calculate EBIDA
  ebitda = operating_income + depreciation

  #LISBOR

  lisbor = 0.25

  #Calculate Net income before taxes
  net_income_before_taxes = operating_income - interest_expense

  #Clculate Net Income after taxes
  net_income_after_taxes = net_income_before_taxes * (1 - tax_rate)

  #Create and return the income statemate as a dictionary
  income_statement = {
    "revenue": revenue,
    "Cost of Goods sold": cost_of_goods_sold,
    "Operating Expenses": operating_expenses,
    "Operating Income": operating_income,
    "Ebitda": ebitda,
    "Interest Expenses": interest_expense,
    "Net Income Before Taxes":net_income_before_taxes,
    "Net Income After Taxes": net_income_after_taxes
  }
  return income_statement
revenue = 100000
cost_of_goods_sold = 600000
operating_expenses = 200000
depreciation = 4000
interest_expenses = 50000
tax_rate = 0.3
lisbor = 0.25

income_statement_result = calculate_income_statement(revenue, cost_of_goods_sold, operating_expenses, depreciation, interest_expenses, tax_rate, lisbor)
print(income_statement_result)