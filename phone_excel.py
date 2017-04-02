import xlrd


a = ''

def main():
    start()

def start():
    a = input('Введите фамилию или q для выхода из программы\n')
    if a == 'q':
        exit(0)

    a = a.title()

    if a != '':
        catalogue(a)
    elif a == '0':
        catalogue(a)
    else:
        pass

def catalogue(a):
        rb = xlrd.open_workbook(r'C:\Список телефонов.xls')
        sheet = rb.sheet_by_index(0)
        vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
        for kabinet, otdel, gorod, phone, dolgnost, first_name in vals:
            first_name = first_name.strip()
            if a == first_name[:1] or a == first_name[:2] or a == first_name[:3]:
                kabinet = str(kabinet)
                kabinet = kabinet[:3]
                name = first_name, kabinet, otdel, gorod, int(phone), dolgnost
                print('{} : каб. {} : {} : {} : т. {} : {}'.format(*name))
            elif a != first_name:
                pass

while True:
    start()

if __name__ == '__main__':
    main()
