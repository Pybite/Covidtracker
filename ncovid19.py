import requests as r
from time import sleep
import os
import dialogs

url = "https://covid19api.herokuapp.com/"
data = r.get(url).json()
location = data['confirmed']['locations']


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        sleep(1)





class corona_virus(object):
    def __init__(self, data=data, location=location):
        self.data = data
        self.location = location
        

    def cases(self):
        loc = input('input a Country: ')
        loc = loc.upper()
        
        for i in self.location:
            if i['country_code'] == loc or i['country'] == loc:
                if i['latest'] == 0:
                    pass
                
                elif i['province'] == "nan":
                    print(f"{i['country']} - {i['latest']} cases")
                
                else:
                    print(f"{i['country']} {i['province']} - {i['latest']} cases")


    def deaths(self):
        loc = input("input a Country code: ")
        loc = loc.upper()     
        for i in self.data['deaths']['locations']:
            if i['country'] == loc or i['country_code'] == loc:
                if i['latest'] == 0:
                    pass
                
                elif i['province'] == "nan":
                    print(f"{i['country']} - {i['latest']} deaths -> {i['history']['3/15/20']} <- (before last upload*)")
                
                else:
                    print(f"{i['country']} {i['province']} - {i['latest']} deaths -> {i['history']['3/15/20']} <- (before last upload*)")


    def recovered(self):
        loc = input('Input a country or country code: ')       
        
        for i in self.data['recovered']['locations']:
            if loc == i['country'] or loc == i['country_code']:
                if i['latest'] == 0:
                    pass

                elif i['province'] == "nan":
                    print(f"{i['country']} - {i['latest']} recovered")

                else:
                    print(f"{i['country']} - {i['province']} : {i['latest']} recovered")

                     


def main():
    chk = dialogs.alert('Welcome to Covid-19 Tracker','','Cases','Deaths','Global')

    if chk == 1:
        clear()
        corona_virus().cases()

    elif chk == 2:
        clear()
        corona_virus().deaths()

    elif chk == 3:
        clear()
        print('''Global confirmed cases: [%s]
Global deaths: [%s]
Global recoveries: [%s]''' % (data['latest']['confirmed'], data['latest']['deaths'],data['latest']['recovered']))
 
  # going to fix this ! 
    elif chk == "4":
        clear()
        corona_virus().recovered()





if __name__ == '__main__':
    main()
