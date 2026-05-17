import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

stocks = []
def analyze_stock():
    ticker = input("Enter Stock to Analyze: ")
    print("=" * 50)
    test = yf.download(ticker, start = "2023-01-01", end = "2024-03-01")
    if test.empty == True:
       print("Invalid Ticker! Check Yahoo Finance For The Correct Code and Try Again")
       return
    try:
        while True:
          print("=" * 50)
          start_date = input("Enter a start date (YYYY-MM-DD): ")
          start_date_processed = dt.date.fromisoformat(start_date)
          end_date = input("Enter an end date  (YYYY-MM-DD): ")
          end_date_processed = dt.date.fromisoformat(end_date)
          date_delta = (end_date_processed - start_date_processed).days
          if date_delta < 50:
             print(f"Warning! selected date is {date_delta} and is below the 50 day moving average threshold, in order to use matplotlib, use a window of 50 days or more")
          try:
            ticker_processing = yf.download (ticker, start = start_date, end = end_date)
            close_prices = ticker_processing["Close"]
            current_price = close_prices.iloc[-1].item()
            first_price = close_prices.iloc[0].item()
            percent_change = float(((current_price-first_price)/first_price)*100)
            moving_average = close_prices.rolling(window=50).mean()
            daily_returns = close_prices.pct_change()
            mean_return = daily_returns.mean().item()
            standard_deviation_return = daily_returns.std().item()
            simulations = 1000
            forecast_days = 30
            all_simulations = []
            for i in range(simulations):
                price_path = [current_price]
                for day in range(forecast_days):
                    random_return = np.random.normal(mean_return, standard_deviation_return)
                    next_price = price_path[-1]*(1+random_return)
                    price_path.append(next_price)
                all_simulations.append(price_path)
            final_prices = [path[-1] for path in all_simulations]
            expected_price = np.mean(final_prices)
            optimistic_price = np.percentile(final_prices, 95)
            pessimistic_price = np.percentile(final_prices, 5)
            print("=" * 50)
            print("        STOCK ANALYSIS SUMMARY")
            print("=" * 50)
            print(f"Name of Stock Ticker: {ticker}")
            print(f"Current Price of Stock: {current_price: .2f}")
            print(f"Percent Change of Stock: {percent_change: .2f}")
            print("=" * 50)
            if percent_change >= 0:
                print(f"Stock price has therefore increased by {percent_change: .2f}% across a time period of {date_delta} days")
            else:
                print(f"Stock price has therefore decreased by {percent_change: .2f}% across a time period of {date_delta} days")
            data_check = input("Are You Interested in Viewing the Raw Data? (Y/N): ")
            if data_check == "Y":
               print("=" * 50)
               print("             RAW DATA")
               print("=" * 50)
               print (ticker_processing)
            else: 
               pass
            print("=" * 50)
            stocks.append({"ticker": ticker, "percent_change": percent_change, "date_delta": date_delta, "close_prices": close_prices, "start_date": start_date, "end_date": end_date})
            
            chart_check = input("Are You Interested in Viewing the Price Chart? (Y/N): ")
            if chart_check.upper() == "Y":
                print("=" * 50)
                print("          PRICE CHART")
                print("=" * 50)
                print("Close the chart window to continue... Program will not run unless chart is closed")
                print("=" * 50)
                plt.figure(figsize=(12,6))
                plt.plot(close_prices, label=ticker)
                plt.plot(moving_average, label="50 Day Moving Average")
                plt.title(f"Stock Price Tracking for {ticker}")
                plt.xlabel("Date")
                plt.ylabel("USD")
                plt.legend()
                plt.show()

            monte_check = input("Are You Interested in Viewing the Monte Carlo Chart? (Y/N): ")
            
            if monte_check.upper() == "Y":
                print("=" * 50)
                print("MONTE CARLO SIMULATION (30 DAY FORECAST)")
                print("=" * 50)
                print(f"Simulations Run: {simulations}")
                print(f"Expected Price:   {expected_price:.2f}")
                print(f"Optimistic:   {optimistic_price:.2f}")
                print(f"Pessimistic:   {pessimistic_price:.2f}")
                print("=" * 50)
                
                plt.figure(figsize=(12,6))
                for path in all_simulations:
                    plt.plot(path, color="blue", alpha=0.05)
                
                mean_path = [np.mean(day_prices) for day_prices in zip(*all_simulations)]
                plt.plot(mean_path, color="yellow", linewidth=3, alpha=0.95, label="Mean path")
                optimistic_path = [np.percentile(day_prices, 95) for day_prices in zip(*all_simulations)]
                plt.plot(optimistic_path, color="green", linewidth=2, alpha=0.95, label="Optimistic Path")
                pessimistic_path = [np.percentile(day_prices, 5) for day_prices in zip(*all_simulations)]
                plt.plot(pessimistic_path, color="red", linewidth=2, alpha=0.95, label="Pessimistic Path")
                plt.title(f"Monte Carlo Simulation for {ticker}")
                plt.xlabel("Days Forecasted")
                plt.ylabel("USD")
                plt.legend()
                plt.show()

            break
          except:
                print("Invalid Date, Kindly Check Yahoo Finance and Try again.")

    except:
       print("Invalid Ticker! Check Yahoo Finance For The Correct Code and Try Again")


def compare_stocks(stocks):
    print("=" * 50)
    print("       STOCK COMPARISON RANKINGS")
    print("=" * 50) 
    if len(stocks) >= 2:
        ranked = sorted(stocks, key=lambda s: s["percent_change"], reverse=True)
        for index, stock in enumerate(ranked):
           print(f"Rank {index + 1}: {stock['ticker']} | {stock['percent_change']:.2f}% | {stock['date_delta']} days")
        print(f"\nWinner: {ranked[0]['ticker']} with {ranked[0]['percent_change']:.2f}%")
        print(f"Loser: {ranked[-1]['ticker']} with {ranked[-1]['percent_change']:.2f}%")
        print("=" * 50)
        print("Close the chart window to continue!")
        plt.figure(figsize=(12,6))
        for stock in ranked:
            plt.plot(stock["close_prices"].squeeze(), label=stock["ticker"])
        plt.title("Stock Comparison Chart")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.show()
        print("=" * 50)
    else:
        print("Insufficient Stocks to Compare. Add a New Stock and Try Again.")
   
use_again = "Y"
while use_again.upper() == "Y":
   analyze_stock()
   use_again = input("Type (Y) to add another stock: ")
compare = "Y"
while compare.upper() == "Y":
   compare_stocks(stocks) 
   compare = input("Type (Y) to see rankings again: ")
   print("=" * 50)
   print("   Thank you for using Stock Tracker!")
   print("=" * 50)