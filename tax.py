# các khoản giảm trừ
myselt_gt = 11000000    # bản thân
snpt_gt   = 4400000     # người phụ thuộc
    
# hàm kiểm tra đầu vào
def rangesOK(tncn, snpt):
    if(tncn < 0):
        raise ValueError("Invalid input amount")
    elif(snpt < 0):
        raise ValueError("Invalid input amount of people")
    return True

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
def tax_calculation(tncn, snpt):
    if(rangesOK(tncn, snpt)):
        tntt = tncn - myselt_gt - snpt_gt * snpt
        tax = 0
        if(tntt >= 0):
            tax = tax_calculation_based_on_taxable_income(tntt)
        return tax

