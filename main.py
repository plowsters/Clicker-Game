import logging
import tkinter as tk
from tkinter import *



#invest in a stock
def invest(vault, stockPrice, numShares):
  numShares += 1
  print(numShares)
  tempA = eval(vault.replace('$', '') + " - " + str(stockPrice.replace('$', '')))
  vault = tempA
  print(vault)

#Take your money out of the stock market
def withdraw(vault, stockPrice, numShares):
  numShares -= 1
  tempA = eval(vault.replace('$', '') + " + " + str(stockPrice.replace('$', '')))
  vault = tempA

def insidertrade(numClicks):
  numClicks += 1
  logging.info(numClicks)


def main():

  #Money storage
  vault = "${:.2f}".format(100.0)

  numClicks = 0
  
  #Dictionary containing the names and initial values of stocks
  Stocks = {
    "GME": "${:.2f}".format(25.0),
    "AAPL": "${:.2f}".format(100.0),
    "AMZN": "${:.2f}".format(500.0),
    "TSLA": "${:.2f}".format(200.0),
    "MSFT": "${:.2f}".format(50.0),
  }

  #Dictionary containing the names of stocks and number of shares owned
  Shares = {
    "GME": 0,
    "AAPL": 0,
    "AMZN": 0,
    "TSLA": 0,
    "MSFT": 0,
  }
  
  #Set up Game Window
  window = tk.Tk()
  window.title("Your Retirement Fund")
  w = Canvas(window, width=400, height=300)
  w.pack()
  #Buy and sell GME stocks
  frame1 = Frame(window)
  frame1.pack( side = TOP )
  investGME = tk.Button(frame1, text = 'Buy GME', fg = 'red', command = lambda: invest(vault, Stocks["GME"], Shares["GME"]))
  investGME.pack( side = TOP)
  divestGME = tk.Button(frame1, text = 'Sell GME', fg = 'blue', command = lambda: withdraw(vault, Stocks["GME"], Shares["GME"]))
  divestGME.pack( side = TOP)
  #Buy and sell AAPL and AMZN stocks
  frame2 = Frame(window)
  frame2.pack( side = LEFT )
  investAAPL = tk.Button(frame2, text = 'Buy AAPL', fg = 'red', command = lambda: invest(vault, Stocks["AAPL"], Shares["AAPL"]))
  investAAPL.pack( side = TOP )
  divestAAPL = tk.Button(frame2, text = 'Sell AAPL', fg = 'blue' , command = lambda: withdraw(vault, Stocks["AAPL"], Shares["AAPL"]))
  divestAAPL.pack( side = TOP )
  investAMZN = tk.Button(frame2, text = 'Buy AMZN', fg = 'red', command = lambda: invest(vault, Stocks["AMZN"], Shares["AMZN"]))
  investAMZN.pack( side = TOP )
  divestAMZN = tk.Button(frame2, text = 'Sell AMZN', fg = 'blue' , command = lambda: withdraw(vault, Stocks["AMZN"], Shares["AMZN"]))
  divestAMZN.pack( side = TOP )
  #Buy and sell TSLA and MSFT stocks
  frame3 = Frame(window)
  frame3.pack( side = RIGHT )
  investTSLA = tk.Button(frame3, text = 'Buy TSLA', fg = 'red', command = lambda: invest(vault, Stocks["TSLA"], Shares["TSLA"]))
  investTSLA.pack( side = TOP)
  divestTSLA = tk.Button(frame3, text = 'Sell TSLA', fg = 'blue', command = lambda: withdraw(vault, Stocks["TSLA"], Shares["TSLA"]))
  divestTSLA.pack( side = TOP)
  investMSFT = tk.Button(frame3, text = 'Buy MSFT', fg = 'red', command = lambda: invest(vault, Stocks["MSFT"], Shares["MSFT"]))
  investMSFT.pack( side = TOP)
  divestMSFT = tk.Button(frame3, text = 'Sell MSFT', fg = 'blue', command = lambda: withdraw(vault, Stocks["MSFT"], Shares["MSFT"]))
  divestMSFT.pack( side = TOP)
  #Insider Trading Button
  itrade = tk.Button(window, text='Insider Trading', height = 5, width = 15, command = lambda: insidertrade(numClicks))
  itrade.pack()
  
  window.mainloop()
  
#Call main() function
main()