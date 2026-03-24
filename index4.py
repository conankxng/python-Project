import os
os.system('cls')

def main():
        product = int(input('กรุณากรอกจำนวนสินค้าที่ต้องซื้อ :'))
        n = price_type(product)

        print(f'ราคาต่อชิ้นที่ต้องจ่าย {n:,.2f} บาท')
        print(f'ราคารวมทั้งหมด {n*product:,.2f} บาท')

def price_type(product):
    if product>=50:
        n = 80
    elif product<50:
        n = 100
    return n

main()
