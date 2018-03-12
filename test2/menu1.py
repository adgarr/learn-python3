menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

num = 0

def do_menu(menu_info,choice=None,flag=True):
    global num
    num +=1
    while(True):
        if flag:
            if choice and num <4:
                print("当前选项'%s' 下的子菜单如下："%choice)
            elif choice and num == 4:
                print("当前选项'%s' 下的公司如下："%choice)
            else:
                print("根菜单如下：")
            if menu_info :
                for one in menu_info:
                    print(one)
            else:
                    print('')
        if menu_info and num < 4:
            choice1 = input("please input choice(b>返回上一级，q>退出，次级名):")
        else:
            choice1 = input("please input choice(b>返回上一级，q>退出):")

        if choice1 in menu_info.keys():
            do_menu(choice=choice1,menu_info=menu_info[choice1])
        elif choice1 == 'b':
            print("返回上一级菜单")
            break
        elif choice1 == 'q':
            print("退出程序")
            exit()
        else:
            flag = False
            print("input error")

    num -=1

if __name__ == "__main__":
    do_menu(menu_info=menu)

