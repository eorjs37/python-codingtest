shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    discount_index = 0
    price_index = 0

    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    max_discount_price = 0
    while discount_index < len(coupons) and price_index < len(prices):
        dicount = (100-coupons[discount_index])/100
        max_discount_price += prices[price_index]*dicount
        discount_index+=1
        price_index+=1

    while price_index < len(prices):
        max_discount_price+=prices[price_index]
        price_index += 1

    return max_discount_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))