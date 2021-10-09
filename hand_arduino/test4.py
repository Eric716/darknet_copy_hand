<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:87a24a64aada87ff6994f40f19210c2d906bcbe49a28ae3b27ed1d4f703a10eb
size 1858
=======
import serial
import random
import os
from time import sleep
COM_PORT='COM7';
BUAD_RATES = 9600;
ser = serial.Serial(COM_PORT,BUAD_RATES)
command = 'Taskkill /im PotPlayerMini64.exe /F'
com=[];
for i in range(0,10):
    a.append(-1)
run=0
while run!=2:
 print('輸入1開始 輸入2結束')
 run=input()
 if run == 1:
  os.system('start.mp3')
  sleep(3.5)
  a=move()
  sleep(2)
  os.system(command)
  b=result()
  jug(a,b)
def jug(com,you)
 if com == 0:
  if you == 0:
   print('draw')
   os.system('draw.mp3')
   sleep(3)
   os.system(command)
  if you == 2:
   print('you lose')
   os.system('loss.mp3')
   os.system(command)
  if you == 5:
   print('you win')
   os.system('win.mp3')
   os.system(command)
 if com == 2:
  if you == 2:
   print('draw')
   os.system('draw.mp3')
   sleep(3)
   os.system(command)
  if you == 5:
   print('you lose')
   os.system('loss.mp3')
   os.system(command)
  if you == 0:
   print('you win')
   os.system('win.mp3')
   os.system(command)
 if com == 5:
  if you == 5:
   print('draw')
   os.system('draw.mp3')
   sleep(3)
   os.system(command)
  if you == 0:
   print('you lose')
   os.system('loss.mp3')
   os.system(command)
  if you == 2:
   print('you win')
   os.system('win.mp3')
   os.system(command)
def move()
 com=random.randint(1,3)
 if com==1:
  ser.write(b'0\n')
  return 0
 if com==2:
  ser.write(b'2\n')
  return 2
 if com==3:
  ser.write(b'5\n')
  return 5
def result()   
 with open(r"C:\Users\Jeff\Desktop\tt", 'r') as fh:
  for line in fh:
   pass
   last = line
 if last[1]==':' and last[0]!='\n':
  a.insert(b,line[0]);
  if len(a)==11:
   a.pop();
  k=last[0];
  b=b+1;
  if b >= 10:
   b=1;
  for i in range(0,10):
   if k == a[i]:
   judge=judge+1;
  if judge==10:
   judge=0;
   return k            
>>>>>>> 8ec9b73 (first commit)
