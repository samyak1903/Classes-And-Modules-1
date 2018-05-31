'''Q.3- Create a Temprature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.'''
class Temperature:
    ''' class for temperature conversion from degree celcius to fahrenheit and vice versa'''
    def convertFahrenheit(self,celcius):
        ''' method for converting degree celcius to degree fahreheit'''
        return ((9/5)*celcius)+32
    def convertCelcius(self,fahrenheit):
        ''' method for converting degree fahrenheit to degree celcius'''
        return ((5/9)*fahrenheit)-32
t=Temperature()
choice=int(input("Enter 1 for Celcius to Fahrenheit & 2 for Fahrenheit to Celcius:"))
if choice==1:
    n=float(input("Enter temperature in degree Celcius: "))
    f=t.convertFahrenheit(n)
    print("degree F: ",f) 
elif choice==2:
    n=float(input("Enter temperature in degree Fahrenheit: "))
    c=t.convertCelcius(n)
    print("degree C: ",c) 
else:
    print("Wrong Choice")

