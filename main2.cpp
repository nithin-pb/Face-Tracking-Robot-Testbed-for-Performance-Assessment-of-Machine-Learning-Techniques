//header...call function library
#include <Arduino.h>
#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

// User input for servo and position
int UserIn[3]; // raw input from serial buffer, 3 bytes
int ini_byt;   // start byte, begin reading input//initial byte
int servo_num; // which servo to pulse?
int pos;       // servo angle 0-180
int i;         // iterator
int t = 0;
int t1 = 90;
int t2 = 20;
int t3 = 0;
int t4 = 50;
int t5 = 100;
//variable to move to according angle
int s = 0;

void setup()
{
    servo1.attach(3); // Attach each Servo object to a digital pin
    servo2.attach(5);
    servo3.attach(6);
    servo4.attach(9);
    servo5.attach(10);
    servo2.write(20);
    servo4.write(50);
    servo5.write(100);
    Serial.begin(115200); // Open the serial connection, 9600 baud
}

void loop()
{

    if (Serial.available() > 2) // Wait for serial input (min 3 bytes in buffer)
    {
        ini_byt = Serial.read(); // Read the first byte
        if (ini_byt == 255)      // If it's really the startbyte (255) ...
        {
            for (i = 0; i < 2; i++) // ... then get the next two bytes
            {
                UserIn[i] = Serial.read();
            }
            servo_num = UserIn[0]; // First byte = servo to move?
            pos = UserIn[1];       // Second byte = which position?
            if (pos == 255)        // Packet error checking and recovery
            {
                servo_num = 255;
            }

            if (servo_num == 1)
            {
                if (pos == 1)
                {

                    //t1=t1+1;

                    if (t1 > 160)
                    {
                        t1 = 160;
                    }
                    for (int s = 0; s <= 1; s++)
                    {
                        t1 = t1 + s;
                        delay(15);
                        servo1.write(t1);
                    }
                }
                else if (pos == 2)
                {
                    //t1=t1-1;
                    if (t1 < 20)
                    {
                        t1 = 20;
                    }
                    for (int s = 0; s <= 1; s++)
                    {
                        t1 = t1 - s;
                        delay(15);
                        servo1.write(t1);
                    }
                }
            }

            if (servo_num == 2)
            {
                if (pos == 1)
                {
                    t2 = t2 - 1;
                    if (t2 < 0)
                    {
                        t2 = 0;
                    }

                    servo2.write(t2);
                }
                else if (pos == 2)
                {
                    t2 = t2 + 1;
                    if (t2 > 40)
                    {
                        t2 = 40;
                    }

                    servo2.write(t2);
                }
            }

            if (servo_num == 3)
            {
                if (pos == 1)
                {
                    t = t + 2;
                    if (t3 > 90)
                    {
                        t3 = 90;
                    }
                    servo3.write(t);
                }
                else if (pos == 2)
                {
                    t = t - 2;
                    if (t3 < 0)
                    {
                        t3 = 0;
                    }
                    servo3.write(t);
                }
            }

            if (servo_num == 4)
            {
                if (pos == 1)
                {
                    t4 = t4 + 2;
                    if (t4 > 90)
                    {
                        t4 = 90;
                    }
                    servo4.write(t4);
                }
                else if (pos == 2)
                {
                    t4 = t4 - 2;
                    if (t4 < 0)
                    {
                        t4 = 0;
                    }
                    servo4.write(t4);
                }
            }

            if (servo_num == 5)
            {
                if (pos == 1)
                {
                    t5 = t5 + 3;
                    if (t5 > 160)
                    {
                        t5 = 90;
                    }
                    servo5.write(t5);
                }
                else if (pos == 2)
                {
                    t5 = t5 - 3;
                    if (t5 < 0)
                    {
                        t5 = 0;
                    }
                    servo5.write(t5);
                }
            }
        }
    }
}