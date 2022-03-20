# cbpi4-mqttBuzzer

> :Info: **_Attention:_** This Plugin would not be needed anymore! You can get the Notifications at MQTT without these plugin. topic: cbpi/notification

~~A Plugin to send alarms via MQTT to a device which has a buzzer installed.

~~You need to specify the MQTT-topic in the settings-menu. Default is `cbpi/alarm`.

~~The MQTT-Messages are `{alarm: "OK"}` or `{alarm: "Info"}` or `{alarm: "Warning"}` or `{alarm: "Error"}`.

The [MQTT-Device](https://github.com/InnuendoPi/MQTTDevice4) can recieve these messages and activate the buzzer.
