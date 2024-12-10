hour = int(input('please set your work hour: '))
per_hour = int(input('please set your money per hour work: '))

def hoghoogh(hour, per_hour):
    if hour > 8:
        return "oh! too much work!"         
    else:
        jam_hoghoogh = hour * per_hour
        return jam_hoghoogh
    
result = hoghoogh(hour, per_hour)
if isinstance(result, str):
    print(result)
else:
    print('your hoghoogh is :', result)    

