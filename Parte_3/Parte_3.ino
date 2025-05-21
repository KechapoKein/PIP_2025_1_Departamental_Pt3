const int led1 = 2;
const int led2 = 3;
const int led3 = 4;
const int led4 = 5;
const int sensorLuz = A0;

int estadoLEDs = LOW;
int valorAnterior = -1;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int luz = analogRead(sensorLuz);

  if (luz != valorAnterior) {
    Serial.print("Nivel de luz: ");
    Serial.println(luz);
    valorAnterior = luz;
  }

  if (luz < 500 && estadoLEDs == LOW) {
    estadoLEDs = HIGH;
  } else if (luz > 550 && estadoLEDs == HIGH) {
    estadoLEDs = LOW;
  }

  digitalWrite(led1, estadoLEDs);
  digitalWrite(led2, estadoLEDs);
  digitalWrite(led3, estadoLEDs);
  digitalWrite(led4, estadoLEDs);

  delay(5000);
}