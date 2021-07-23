

def paixiu(index,list):
    list2 = []
    if index==0:

        for x in range(len(list)):
            list2.append(max(list))
            list.pop(list.index(max(list)))
        print(list2)

    elif index==1:
        for x in range(len(list)):
            list2.append(min(list))
            list.pop(list.index(min(list)))
        print(list2)
    else:
        print("你输入有误，0是降序，1是升序")
paixiu(1,list=[1,34,23,453,5555,2342,534543,46453,238])



def quzhong():
    list1=[1,1,2,2,3,3,4,4,5,5,5,5,5]
    # list2=[]
    # for x in list1:
    #     if x not in list2:
    #
    #         list2.append(x)
    # print(list2) 
    # print(list(enumerate(list1)))
    return list(set(list1))
print(quzhong())




with open(r"C:\Users\Lenovo\Desktop\pytest笔记.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件
    print(data)





s='helloworld'
d=dict()
for x in s:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]=d[x]+1
print(d)

