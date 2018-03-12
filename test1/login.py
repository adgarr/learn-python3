status_file_path = '/root/status_file'
init_user_and_passwd = {'user1':'123','user2':'1234','user3':'1234'}

file_pd = open(status_file_path,"r")
status = file_pd.read()
file_pd.close()
if __name__ == "__main__":
    status_list = status.split(' ')
    print("status_list = %s"%status_list)
    count = 0
    while(True):
        user = input("please input user name:")
        #print user
        if user in init_user_and_passwd.keys():
            if user in status_list:
                print('sorry,the user %s is still locked'%user)
                break
            else:
                while(count<3):
                    passwd = input('please input user passwd:')
                    if passwd == init_user_and_passwd[user]:
                        print("*******welcome you!*******")
                        exit()
                    else:
                        print("sorry,the passwd %s is not %s 's  passwd"%(passwd,user))
                        count +=1
                    if count == 3:
                        file_pd = open(status_file_path,"a+")
                        file_pd.write(user+' ')
                        file_pd.close()
                        break

        else:
            print('sorry,the user %s isn not exist'%user)
        if count == 3 :
            break
