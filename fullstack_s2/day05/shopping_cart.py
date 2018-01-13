#__author:  "Jing Xu"
#date:  2018/1/13
price = [8000,12000,32,80,1500]
balance = int( input( "Please input your balance:" ) )
msg='''
---- shopping list ----
1. iphoneX	    %d
2. macbookpro   %d
3. coffee	    %d
4. pythonbook	%d
5. bicycle      %d
--------- End ---------
''' % (price[0],price[1],price[2],price[3],price[4])
flag = True
while( flag ):
	print(msg)
	number_topay = int( input("Press the number to add the item into your shopping cart") )
	if ( balance >= price[ number_topay - 1 ] ):
		confirm = input( "Add to shopping cart?[Y/N]" )
		if ( confirm == "Y" or confirm == "y" ):
			balance = balance - price[ number_topay - 1 ]
			print( "Already added into shopping cart" )
	else:
		print( "Insufficient balance" )
	shopping_desire = input( "Still want to buy something?[Y/N]" )
	if ( shopping_desire == "N" or shopping_desire == "n" ):
		flag = False
print( "End" )





































