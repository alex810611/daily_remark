
import os
#讀取檔案
def read_file(filename):
	products = []
	with open(filename,'r', encoding = 'utf-8') as f: #開啟檔案
		for line in f :
			if '商品,價格' in line:
				continue 
			name,price,date = line.strip().split(',') #strip去除\n 再用split ,切割
			products.append([name,price,date])
	return products

#讓使用者輸入
def user_input(products):
	while True :
		name = input('請輸入商品名稱')
		if name == 'q' : #q 離開
			break
		price = input('請輸入商品價格')
		price = int(price)
		date = input('xxxx年,xx月,xx日')
		date =int(date)
		products.append([name,price,date])
	print(products)
	return products

#印出所有購買清單
def print_products(products):
	for p in products: #列出清單中所有資訊
		print(p[0],'的價格是',p[1],'日期',p[2])
	
#寫入CSV檔
def write_file(filename, products):
	with open (filename , 'w', encoding = 'utf-8') as f :      #打開檔案
		f.write('商品,價格,日期\n')
		for p in products:                       #for 迴圈
			f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2])+'\n' )    

#主程式碼
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yes,找到檔案')
		products = read_file(filename)
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
