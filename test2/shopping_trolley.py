#coding:utf-8
import json
import os

goods = [["iphone1",111],["iphone2",222],["iphone3",333],["iphone4",444],["iphone5",555]]

users_info ={'user1':'1','user2':'2','user3':'3'}

path_dir = "/root/python/user/%s"

user_shopping_info_path = path_dir+"/shopping_info"

def get_history_info(user):
    user_path_dir = path_dir%user
    if not os.path.exists(user_path_dir):
        os.makedirs(user_path_dir)
        return None
    path = user_shopping_info_path%user
    status = os.path.exists(path)
    user_shopping_info_pd = open(path,'r')
    user_shopping_info_bk =user_shopping_info_pd.read()
    if user_shopping_info_bk:
        user_shopping_info_bk2 = json.loads(user_shopping_info_bk)
    else:
        user_shopping_info_bk2 = None
    user_shopping_info_pd.close()
    return user_shopping_info_bk2

def store_shopping_info(user_shopping_history_info):
    user_shopping_history_info_obj = json.dumps(user_shopping_history_info)
    user_shopping_info_pd = open(user_shopping_info_path%user,'w+')
    user_shopping_info_pd.write(user_shopping_history_info_obj)
    user_shopping_info_pd.close()

def get_buyed_goods(user_shopping_history_info):
    print("\033[1;31;40m******buyed goods******* \033[0m")
    for good in user_shopping_history_info['goods']:
        print("\033[1;31;40m %s %s %s \033[0m"%(good,user_shopping_history_info['goods'][good]['num'],user_shopping_history_info['goods'][good]['cost']))

def get_available_money(user_shopping_history_info):
    print("\033[1;31;40m *****you available money : %s \033[0m"%user_shopping_history_info['available_money'])

def print_goods():
    print("\033[1;31;40m *******all goods******** \033[0m")
    for key,good in enumerate(goods):
        print("\033[1;31;40m %s  %s %s \033[0m"%(key,good[0],good[1]))

def shopping(user_shopping_history_info):
    available_money=user_shopping_history_info['available_money']
    while(True):
        choice = input("please input id to by good or input 'q' to exit or input 'm' to get available_money or input 'h' to get history or input 'g' to show goods:")
        if choice.isdigit():
            aa = int(choice)
            if goods[aa][1] > int(available_money):
                print("\033[1;31;40m your avabliy money is not enough to buy %s \033[0m"%goods[aa][0])
            else:
                if goods[aa][0] in user_shopping_history_info['goods'].keys():
                    user_shopping_history_info['goods'][goods[aa][0]]['num']+=1
                    user_shopping_history_info['goods'][goods[aa][0]]['cost']+=goods[aa][1]
                else:
                    user_shopping_history_info['goods'][goods[aa][0]]={'num':1,'num':1,'cost':goods[aa][1]}
                available_money = int(available_money) - int(goods[aa][1])
                user_shopping_history_info['available_money'] = int(user_shopping_history_info['available_money']) - int(goods[aa][1])
                print("\033[1;31;40m you succeed buyed  %s and cost %s \033[0m"%(goods[aa][0],goods[aa][1]))
        elif choice == 'q':
            get_buyed_goods(user_shopping_history_info)
            get_available_money(user_shopping_history_info)
            break
        elif choice =='m':
            get_available_money(user_shopping_history_info)
        elif choice == 'h':
            get_buyed_goods(user_shopping_history_info)
        elif choice == 'g':
            print_goods()
        else:
            print("your input is wrong")
    store_shopping_info(user_shopping_history_info)

def start_shopping(user):
    user_shopping_history_info = get_history_info(user)
    if user_shopping_history_info:
        shopping(user_shopping_history_info)
    else:
        while(True):
            all_money = input("please input your money:")
            print_goods()
            if all_money.isdigit():
                user_shopping_history_info={}
                user_shopping_history_info['goods']={}
                user_shopping_history_info['all_money']=all_money
                user_shopping_history_info['available_money'] = all_money
                shopping(user_shopping_history_info)
                break
            else:
                print("format of money is rong")

if __name__ == "__main__":
    count = 0
    status = False
    while(True):
        user = input("please input user name:")
        if user in users_info.keys():
            while(count<3):
                passwd = input("please input passwd:")
                if passwd == users_info[user]:
                    status = start_shopping(user)
                    exit()
                else:
                    print("the user %s 's passwd is wrong"%user)
                    count += 1
                if count == 3:
                    break
            if status == True:
                print("finished shopping")
                break
        else:
            count += 1
        if count == 3:
            break

