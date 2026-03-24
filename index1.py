import os
os.system('cls')
def main():
        number = float(input('กรุณากรอกเกรดของตัวเอง :'))
        n = graduate(number)
        print(n)
def graduate(score):
        if score>= 3.6:
            n = '‘ได้เกียรตินิยมอันดับ 1’'      
        elif score >= 3.2:
            n = '‘ได้เกียรตินิยมอันดับ 2’'
        else:
            n = 'ปกติ'
        return n

main()
