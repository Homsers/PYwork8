def sorting(number,read,write,sor,t,data):
    while True: 
        d=number()
        if d=='1':
            print(*t(0,read()),sep='\n')    
        elif d=='2':
            print(*t(1,read()),sep='\n')        
        elif d=='3':
            print(*t(2,read()),sep='\n')    
        elif d=='4':
            print(*sor(input('Введите № группы: '),read()),sep='')   
        elif d=='5':
            print(*read(),sep='')
        elif d=='6':
            print(*sor(input('Введите фамилию:'),read()),sep='')    
        elif d=='7':
            write(data())
        elif d=='8':
            print('Завершение работы программы...')        
            break