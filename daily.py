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

for p in products: #列出清單中所有資訊
	print(p[0],'的價格是',p[1])
	

	


print(products)
