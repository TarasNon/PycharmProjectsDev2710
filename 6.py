import datetime
import requests


print(datetime.datetime.now())

response = requests.get('https://google.com')
if 200 <= response.status_code < 300:
    print("site ok")
else:
    print("site not work")

names = open('request.txt', 'w')
names.write('\nchrly')
names.write('\nchrly')
names.write('\nroot')
names.close()


def save_name(name1):
    try:
        names=open('request.txt', 'a')
        names.write('\n' +name1)
        names.close()
    except:
        print("OK")

def open_name(name):
    try:
        names = open('request.txt', 'a')
        names.read('\n', name)

    except:
        print(f"{name}")


open_name("name")
save_name("Ugly")




def div_number(x, y):
   try:
       print ('\n', x/y)
   except BaseException as e:
       print(f"the error {e}")
   except ZeroDivisionError:
       print("You can divide to zero")


div_number(10, 5)
div_number(10, 0)
div_number(10, 3)







