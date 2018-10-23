
import pymysql

#class shuju():
record_list=[]
id=0
def input_record():
    name=input("请输入姓名：")
    phone_number=input('请输入电话号码：')
    record={'name'=name,'phone_number'=phone_number}

    return record

def add_record():
    record=input_record()
    global id
    id+=1
    record[id]=id
    record_list.append(record)
    return '添加成功'

def query_record(name):
    query_result=[]
    query_ids=[]
    for record in record_list:
        if record['name']==name:
            query_ids.append(record["record_id"])
            query_result.append(record)
    return query_ids,query_result

def delete_record(name):
    query_ids,query_result=query_record(name)

def delete_record(name):
    query_ids,query_result= query_record(name)








    def query_record():

        listtable = [{'姓名'：'张三'，'电话': '12465', 'id': '1'}]




        def change_record():


    def delete_record():


