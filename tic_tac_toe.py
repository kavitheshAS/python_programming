b={'topl':' ','topm':' ','topr':' ',
          'midl':' ','midm':' ','midr':' ',
          'lowl':' ','lowm':' ','lowr':' '}
def printboard(theboard) :
    print(b['topl']+'|'+b['topm']+'|'+b['topr'])
    print('-+-+-')
    print(b['midl'] + '|' + b['midm'] + '|' + b['midr'])
    print('-+-+-')
    print(b['lowl'] + '|' + b['lowm'] + '|' + b['lowr'])
#les say x starts first
winx=True
turn='x'
while turn=='x':
    print("x's turn to play")
    for i in range(9):
        printboard(b)
        print('turn for '+turn+' ,select!')
        print('move on which space')
        move=input()
        b[move]=turn
        if turn=='x':
          turn='o'
        else:
          turn='x'
printboard(b)
w_comb=[['topl','topm','topr'],['midl','midm','midr'],['lowl','lowm','lowr'],['topl','midl','lowl'],['topm','midm','lowm'],['topr','midr','lowr'],['topl','midm','lowr'],['lowl','midm','topr']]
for i in w_comb:
    if i!='':
     if i=='x':
         winx=True
     else:
         winx=False

     if i=='':
        print('complete the game!')
        break
if winx:
    print('x wins the game')
else:
    print('o wins the game')

printboard(b)












