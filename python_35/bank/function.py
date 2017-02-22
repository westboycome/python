# author by li
# _*_ coding:utf-8_*_
import json, sys, os, time, shutil
Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_dir)

#定义认证装饰器
def auth(func):
    def wrapper(*args, **kwargs):
        print("请输入卡号和密码")
        f = open(Base_dir+'\data\user_db.txt','r')
        Log_file = open(Base_dir+'\logs\log.txt',encoding='utf-8')
        Bill_log_file = open(Base_dir+'\logs\\bill_log.txt','a+',encoding='utf-8')
        func_name = func.__name__
        Time_formate = '%Y-%m-%d %X'
        start_time = time.strftime(Time_formate,time.localtime())
        user_data = json.load(f)
        count = 0
        while count <3:
            global user_id
            global user_pwd
            user_id = input('请输入你的卡号')
            user_pwd = input('请输入你的密码')
            if user_id in user_data:
                if user_pwd == user_data[user_id]['Password']:
                    Log_file.write(start_time+'卡号%s认证成功!\n'%user_id)
                    Log_file.flush()
                    time.sleep(1)
                    Log_file.close()
                    keywords = func(*args,**kwargs)
                    if func_name == 'repayment' or func_name == 'transfer' or func_name == 'enchashment':
                        Bill_log_file.write(start_time+'卡号'+user_id+'发起'+func_name+'业务，金额为:%s \n '%keywords)
                        Bill_log_file.flush()
                        time.sleep(1)
                        Bill_log_file.close()
                        return keywords
                    else:
                        return keywords
                else:
                    print('卡号或密码不正确！请重新输入！')
                    Log_file.write(start_time+'卡号%s 认证失败'%user_id)
                    Log_file.flush()
                    time.sleep(1)
                    Log_file.close()
                    count +=1
            else:
                print('卡号不存在，请确认！')
            if count == 3:
                print("对不起,您已输错3三次，卡号已锁定！")
                Log_file.write(start_time + ' 卡号 %s 因连续三次验证失败而被锁定！\n' % user_id)
                Log_file.flush()
                time.sleep(1)
                Log_file.close()
        return wrapper

    # 定义菜单函数，根据不同用户显示不通菜单。
    def menu(choice):
        if choice == '2':
            print("请选择服务类别:\n"
                  "1、查询信用额度。\n"
                  "2、信用卡还款。\n"
                  "3、信用卡提现。\n"
                  "4、修改口令。\n"
                  "5、信用卡转账。\n"
                  "6、信用卡账单查询。\n"
                  "7、轻松购物。\n"
                  "8、退出请按q!\n")

