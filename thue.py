import pandas as pd
# các khoản giảm trừ
myselt_gt = 11000000    # bản thân
snpt_gt   = 4400000     # người phụ thuộc
    
# hàm kiểm tra đầu vào
def rangesOK(tncn, snpt,output):
    checkInput = True
    if(tncn < 0):
        with open(output, "a") as file:
            file.write("Invalid input amount\n")
        checkInput = False
        # raise ValueError("Invalid input amount\n")
    elif(snpt < 0):
        with open(output, "a") as file:
            file.write("Invalid input amount of people\n")
        checkInput = False
        # raise ValueError("Invalid input amount\n")
    return checkInput

# hàm tính thuế dựa trên thu nhập chịu thuế (sau khi trừ các khoản giảm trừ)
def tax_calculation_based_on_taxable_income(tntt):
    tax = 0
    if(tntt >= 0 and tntt <= 5000000):
        tax = tntt * 5 / 100
    elif(tntt <= 10000000):
        tax = tntt * 10 / 100 - 250000
    elif(tntt <= 18000000):
        tax = tntt * 15 / 100 - 750000
    elif(tntt <= 32000000):
        tax = tntt * 20 / 100 - 1650000
    elif(tntt <= 52000000):
        tax = tntt * 25 / 100 - 3250000
    elif(tntt <= 80000000):
        tax = tntt * 30 / 100 - 5850000
    else:
        tax = tntt * 35 / 100 - 9850000
    return int(tax)
        
# hàm tính thuế
def tax_calculation(tncn, snpt,output):
    if(rangesOK(tncn, snpt,output)):
        tntt = tncn - myselt_gt - snpt_gt * snpt
        tax = 0
        if(tntt >= 0):
            tax = tax_calculation_based_on_taxable_income(tntt)
        with open(output, "a") as file:
            file.write(str("{:,.0f}".format(tax)) + "\n")
        return tax

def read_file(path,file_name,sheet):
    # File output rỗng
    output = path + sheet + ".txt"
    with open(output, "w") as file:
        file.write("")
    # Đọc dữ liệu từ file 
    df = pd.read_excel(path + file_name, sheet_name=sheet)
    # Thu nhập cá nhân và số người phụ thuộc
    tncn = df['Thu nhập tháng']
    snpt = df['Số người phụ thuộc']
    # xử lí số 100.000.000
    tncn = [int(v.replace(",","")) if isinstance(v, str) else v for v in tncn]
    for i in range(len(tncn)):
        tax_calculation(tncn[i],int(snpt[i]),output)


# kiểm thử giá trị biên
# đường dẫn đến file excel
your_path = "D:/Zio7/Code/Python/TTNCN/"
file_name = 'Thuế thu nhập cá nhân.xlsx'

sheet_name = 'Kiểm thử giá trị biên'
read_file(your_path,file_name,sheet_name)
sheet_name = 'Kiểm thử lớp tương đương'
read_file(your_path,file_name,sheet_name)
sheet_name = 'Bảng quyết định'
read_file(your_path,file_name,sheet_name)
