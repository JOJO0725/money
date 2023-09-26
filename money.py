import os

products = []
if os.path.isfile('products.csv'):#檢查檔案是否存在
    print('耶!找到檔案!!')    
    with open ('products.csv','r',encoding = 'utf-8') as pr:#讀取模式
        for line in pr:
            if '商品,價格' in line:
                continue
            goods, price = line.strip().split(',')
            products.append([goods, price])
        print(products)
else:
    print('找不到檔案......')
# 新增商品
while True:
    goods = input('請輸入商品:(q:離開)')
    if goods == 'q':
        break
    elif goods == '':
        goods = input('請輸入商品:(q:離開)')
    price = input('請輸入價格:')
    if price == '':
        price = input('請輸入價格:')
    products.append([goods,price])
print(products)
for p in products:#顯示購物清單
    print(p)
with open('products.csv','w',encoding = 'utf-8') as f:#寫入清單
    f.write('商品,價格,\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '元' + '\n')
