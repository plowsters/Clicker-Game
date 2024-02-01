import logging
import math
import random
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

#Calculates how the value of each stock changes over time
def calcStockVal(stockName):
  global trendDownwards
  trendDownwards = False
  global trendUpwards
  trendUpwards = False
  #Produces a random integer from -45 to 45
  x = random.randint(-45, 45)
  #Sets the multiplier to sin((x*pi)/180) + a random
  #float between -1 and 0.11, all rounded to 2 decimal places
  multiplier = round(math.sin(x*math.pi/180) + random.uniform(-1, 0.11), 2)
  tempA = float(Stocks[stockName].replace("$", ""))
  #Prevents stock value from ever being negative or zero
  if tempA - (tempA ** multiplier) <= 0:
    tempA += (tempA ** multiplier)
  #50/50 chance to add or subtract (current stock value)^(multiplier)
  #from the stock. Also checks if a stock is increasing or decreasing
  #too rapidly to set soft upper and lower limits to stock price
  upperThreshold = 1500
  lowerThreshold = 5
  if (tempA >= upperThreshold) or (trendDownwards == 1):
    trendDownwards = True
    ##Gives stock an 80% chance to go down until it reaches $750
    if random.uniform(0, 1) < 0.8:
      tempA -= tempA**multiplier
    else:
      tempA += tempA**multiplier
    if tempA <= 750:
      trendDownwards = False
  elif (tempA <= lowerThreshold) or (trendUpwards == 1):
    trendUpwards = True
    #Gives stock an 80% chance to go up until it reaches $75
    if random.uniform(0, 1) < 0.8:
      tempA += tempA**multiplier
    else:
      tempA -= tempA**multiplier
    if tempA >= 75:
      trendUpwards = False
  else:
    #Gives stock a 50% chance to go up or down if within the
    #upper and lower thresholds
    if random.uniform(0, 1) < 0.5:
      tempA += tempA ** multiplier
    else:
      tempA -= tempA ** multiplier
  return "${:.2f}".format(tempA)

#A function that updates the stock values every second
def updateStocks():
  global stockLabels
  while firstInvest == 0:
    time.sleep(1)
    updateStocks()
  global Stocks
  while True:
    for key in Stocks: 
      Stocks[key] = calcStockVal(key)
    if stockLabels:
      stockLabels[0].config(text="GME: " + Stocks["GME"])
      stockLabels[1].config(text="AAPL: " + Stocks["AAPL"])
      stockLabels[2].config(text="AMZN: " + Stocks["AMZN"])
      stockLabels[3].config(text="TSLA: " + Stocks["TSLA"])
      stockLabels[4].config(text="MSFT: " + Stocks["MSFT"])
    time.sleep(0.5)

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
  tempA = eval(vaultParam.replace('$', '') + " - " + (stockPrice.replace('$', '')))
  cancelTransaction = errorCheck(tempA)
  if cancelTransaction == 0:
    return
  vault = "${:.2f}".format(tempA)
  numShares += 1
  Shares[stockName] = numShares
  firstInvest = True
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

  continuous_thread = threading.Thread(target=updateStocks)
  continuous_thread.start()
  #Set up Game Window
  window = tk.Tk()
  window.title("Your Retirement Fund")
  window.geometry("500x500")
  sFrame1 = Frame(window, bg = "red")
  global stockLabels
  stockLabels = [
    Label(sFrame1, text="GME: " + Stocks["GME"], bg = "red"),
    Label(sFrame1, text="AAPL: " + Stocks["AAPL"], bg = "red"),
    Label(sFrame1, text="AMZN: " + Stocks["AMZN" ], bg = "red"),
    Label(sFrame1, text="TSLA: " + Stocks["TSLA"], bg = "red"),
    Label(sFrame1, text="MSFT: " + Stocks["MSFT"], bg = "red")
  ]
  for label in stockLabels:
    label.pack()
  sFrame1.pack()
  
  w = Canvas(window, width=300, height=200)

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