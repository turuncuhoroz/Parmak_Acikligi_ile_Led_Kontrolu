int ledpin=2;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(ledpin,OUTPUT);
}

void loop() {
  if(Serial.available()>0)
  {
    char command=Serial.read();

    if(command == 'A')
    {
      analogWrite(ledpin,255);
    }
    else if(command == 'B')
    {
      analogWrite(ledpin,220);
    }
    else if(command == 'C')
    {
      analogWrite(ledpin,180);
    }
    else if(command == 'D')
    {
      analogWrite(ledpin,100);
    }
    else if(command == 'E')
    {
      analogWrite(ledpin,60);
    }
    else if(command == 'F')
    {
      analogWrite(ledpin,30);
    }
    else if(command == 'G')
    {
      analogWrite(ledpin,0);
    }
  }

}
