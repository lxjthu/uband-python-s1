#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

# For beginner
# 1. variable - num,str,bool
# 2. if
# 3. > < >= <= ==
# 4. print
def main():
  who = '糖小醋的老妈 '
  good_price = 5 #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌
  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  print '%s上街看到了%s, 卖 %d 元/斤' % (who, good_description, good_price)

  if good_price <= reasonable_price:
	 print '她认为便宜'
	 is_cheap = True
	 finalbuy = (reasonable_price - good_price)+2
	 if finalbuy >= 4:
	  print '她买了 4 斤' 
	 else :
		print '她买了 %d 斤' % (finalbuy)
  else:
   print '她认为贵了'
   is_cheap = False
   print '她并没有买，扬长而去'

# run function
if __name__ == '__main__':
  main()