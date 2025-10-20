"""
TASK 2: STOCK PORTFOLIO TRACKER
File: stock_portfolio_tracker.py
Description: Track stock investments and calculate portfolio value
"""

import csv
from datetime import datetime

def display_available_stocks(stock_prices):
    """Display all available stocks and prices"""
    print("\n" + "=" * 50)
    print("📊 AVAILABLE STOCKS")
    print("=" * 50)
    for stock, price in sorted(stock_prices.items()):
        print(f"  {stock:<8} - ${price:>6.2f}")
    print("=" * 50)

def add_stocks_to_portfolio(stock_prices):
    """Allow user to add stocks to portfolio"""
    portfolio = {}
    
    print("\n📝 Add stocks to your portfolio")
    print("Type 'done' when finished\n")
    
    while True:
        stock_symbol = input("Enter stock symbol: ").upper().strip()
        
        if stock_symbol == 'DONE':
            break
        
        if stock_symbol not in stock_prices:
            print(f"❌ '{stock_symbol}' not found! Please choose from available stocks.\n")
            continue
        
        try:
            quantity = int(input(f"Enter quantity for {stock_symbol}: "))
            
            if quantity <= 0:
                print("❌ Quantity must be greater than 0!\n")
                continue
            
            # Add or update portfolio
            if stock_symbol in portfolio:
                portfolio[stock_symbol] += quantity
                print(f"✅ Added {quantity} more shares of {stock_symbol} (Total: {portfolio[stock_symbol]})\n")
            else:
                portfolio[stock_symbol] = quantity
                print(f"✅ Added {quantity} shares of {stock_symbol}\n")
        
        except ValueError:
            print("❌ Invalid quantity! Please enter a number.\n")
    
    return portfolio

def calculate_portfolio_value(portfolio, stock_prices):
    """Calculate total portfolio value and display summary"""
    
    if not portfolio:
        print("\n⚠️ Your portfolio is empty!")
        return None
    
    print("\n" + "=" * 65)
    print("💼 YOUR PORTFOLIO SUMMARY")
    print("=" * 65)
    print(f"{'Stock':<10} {'Quantity':<12} {'Price/Share':<15} {'Total Value':<15}")
    print("-" * 65)
    
    total_value = 0
    portfolio_details = []
    
    for stock, quantity in sorted(portfolio.items()):
        price = stock_prices[stock]
        stock_value = quantity * price
        total_value += stock_value
        
        print(f"{stock:<10} {quantity:<12} ${price:<14.2f} ${stock_value:<14.2f}")
        portfolio_details.append({
            'stock': stock,
            'quantity': quantity,
            'price': price,
            'value': stock_value
        })
    
    print("-" * 65)
    print(f"{'TOTAL PORTFOLIO VALUE:':<40} ${total_value:>20.2f}")
    print("=" * 65)
    
    return portfolio_details, total_value

def save_portfolio_to_file(portfolio_details, total_value):
    """Save portfolio to CSV and TXT files"""
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save as CSV
    csv_filename = f"portfolio_{timestamp}.csv"
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Stock Symbol', 'Quantity', 'Price per Share', 'Total Value'])
        
        for item in portfolio_details:
            writer.writerow([item['stock'], item['quantity'], item['price'], item['value']])
        
        writer.writerow([])
        writer.writerow(['TOTAL PORTFOLIO VALUE', '', '', total_value])
    
    # Save as TXT
    txt_filename = f"portfolio_{timestamp}.txt"
    with open(txt_filename, 'w') as file:
        file.write("=" * 65 + "\n")
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}\n")
        file.write("=" * 65 + "\n\n")
        
        file.write(f"{'Stock':<10} {'Quantity':<12} {'Price/Share':<15} {'Total Value':<15}\n")
        file.write("-" * 65 + "\n")
        
        for item in portfolio_details:
            file.write(f"{item['stock']:<10} {item['quantity']:<12} ${item['price']:<14.2f} ${item['value']:<14.2f}\n")
        
        file.write("-" * 65 + "\n")
        file.write(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}\n")
        file.write("=" * 65 + "\n")
    
    print(f"\n✅ Portfolio saved successfully!")
    print(f"   📄 CSV file: {csv_filename}")
    print(f"   📄 TXT file: {txt_filename}")

def main():
    """Main function to run stock portfolio tracker"""
    
    # Hardcoded stock prices dictionary
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "GOOGL": 140.25,
        "MSFT": 370.00,
        "AMZN": 145.80,
        "NVDA": 480.30,
        "META": 310.45,
        "NFLX": 425.60
    }
    
    print("=" * 50)
    print("📈 STOCK PORTFOLIO TRACKER")
    print("=" * 50)
    
    display_available_stocks(stock_prices)
    
    portfolio = add_stocks_to_portfolio(stock_prices)
    
    result = calculate_portfolio_value(portfolio, stock_prices)
    
    if result:
        portfolio_details, total_value = result
        
        save_option = input("\n💾 Save portfolio to file? (yes/no): ").lower()
        
        if save_option.startswith('y'):
            save_portfolio_to_file(portfolio_details, total_value)
    
    print("\n✅ Thank you for using Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()