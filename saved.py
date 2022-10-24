def writing(data):
    with open('names.csv','a') as file:
        file.writelines(data)
          
def reading():
    with open('names.csv','r') as file:
        return file.readlines()
    
      
