product_price= float(input("商品價格是多少元?"))
etf_price= float(input("0050 現在一股多少元?"))

shares = product_price/ etf_price

print(f"這個商品約等於 {shares:.2f}股 0050")