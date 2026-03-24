import os
os.system('cls')
def main():
        total = float(input('กรุณากรอกยอดขายสินค้า:'))
        discount(total)
def discount(price):
    if price >= 2000:
        net = price - (price * 0.10)
    else:
        net = price - (price * 0.05)

    print(f'ยอดซื้อสินค้า {price:,.2f} บาท')
    print(f'ราคารวมสินค้าที่ได้ส่วนลด {net:,.2f} บาท')
main()
