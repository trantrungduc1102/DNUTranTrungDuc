#include <ESP32Servo.h>

// ===================== CHÂN CẢM BIẾN KHOẢNG CÁCH =====================
// Cảm biến E18-D80NK dùng tín hiệu digital (chân đen - OUT)
#define SENSOR1_PIN 32  // D32 - Cảm biến 1
#define SENSOR2_PIN 33  // D33 - Cảm biến 2
#define SENSOR3_PIN 25  // D25 - Cảm biến 3

// ===================== CHÂN SERVO =====================
#define SERVO1_PIN 26  // D26 - Servo 1
#define SERVO2_PIN 27  // D27 - Servo 2

#define RELAY_PIN 4  // D27 - Servo 2

String data_receive;
String loai_qua = "";
Servo servo1;
Servo servo2;

int qua_cam_count = 0;
int qua_cachua_count = 0;
int qua_chuoi_count = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(SENSOR1_PIN, INPUT);
  pinMode(SENSOR2_PIN, INPUT);
  pinMode(SENSOR3_PIN, INPUT);
  pinMode(SENSOR3_PIN, INPUT);
  pinMode(RELAY_PIN, OUTPUT);

  // Gắn servo vào chân điều khiển
  servo1.attach(SERVO1_PIN);
  servo2.attach(SERVO2_PIN);

  // Đặt vị trí ban đầu cho servo
  servo1.write(90);  // Trung tâm
  servo2.write(90);  // Trung tâm
}

void loop() {
  // put your main code here, to run repeatedly:
  int cambien1_value = !digitalRead(SENSOR1_PIN);
  int cambien2_value = !digitalRead(SENSOR2_PIN);
  int cambien3_value = !digitalRead(SENSOR3_PIN);

  // Serial.print("Cam bien 1: ");
  // Serial.print(cambien1_value);
  // Serial.print("   ");
  // Serial.print("Cam bien 2: ");
  // Serial.print(cambien2_value);
  // Serial.print("   ");
  // Serial.print("Cam bien 3: ");
  // Serial.print(cambien3_value);
  // Serial.print("   ");
  // Serial.print("Loai qua: ");
  // Serial.print(loai_qua);
  // Serial.println("   ");

  while (Serial.available() > 0) {
    char chr_rec = Serial.read();
    data_receive += chr_rec;

    if (chr_rec == '\n') {
      loai_qua = data_receive.substring(0, 5);
      data_receive = "";
    }
  }



  if (loai_qua == "Loai1") {
    if (cambien2_value) {
      servo1.write(15);
      delay(5000);
      servo1.write(90);
      qua_cam_count += 1;
      String result = "Done, " + String(qua_cam_count) + ", " + String(qua_cachua_count) + ", " + String(qua_chuoi_count);
      Serial.println(result);
      loai_qua = "";

    } else {
      digitalWrite(RELAY_PIN, LOW);
    }
  } else if (loai_qua == "Loai2") {
    if (cambien3_value) {
      servo2.write(15);
      delay(5000);
      servo2.write(90);
      qua_cachua_count += 1;
      String result = "Done, " + String(qua_cam_count) + ", " + String(qua_cachua_count) + ", " + String(qua_chuoi_count);
      Serial.println(result);
      loai_qua = "";

    } else {
      digitalWrite(RELAY_PIN, LOW);
    }
  } else if (loai_qua == "Loai3") {
    digitalWrite(RELAY_PIN, LOW);
    delay(5000);
    qua_chuoi_count += 1;
    String result = "Done, " + String(qua_cam_count) + ", " + String(qua_cachua_count) + ", " + String(qua_chuoi_count);
    Serial.println(result);
    loai_qua = "";

  } else {
    digitalWrite(RELAY_PIN, LOW);
  }

  if (cambien1_value) {
    if (loai_qua == "") {
      digitalWrite(RELAY_PIN, HIGH);
      Serial.println("Start");
    } else {
      digitalWrite(RELAY_PIN, LOW);
      delay(200);
    }
  }
}
