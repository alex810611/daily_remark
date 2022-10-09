products = []

while True :
	name = input('請輸入商品名稱')
	if name == 'q' : #q 離開
		break
	price = input('請輸入商品價格')
	price = int(price)

	#p =[]
	#p.append(name)
	#p.append(price)
	#p = [name , price]
	products.append([name,price])

for p in products: #列出清單中所有資訊
	print(p[0],'的價格是',p[1])


with open ('products.csv' , 'w', encoding = 'utf-8') as f :      #打開檔案
	f.write('商品,價格\n')
	for p in products:                       #for 迴圈
		f.write(p[0] + ',' + str(p[1]) + '\n' )    