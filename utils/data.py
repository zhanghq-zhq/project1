import xlrd





def get_hangshu(datapath):
	wb = xlrd.open_workbook(datapath)
	sh = wb.sheet_by_index(0)
	title=sh.nrows
	return title-1

def get_sheet(datapath,sheet_name):
	wb=xlrd.open_workbook(datapath)
	sh = wb.sheet_by_name(sheet_name)
	title = sh.row_values(0)
	data = []
	for row in range(1, sh.nrows):
		case_data = sh.row_values(row)
		data.append(dict(zip(title, case_data)))
	return data



if __name__ == '__main__':

	a=get_sheet("E:\\project1\\data\\test_data.xls","Sheet1")
	print(a)







# def load_yaml(file_name):
#     file_path = os.path.join(DATA_DIR, file_name)
#     with open(file_path, encoding='utf-8') as f:
#         return yaml.safe_load(f)  # 把yaml文件转为字典格式
#

# if __name__ == '__main__':
#     pass
    # excel = Excel('data.xls')
    # data = excel.get_sheet('添加加油卡')
    # print(data)
    # for case in data:
    #     print(case['TITLE'])
    # data = load_yaml()
    # print(data['test_add_fuel_card'])
