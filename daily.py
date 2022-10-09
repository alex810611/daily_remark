products = []

while True :
	name = input('請輸入商品名稱')
	if name == 'q' : #q 離開
		break
	price = input('請輸入商品價格')
	#p =[]
	#p.append(name)
	#p.append(price)
	#p = [name , price]
	products.append([name,price])

	


print(products)
