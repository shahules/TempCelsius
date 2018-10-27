
# coding: utf-8



#coder:Shahules786 
try:
   import requests
   from bs4 import BeautifulSoup
   from math import floor as f
   from termcolor import colored
except ImportError:
  print("IMPORT ERROR")
  
  
  
try:
   res=requests.get("https://www.msn.com/en-us/weather")
except Exception as e:
  print(colored("No INTERNET","blue"))
  exit(0)
bsobj=BeautifulSoup(res.text,"html.parser")
ftemp=bsobj.find("span",{"class":"current"})
temp=int(ftemp.get_text())
tempc=(temp-32)*5/9
print(colored(str(f(tempc))+"°C","white"))





