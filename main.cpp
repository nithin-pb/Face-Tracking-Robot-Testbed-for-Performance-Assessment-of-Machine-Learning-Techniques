#include <Arduino.h>
#include <Servo.h>

Servo head;
Servo neck;
Servo hand;
Servo leg;
Servo foot;

int pos = 90;
int pos1 = 0;
int pos2 = 0;
int pos3 = 0;
int pos4 = 0;
int x, y, h, l, f,a, b, c, d, e, preX, preY, preH, preL, preF, preA, preB, preC, preD, preE;
int prevalue;
//prototypes
int startCall();
int moveServo(int x, int y, int h, int l, int f);
int trajectory(int a, int b, int c, int d, int e);
int servoforloop(int currentvalue, Servo servo);

void setup()
{
  head.attach(3);
  neck.attach(5);
  hand.attach(6);
  leg.attach(9);
  //foot.attach(10);

  servoforloop(60,head);
  servoforloop(35,neck);
  servoforloop(35,hand);
  delay(3000);
  startCall();
  Serial.begin(115200);
}

void loop()
{
  if (Serial.available() > 0)
  {
    if (Serial.read() == 'X')
    {
      x = Serial.parseInt();
      //Serial.print(x);
      if (Serial.read() == 'Y')
      {
        y = Serial.parseInt();
        //Serial.print(y);
        if (Serial.read() == 'H')
        {
          h = Serial.parseInt();
          //Serial.print(h);
          if (Serial.read() == 'L')
          {
            l = Serial.parseInt();
            //Serial.print(l);
            if (Serial.read() == 'F')
            {
              f = Serial.parseInt();
              //Serial.print(f);
              moveServo(x,y,h,l,f);
            }
          }
        }
      }
    }
//trajectory planning in elseif loop in case of error remove the lines.

    else
      {
        a = Serial.parseInt();
        if (Serial.read() == 'B')
        {
          b = Serial.parseInt();
          if (Serial.read() == 'C')
          {
            c = Serial.parseInt();
            if (Serial.read() == 'D')
            {
              d = Serial.parseInt();
              if (Serial.read() == 'E')
              {
                e = Serial.parseInt();
                trajectory(a,b,c,d,e);
              }
            }

          }
        }
      }
    while (Serial.available() > 0)
    {
      Serial.read();
    }
  }
}

int startCall()
{
  for (pos = 60; pos <= 140; pos += 1)
  {

    head.write(pos);
    delay(15);
  }
  for (pos1 = 0; pos1 <= 35; pos1 += 1)
  {

    neck.write(pos1);
    delay(15);
  }

  for (pos2 = 3; pos2 <= 35; pos2 += 1)
  {

    hand.write(pos2);
    delay(15);
  }

  for (pos = 140; pos >= 60; pos -= 1)
  {
    head.write(pos);
    delay(15);
  }
  for (pos1 = 35; pos1 >= 0; pos1 -= 1)
  {
    neck.write(pos1);
    delay(15);
  }

  for (pos2 = 35; pos2 >= 3; pos2 -= 1)
  {

    hand.write(pos2);
    delay(15);
  }
  for (pos = 60; pos <= 90; pos += 1)
  {

    head.write(pos);
    delay(15);
  }
  return 0;
}

int moveServo(int x, int y, int h, int l, int f) //face tracking servo movement
{
  if (preX != x || preY != y || preH != h || preL != l || preF != f)
  {
    Serial.print("\n");
    Serial.print("[INFO] x value \t");
    Serial.print(x);
    Serial.print("\n");
    Serial.print("[INFO] x value \t");
    Serial.print(y);
    Serial.print("\n");
    Serial.print("[INFO] x value \t");
    Serial.print(h);
    Serial.print("\n");
    Serial.print("[INFO] x value \t");
    Serial.print(l);
    Serial.print("\n");
    Serial.print("[INFO] x value \t");
    Serial.print(f);
    Serial.print("\n");
    Serial.print("\n");

    servoforloop(x,head);
    servoforloop(y,neck);
    servoforloop(h,hand);
    servoforloop(l,leg);
    servoforloop(f,foot);

    preX = x;
    preY = y;
    preH = h;
    preL = l;
    preF = f;
    Serial.print("loop complete");
  }
  return 0;
}
int trajectory(int a, int b, int c, int d, int e) //trajectory planning servo movement
{
    if (preA != a || preB != b || preC != c || preD != d || preE != e)
    {

      //hval=
      //lval=
      //fval=
      Serial.print("\n");
      Serial.print("[INFO] a value \t");
      Serial.print(a);
      Serial.print("\n");
      Serial.print("[INFO] b value \t");
      Serial.print(b);
      Serial.print("\n");
      Serial.print("[INFO] c value \t");
      Serial.print(c);
      Serial.print("\n");
      Serial.print("[INFO] d value \t");
      Serial.print(d);
      Serial.print("\n");
      Serial.print("[INFO] x value \t");
      Serial.print(e);
      Serial.print("\n");
      Serial.print("\n");
      servoforloop(a,head);
      servoforloop(b,neck);
      servoforloop(c,hand);
      servoforloop(d,leg);
      servoforloop(e,foot);
      preA = a;
      preB = b;
      preC = c;
      preD = d;
      preE = e;
      Serial.print("trajectory planning complete");
    }
  return 0;
}

int servoforloop(int currentvalue, Servo servo) //for loop for smooth servo movement pass value and servoname
{
  prevalue = servo.read();
  if (prevalue<currentvalue)
  {
    Serial.print("\n");
    for(int i = prevalue;i<currentvalue;i++)
    {
      //dela;
      servo.write(i);
      Serial.print(i);
    }
  }
  else if(currentvalue<prevalue)
  {
    Serial.print("\n");
    for(int i=prevalue;i>currentvalue;i--)
    {
      delay(20);
      servo.write(i);
      Serial.print(i);
    }
  }
  return 0;
}