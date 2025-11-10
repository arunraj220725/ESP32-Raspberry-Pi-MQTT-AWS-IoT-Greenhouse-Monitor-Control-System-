#include <WiFi.h>
#include <PubSubClient.h>
#include "config.h"

WiFiClient espClient;
PubSubClient client(espClient);

float readTemperature() {
  // Placeholder
  return 25.6;
}

void setup() {
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) delay(100);

  client.setServer(MQTT_HOST, MQTT_PORT);
  while (!client.connected()) client.connect("greenhouse-node-1");
}

void loop() {
  char payload[50];
  float temp = readTemperature();
  sprintf(payload, "{\"temperature\": %.2f}", temp);

  client.publish("greenhouse/sensors/temp", payload);

  delay(5000);
}
