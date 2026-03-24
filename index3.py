import os
os.system('cls')

def main():
    name = input('กรุณากรอกชื่อพนักงาน: ')
    sales = float(input('กรุณากรอกยอดขายประจำปี: '))
    get_bonus(name, sales)

def get_bonus(name, sales):
    if sales >= 1000000:
        net = 20000
    elif sales >= 500000:
        net = 10000
    else:
        net = 5000

    print(f'ชื่อพนักงาน {name}')
    print(f'โบนัสที่พนักงานได้รับ {net:,.0f} บาท')

main()
