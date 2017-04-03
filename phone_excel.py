import xlrd


str_first_name = ''

def main():
    start()

def start():
    str_first_name = input('Введите фамилию или q для выхода из программы\n')
    if str_first_name == 'q':
        exit(0)

    str_first_name = str_first_name.title()

    if str_first_name != '':
        catalogue(str_first_name)
    elif str_first_name == '0':
        catalogue(str_first_name)
    else:
        pass

def catalogue(str_first_name):
        rb = xlrd.open_workbook(r'C:\Список телефонов.xls')
        sheet = rb.sheet_by_index(0)
        vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
        for kabinet, otdel, gorod, phone, dolgnost, first_name in vals:
            first_name = first_name.strip()
            if str_first_name == first_name[:1] or str_first_name == first_name[:2] or str_first_name == first_name[:3]:
                kabinet = str(kabinet)
                kabinet = kabinet[:3]
                name = first_name, kabinet, otdel, gorod, int(phone), dolgnost
                print('{} : каб. {} : {} : {} : т. {} : {}'.format(*name))
            elif first_name != str_first_name:
                pass

while True:
    start()

if __name__ == '__main__':
    main()
