def solution(price):
    priceBoundary_sale = {500000 : 0.8, 300000 : 0.9, 100000 : 0.95, 0 : 1}
    
    for priceBoundary in priceBoundary_sale.keys():
        if price >= priceBoundary:
            return int(price * priceBoundary_sale[priceBoundary])