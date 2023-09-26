products = []
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
for p in products:
    print(p)
with open('products.csv','w',encoding = 'utf-8') as f:
    f.write('商品,價格,\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '元' + '\n')
