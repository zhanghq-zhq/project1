import random


class DATA_JYK():

    def data_add(self,count):
        list=[]
        for x in range(count):
            data=random.randint(111111,999999999)
            list.append({"cardNumber":f'{data}'})
        print(len(list))
        return list


if __name__ == '__main__':

    print(DATA_JYK().data_add(10))