import tkinter as tk
from tkinter import *

def invest():
  thirty = 30


def insidertrade():
  forty = 40


def main():

  #Money storage
  vault = "${:.2f}".format(100.0)
  print(vault)

  #Dictionary containing the names and initial values of stocks
  Stocks = {
    "GME": "${:.2f}".format(25.0),
    "AAPL": "${:.2f}".format(100.0),
    "AMZN": "${:.2f}".format(500.0),
    "TSLA": "${:.2f}".format(200.0),
    "MSFT": "${:.2f}".format(50.0),
  }

  print(Stocks.get("GME"))

  
  #Set up Game Window
  window = tk.Tk()
  window.title("Your Retirement Fund")
  w = Canvas(window, width=400, height=300)
  w.pack()
  frame = Frame(window)
  frame.pack( side = LEFT )
  #Insider Trading Button
  itrade = tk.Button(window, text='Insider Trading', height = 5, width = 12, command = insidertrade())
  itrade.pack()
  window.mainloop()
  
#Call main() function
main()