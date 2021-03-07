from datetime import date

class MyCalendar:
    def __init__(self, *args): 
        data = ''
        self.datas = []
        #print(args)
        for item in args:
            if item in self.datas:
                continue               
            if isinstance(item, date): 
                self.datas.append(item)                
            else: 
                try:
                    data = date(int(str(item).split('/')[2]),int(str(item).split('/')[1]),int(str(item).split('/')[0])) 
                    if data in self.datas:
                        continue
                    else:
                        self.datas.append(data) 
                except:
                    continue
                
    def add_holiday(self, *args):              
        for item in args:  
            if item in self.datas:
                continue          
            if isinstance(item, date):
                self.datas.append(item)                                
            else:
                try:
                    data = date(int(str(item).split('/')[2]),int(str(item).split('/')[1]),int(str(item).split('/')[0]))
                    if data in self.datas:
                        continue
                    else:
                        self.datas.append(data)  
                except:
                    continue                 
           
    def check_holiday(self, *args): 
        for item in args:                        
            if isinstance(item, date): 
                if item in self.datas:
                    return True 
                else:
                    return False                  
            else: 
                try:
                    data = date(int(str(item).split('/')[2]),int(str(item).split('/')[1]),int(str(item).split('/')[0])) 
                    if data in self.datas:
                        return True 
                    else:
                        return False                  
                except:
                    return False                    