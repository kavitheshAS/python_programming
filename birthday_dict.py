import pprint
#prog to store birthdays
bdlist={'kavi':'sept 18','ash':'apr 1','kas':'sept 1'}
while True:
    print('enter the name:(enter blank to quit)')
    name=input()
    if name=='':
        break
    if name in bdlist:
        print(bdlist[name]+ ' is the birthday of '+name)
    else:
        print('enter their birthday')
        bday=input()
        bdlist[name]=bday
        print('database updated')
pprint.pprint(bdlist)
#the pprint doesnt seem to work



