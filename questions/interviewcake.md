1. Write a function to find the 2nd largest element in a binary search tree. 
2. Reverse a LinkedList
3. Suppose we could access yesterday's stock prices as a list, where:

	The indices are the time in minutes past trade opening time, which was 9:30am local time.
	The values are the price in dollars of Apple stock at that time.
	So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

	Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

	For example:

	```
	stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
	
	get_max_profit(stock_prices_yesterday)
	# Returns 6 (buying for $5 and selling for $11)
	```

	No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).

4. You have a function rand5() that generates a random integer from 1 to 5. Use it to write a function rand7() that generates a random integer from 1 to 7.
