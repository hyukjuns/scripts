import re
import pandas as pd
import openpyxl

# Excel data
raw_data = pd.read_excel('product.xlsx', engine='openpyxl')
print(raw_data)

# Create new column
raw_data['부가세포함'] = raw_data['판매가'] * 1.1
print(raw_data)

# apply > df['컬럼'].apply(함수)
def include_tax(data):
    return data * 1.1

raw_data['부가세포함'] = raw_data['판매가'].apply(include_tax)
print(raw_data)

def select_category(data):
    if re.search('Chair', str(data)):
        return 'Chair'
    elif re.search('Table', str(data)):
        return 'Table'
    elif re.search('Sofa', str(data)):
        return 'Sofa'
    elif re.search('Mirror', str(data)):
        return 'Mirror'
    else:
        return None

raw_data['카테고리'] = raw_data['상품목록'].apply(select_category)
print(raw_data)