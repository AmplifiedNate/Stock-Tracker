
 # Stock Tracker
 A Python-based Financial Analysis tool that identifies stock performance by fetching real-time stock prices from Yahoo Finance, which is then processed through graphing historical stock prices, moving day averages, performing Monte Carlo simulations for predicting futures, and comparative analysis through visualization and ranking.

# Features of the Tool
 The Stock Tracker includes multiple features that focus on data processing and data visualization allowing users to better understand raw financial data. These features include:
 1. Ability to fetch historical data from any stock ticker listed on Yahoo Finance, which includes current prices.
 2. Basic arithmetic calculations in finance such as percent changes and moving averages of stock prices.
 3. Visualizes Price history presented as line graph overlaid with moving average.
 4. Conducts Monte Carlo Simulations capped at 1000 max simulations predicting future stock prices across 30 days.
 5. Visualizes Expected stock price, Optimistic (95th percentile) stock price, and Pessimistic (5th percentile stock price).
 6. Ability to store multiple stock data to compare and rank (from best performing to worst).
 7. Visualizes historical performance of multiple stocks overlaid into a single graph.

 # Libraries Used by the Tool
 The following libraries have been used for the data processing and data visualization of the tool:
 1. YFinance - Main source of Financial data and serves as the foundational datapoint of the Tool
 2. Pandas - Processing and Visualization tool used to arrange and sort raw data derived from Yahoo Finance, compute for percent changes, and rolling moving averages
 3. Matplotlib - Primary visualization tool utilized to plot historical stock performance, Monte Carlo predictors, and aggregated stock comparisons
 4. Numpy - Handles the advanced data processing required to perform Monte Carlo simulations focusing on statistical analysis. 
 5. Datetime - Supplementary import to convert dates from standard string form to quantifiable data able to be computed

# Instructions for Responsible and Effective Use
The tool comprises of five (5) stages that allows user to find the necessary data needed
1. Basic Historical Stock Price Tracking
2. Historical Stock Price Visualization
3. Monte Carlo Simulation and Visualization
4. Repeat input for comparative stock analysis
5. Ranking and Visualization for comparing multiple stocks

Users will always begin on the very first function of basic historical stock price tracking, which will serve as the foundation of all analysis conducted by the program moving forward.

Input your desired stock ticker present on Yahoo Finance, note that the program can only look up and analyze one stock at a time.

Input your desired time horizon to reveal the basic information of the stock, including current price and percent change within time horizon.

Due to the inconsistencies of Yahoo finance in collecting data from smaller tickers (for instance, Philippine corporations), users are given an option to view the raw data and validate the information by pressing Y to view and N to proceed to next step.

Users will be asked for an option to view the historical stock price chart overlaid with 50 day moving average. Press Y to view and N to proceed however take note, kindly close the window displaying the table for the program to continue. 

From there, users will be given the option to view the Monte Carlo Simulation which prints the amount of simulations run, expected price, optimistc price, and pessimistic price, along with the visualization table opening automatically. Once again, kindly close the window displaying the table for the program to continue. 

Congratulations! you have analyzed your first stock, however, thankfully, the stock tracker is able to store your searched and analyzed stocks allowing users to loop the stock analysis and compare multiple stocks using the same parameters. 

Simply initiate the stock analysis once more to analyze another stock until you have successfully searched all desired stocks. Press N when asking to add another stock once done to view the rankings and for the visualization tool to automatically open.

Lastly, Close the final visualization table for the comparative analysis for the program to also finish and close.

