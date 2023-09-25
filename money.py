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
