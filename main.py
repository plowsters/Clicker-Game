import logging
import threading
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import *

#Money storage
global vault
vault = "${:.2f}".format(100.0)

#number of times "Insider Trading" is clicked
global numClicks
numClicks = 0

#Failsafe for updateStocks() bug
global firstInvest
firstInvest = False
global secondInvest
secondInvest = False

#Dictionary containing the names and initial values of stocks
global Stocks
Stocks = {
  "GME": "${:.2f}".format(25.0),
  "AAPL": "${:.2f}".format(100.0),
  "AMZN": "${:.2f}".format(500.0),
  "TSLA": "${:.2f}".format(200.0),
  "MSFT": "${:.2f}".format(50.0),
}

#Dictionary containing the names of stocks and number of shares owned
global Shares
Shares = {
  "GME": 0,
  "AAPL": 0,
  "AMZN": 0,
  "TSLA": 0,
  "MSFT": 0,
}

##A function that updates the stock values every second
def updateStocks():
  global Stocks
  global firstInvest
  global secondInvest
  global numStocks
  while firstInvest == 1 or secondInvest == 1:
    for key in Stocks: 
      Stocks[key] = eval((Stocks[key].replace('$', '') + " + " + (Stocks[key].replace('$','')))) * 0.1
      Stocks[key] = "${:.2f}".format(Stocks[key])
      print(Stocks[key])
  time.sleep(1)
  updateStocks()

#Checks if the user has enough money to buy the stock
def errorCheck(tempA):
  if float(tempA) >= 0.0:
    return True
  else:
    messagebox.showinfo("Error","You don't have enough money to buy this stock")
    return False

#invest in a stock
def invest(vaultParam, stockPrice, numShares, stockName):
  global vault
  global firstInvest
  global secondInvest
  if vault != "${:.2f}".format(100.0):
    secondInvest = True
  tempA = eval(vaultParam.replace('$', '') + " - " + (stockPrice.replace('$', '')))
  cancelTransaction = errorCheck(tempA)
  if cancelTransaction == 0:
    return
  vault = "${:.2f}".format(tempA)
  numShares += 1
  Shares[stockName] = numShares
  firstInvest = True
  if secondInvest:
    firstInvest = False
  return
  print(vault)

#Take your money out of the stock market
def withdraw(vaultParam, stockPrice, numShares, stockName):
  global vault
  if numShares < 1:
    messagebox.showinfo("Error","You don't own any shares of this stock")
    return
  numShares -= 1
  Shares[stockName] = numShares
  tempA = eval(vaultParam.replace('$', '') + " + " + str(stockPrice.replace('$', '')))
  vault = "${:.2f}".format(tempA)

def insidertrade(clickCounter):
  global numClicks
  clickCounter += 1
  numClicks = clickCounter
  logging.info(numClicks)


def main():

  #Set up Game Window
  window = tk.Tk()
  window.title("Your Retirement Fund")
  window.geometry("500x500")
  sFrame1 = Frame(window, bg = "red")
  GMELabel = Label(sFrame1, text="GME: " + Stocks["GME"], bg = "red")
  GMELabel.pack()
  sFrame1.pack()
  sFrame2 = Frame(window, bg = "red")
  AAPLLabel = Label(sFrame2, text="AAPL: " + Stocks["AAPL"], bg = "red")
  AAPLLabel.pack()
  sFrame2.pack()
  sFrame3 = Frame(window, bg = "red")
  AMZNLabel = Label(sFrame3, text="AMZN: " + Stocks["AMZN"], bg = "red")
  AMZNLabel.pack()
  sFrame3.pack()
  sFrame4 = Frame(window, bg = "red")
  TSLALabel = Label(sFrame4, text="TSLA: " + Stocks["TSLA"], bg = "red")
  TSLALabel.pack()
  sFrame4.pack()
  sFrame5 = Frame(window, bg = "red")
  MSFTLabel = Label(sFrame5, text="MSFT: " + Stocks["MSFT"], bg = "red")
  MSFTLabel.pack()
  sFrame5.pack()
  w = Canvas(window, width=300, height=300)
  
  w.pack(side = TOP )
  #Buy and sell GME stocks
  frame1 = Frame(window)
  investGME = tk.Button(frame1, text = 'Buy GME', fg = 'red', command = lambda: invest(vault, Stocks["GME"], Shares["GME"], "GME"))
  investGME.pack( side = TOP)
  divestGME = tk.Button(frame1, text = 'Sell GME', fg = 'blue', command = lambda: withdraw(vault, Stocks["GME"], Shares["GME"], "GME"))
  divestGME.pack( side = TOP)
  frame1.pack( side = TOP )

  #Buy and sell AAPL and AMZN stocks
  frame2 = Frame(window)
  investAAPL = tk.Button(frame2, text = 'Buy AAPL', fg = 'red', command = lambda: invest(vault, Stocks["AAPL"], Shares["AAPL"], "AAPL"))
  investAAPL.pack( side = TOP )
  divestAAPL = tk.Button(frame2, text = 'Sell AAPL', fg = 'blue' , command = lambda: withdraw(vault, Stocks["AAPL"], Shares["AAPL"], "AAPL"))
  divestAAPL.pack( side = TOP )
  investAMZN = tk.Button(frame2, text = 'Buy AMZN', fg = 'red', command = lambda: invest(vault, Stocks["AMZN"], Shares["AMZN"], "AMZN"))
  investAMZN.pack( side = TOP )
  divestAMZN = tk.Button(frame2, text = 'Sell AMZN', fg = 'blue' , command = lambda: withdraw(vault, Stocks["AMZN"], Shares["AMZN"], "AMZN"))
  divestAMZN.pack( side = TOP )
  frame2.pack( side = RIGHT )

  #Buy and sell TSLA and MSFT stocks
  frame3 = Frame(window)
  investTSLA = tk.Button(frame3, text = 'Buy TSLA', fg = 'red', command = lambda: invest(vault, Stocks["TSLA"], Shares["TSLA"], "TSLA"))
  investTSLA.pack( side = TOP)
  divestTSLA = tk.Button(frame3, text = 'Sell TSLA', fg = 'blue', command = lambda: withdraw(vault, Stocks["TSLA"], Shares["TSLA"], "TSLA"))
  divestTSLA.pack( side = TOP)
  investMSFT = tk.Button(frame3, text = 'Buy MSFT', fg = 'red', command = lambda: invest(vault, Stocks["MSFT"], Shares["MSFT"], "MSFT"))
  investMSFT.pack( side = TOP)
  divestMSFT = tk.Button(frame3, text = 'Sell MSFT', fg = 'blue', command = lambda: withdraw(vault, Stocks["MSFT"], Shares["MSFT"], "MSFT"))
  divestMSFT.pack( side = TOP)
  frame3.pack( side = LEFT )

  #Insider Trading Button
  frame4 = Frame(window)
  itrade = tk.Button(window, text='Insider Trading', height = 5, width = 15, command = lambda: insidertrade(numClicks))
  itrade.pack()
  frame4.pack( side = TOP )
  window.mainloop()

#Call main() function
main()  