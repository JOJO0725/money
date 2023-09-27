import os
def read_file(filename):
    products = []    
    with open (filename,'r',encoding = 'utf-8') as pr:#讀取模式
        for line in pr:
            if '商品,價格' in line:
                continue
            goods, price = line.strip().split(',')
            products.append([goods, price])
    return products
def add_goods(products):# 新增商品
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
    return products
def display_list(products):#顯示購物清單   
    for p in products:
        print(p)
def write_file(filename,products):        
    with open(filename,'w',encoding = 'utf-8') as f:#寫入清單
        f.write('商品,價格\n')
        for p in products:
            if '元' in p:
                continue
            else:
                f.write(p[0] + ',' + p[1] + '\n')


filename = 'products.csv'
if os.path.isfile(filename):#檢查檔案是否存在
    products = read_file('products.csv')
    print('耶!找到檔案!!')
else:
    print('找不到檔案......')
products = add_goods(products)
display_list(products)
write_file(filename,products)