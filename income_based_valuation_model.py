## Income Based Valuation Model 
# Revenue includes all revenues from the property, including rent.
# Payroll includes all compensation paid (salaries, bonuses, benefits, commissions, property management fees etc.)
# NOI is a before tax figure and is also referred to as EBIT (earnings before income taxes).
# This appears on the income statement and cash flow statement 
# It excludes principle and income payments on debt, capital expenditures, depreciation, and amoritization. 

print("Enter the values for the period (e.g. annually, quarterly, or annual totals) for income based valuation.")
revenue = input("Enter property revenue: " )
payroll = input("Enter salaries and payroll: " )
property_taxes = input("Enter property taxes: " )
insurance = input("Enter insurance costs: " )
rm = input("Enter repair and maintenance costs: " )
r = input("Enter your required rate of return: " )
noi = revenue - float(payroll + insurance + property_taxes + rm)

print()
print("Revenue:", revenue, "Payroll:", payroll, "Insurance:", insurance, "Property Taxes:", 
      property_taxes, "Repairs:", rm, "Required rate of return:", r)
print("Net operating income=",f"${noi:,.2f}")

print()
income_based_valuation_model = noi / r 
print("The value of this property is",f"${income_based_valuation_model:,.2f}")
