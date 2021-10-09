<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:15a5fd01de3e7ac84d9c2d1e12b9bb88c1f87bffe62b52a4dbb32173bbd888ac
size 1062
=======
#include <Servo.h>
String str;

Servo f1;
Servo f2;
Servo f3;
Servo f4;
Servo f5;
//f2 (5)手指伸長 180
//f3 (6)手指伸長 0
//F4 (9)手指伸長 0
//0 ,10110

void setup()
{
  Serial.begin(9600);
  f1.attach(3);
  f2.attach(5);
  f3.attach(6);
  f4.attach(9);
  f5.attach(10);
}

void loop()
{
  if (Serial.available() > 0)
  {
    str = Serial.readStringUntil('\n');
    if (str == "2")
    {
      Serial.println(2);
      f1.write(180);
      //delay(10);
      f2.write(180);
      f3.write(0);
      f4.write(180);
      f5.write(0);
      //delay(1000);
      //f1.write(180);
      delay(100);
    }
    else if (str == "0")
    {
      Serial.println(0);
      f1.write(180);
      //delay(10);
      f2.write(0);
      f3.write(180);
      f4.write(180);
      f5.write(0);
      delay(100);
    }
    else if (str == "5")
    {
      Serial.println(5);
      f1.write(0);
      f2.write(180);
      f3.write(0);
      f4.write(0);
      f5.write(180);
      delay(100);
    }
  }
}
>>>>>>> 8ec9b73 (first commit)
