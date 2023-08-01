class BalanceSheet:
    def __init__(self, assets, liabilities, equity):
        self.assets = assets
        self.liabilies = liabilities
        self.equity = equity
    def calculate_total_assets(self):
        return sum(self.assets.values())
    
    def calculate_total_liabilities(self):
        return sum(self.liabilies.values())
    
    def calculate_total_equity(self):
        return sum(self.equity.values())
    
    def calculate_total_liabilities_and_equity(self):
        return self.calculate_total_liabilities() +  self.calculate_total_equity()
    
    def print_balance_sheet(self):

        print("Balance Sheet")
        print("======")
        print("Assets:")
        for asset, value in self.assets.items():
            print(f"{asset}: {value}")
        print("Total Assets:", self.calculate_total_assets())
        print("========>")
        print("Liabilities:")
        for liability, value in self.liabilies.items():
            print(f"{liability}: {value}")
        print("Total Liabilies:", self.calculate_total_liabilities())
        print("========>")
        print("Equity:")
        for equity_item, value in self.equity.items():
            print(f"{equity_item:}: {value}")
        print("Total Equity:", self.calculate_total_equity())
        print("========>")
        print("Total liabilities and Equity:", self.calculate_total_liabilities_and_equity())
assets = {
    "Cash": 5.0,
    "Accounts Receivable": 12.0,
    "inventory": 8,
    "Other Current Assets": 1.0,
    "Total Current Assets": 26.0,
    "Gross PP&E": 277.2,
    "Accumulated Depreciation": 25.0,
    "Net PP$E": 252.2,
    "Other Assets": 0.0,
    "GodsWill": 5.0,
}
libilities = {
    "Acounts Payable": 8.5,
    "Accrued Liabilities": 1.0,
    "Other Current Liabilities": 1.0,
    #"Total Current Liabilities": 11.5,
    "Revolving Credit Facility": 13.3,
    "Term Loan": 180.0,
    "Unsecured Debt": 50.0,
    "Other Liabilities": 1.0,

}

equity = {
    "Retained Earnings": 17.4,
    "Common Stock": 10.0,
}
balance_sheet = BalanceSheet(assets, libilities, equity)
balance_sheet.print_balance_sheet()
        
        

    
