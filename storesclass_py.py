# -*- coding: utf-8 -*-
"""StoresClass.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fJAExTK8vxBTi929TmeqhfuEab8afYLa
"""

class Stores:
  def __init__ (self, item, Target, Aldi, Walmart):
    self.item = item
    self.Target = Target
    self.Aldi = Aldi
    self.Walmart = Walmart

  def get_Target(self):
    return self.Target

  def get_Aldi(self):
    return self.Aldi

  def get_Walmart(self):
    return self.Walmart

  def get_price(self):
    return self.price
  
  def show_list(self, price_data):
	  print("---------------- Groceries ----------------")
	  print("Available items:")
	  for item_number, item_info in price_data.items():
		  item_name = item_info["Item"]
		  print(f"{item_number}: {item_name}")




  def __str__():
    msg = f"Sucessfully added {self.item} to the cart"
    return msg

