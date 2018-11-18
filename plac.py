record_list=[]
record_id=0
def record_input():
    name = input('输入姓名：')
    phone = input('输入电话号码：')
    record={'name':name,'phone':phone}
    return record
def add_record():
    record = record_input()
    global record_id
    record_id += 1
    record['record_id'] = record_id
    record_list.append(record)
    print('添加成功')
    return record_list
    #return '添加成功'
def query_record():
    #query_result=[]
    #query_ids=[]
    if len(record_list) == 0:
        return '不存在'
    else:
        condi = input('请输入查询条件(姓名或电话)：')
        for record in record_list:
            if record['name']==condi:
                #return record['name'],record['phone'],record['record_id']

                return record
                #print(record)
            elif int(record['record_id'])==int(condi):
                #return record['name'],record['phone'],record['record_id']
                return record
                #print(record)
            elif record['phone']==condi:
                #return record['name'],record['phone'],record['record_id']
                return record
                # print(record)
            else:
                return '没有电话记录'
def delete_record():
    if len(record_list)<1:
        return '不存在'
    else :
        decondi=input('请输入删除条件(姓名或电话)：')
        for record in record_list:
            if record['name']==decondi:
                record_list.remove(record)
                print(record_list)
                return '删除成功'
            elif int(record['record_id'])==int(decondi):
                record_list.remove(record)
                print(record_list)
                return '删除成功'
            elif record['phone']==decondi:
                record_list.remove(record)
                print(record_list)
                return '删除成功'
            else:
                return '没有电话记录'
def change_record():
    if len(record_list)>=1:
        record=query_record()
        change=input('请选择修改内容"name"or"phone"：')
        if change in ['name','phone']:
            if change=='name':
                name=input('修改姓名为：')
                record['name']=name
            else:
                change=='phone'
                phone=input('修改手机号为：')
                record['phone']=phone
        else:
            print('不存在')
        print(record_list)
        return record
    else:
        return '不存在'

if __name__=='__main__':
    while True:
        menu="""1.添加，2.查找，3.删除，4.修改，5.退出"""
        print(menu)
        choose=input('请选择操作：')
        if choose=='1':
            print(add_record())
        elif choose=='2':
            print('查询结果：')
            print(query_record())
        elif choose=='3':
            print('删除后的结果：')
            print(delete_record())
        elif choose=='4':
            print(change_record())
            print('修改成功')
        elif choose=='5':
            print('退出')
            break
        else:
            print('无操作')
            continue


