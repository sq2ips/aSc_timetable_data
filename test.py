from datetime import datetime
from datetime import timedelta

x =datetime(2023, 9, 2)
x=datetime.now()

if(x.strftime('%w') == '0'):
    x=x+timedelta(days=1)
    print("ni")
elif(x.strftime('%w') == '6'):
    print("so")
    x=x+timedelta(days=2)
    
w = x-timedelta(days=x.weekday())
sow = w.strftime("%Y-%m-%d")
eow = (w+timedelta(days=6)).strftime("%Y-%m-%d")
    

    
        
print(sow)
print(eow)