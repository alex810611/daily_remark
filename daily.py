#讀取檔案
products =[]
with open('products.csv','r') as f :
	for line in f :
		if '商品,價格' in line:
			continue 
		name,price,date = line.strip().split(',') #strip去除\n 再用split ,切割
		products.append([name,price,date])

print(products)

#記帳程式，可存成CSV

products = []

while True :
	name = input('請輸入商品名稱')
	if name == 'q' : #q 離開
		break
	price = input('請輸入商品價格')
	price = int(price)
	date = input('xxxx年,xx月,xx日')

	#p =[]
	#p.append(name)
	#p.append(price)
	#p = [name , price]
	products.append([name,price,date])

for p in products: #列出清單中所有資訊
	print(p[0],'的價格是',p[1],'日期',p[2])


with open ('products.csv' , 'w', encoding = 'utf-8') as f :      #打開檔案
	f.write('商品,價格,日期\n')
	for p in products:                       #for 迴圈
		f.write(p[0] + ',' + str(p[1]) + ',' + p[2]+'\n' )    
