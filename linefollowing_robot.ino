#include <Servo.h>
int ldrpin[8]={A0,A1,A2,A3,A4,A5,A6,A7},minval[8]={1500,1500,1500,1500,1500,1500,1500,1500},ldr,maxval[8]={0,0,0,0,0,0,0,0},value,ldrval[8],avg[8],angle;
float dir;
void calib();
Servo myservo;
void setup() 
{
  Serial.begin(9600);
  myservo.attach(3);
  for (int i=0;i<8;i++)
  {
    pinMode(ldrpin[i],INPUT);
  }
  pinMode(3,OUTPUT);
  digitalWrite(A8,HIGH);
  digitalWrite(A9,LOW);
  digitalWrite(A10,HIGH);
  digitalWrite(A11,LOW);
  digitalWrite(1,LOW);
  digitalWrite(2,LOW);
  calib();
}

void loop() 
{
  float count=0,sum=0;
  analogWrite(4,245);
  analogWrite(5,245);
  for (int i=0;i<8;i++)
  {    
    ldrval[i]=analogRead(ldrpin[i]);
    if (ldrval[i]<avg[i])
    {
      
      count++;
      sum+=i;
    }
  }
  if (count!=0)
  {
    dir=sum/count;
    angle=map(dir,0,7,50,130);
    myservo.write(angle);
  }
  else
  {
    digitalWrite(6,HIGH);
    digitalWrite(7,HIGH);
  }
}

void calib()
{
  for (int i=0;i<100;i++)
  {
    for (int j=0;j<8;j++)
    {
      value=analogRead(ldrpin[j]);
      if (value>maxval[j])
      maxval[j]=value;
      if (value<minval[j])
      minval[j]=value;
      avg[j]=(minval[j]+maxval[j])/2;
    }
    delay(30);
  }
  
  
}

