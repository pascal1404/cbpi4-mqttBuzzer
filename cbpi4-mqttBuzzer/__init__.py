
# -*- coding: utf-8 -*-
import os, threading, time
from aiohttp import web
import logging
import asyncio
from cbpi.api import *
from cbpi.api.config import ConfigType
from cbpi.api.base import CBPiBase

logger = logging.getLogger(__name__)

buzzer_topic = None

class MQTT_Buzzer(CBPiExtension):

    def __init__(self,cbpi):
        self.cbpi = cbpi
        self._task = asyncio.create_task(self.run())


    async def run(self):
        logger.info('Starting Buzzer background task')
        await self.buzzer_topic()
        if buzzer_topic is None or buzzer_topic == "" or not buzzer_topic:
            logger.warning('Check buzzer topic is set')

        self.listener_ID = self.cbpi.notification.add_listener(self.buzzerEvent)
        logger.info("Buzzer Listener ID: {}".format(self.listener_ID))
        logging.info("MQTT Buzzer started")
        await self.start_buzz()
        pass

    async def buzzer_topic(self):
        global buzzer_topic
        buzzer_topic = self.cbpi.config.get("buzzer_topic", None)
        if buzzer_topic is None:
            logger.info("INIT MQTT Buzzer")
            try:
                await self.cbpi.config.add("buzzer_topic", "cbpi/alarm", ConfigType.STRING, "Buzzer MQTT-Topic")
                buzzer_topic = self.cbpi.config.get("buzzer_topic", None)
            except:
                logger.warning('Unable to update config')

    async def buzzerEvent(self, cbpi, title, message, type, action):
        if str(type) == "success":
            self.cbpi.ws.send(dict(topic=self.buzzer_topic, data={"alarm" : "OK"} ))
            self.cbpi.push_update("cbpi/alarm", dict(alarm="OK"), True)
        elif str(type) == "info":
            self.cbpi.ws.send(dict(topic=self.buzzer_topic, data={"alarm" : "Info"} ))
            self.cbpi.push_update("cbpi/alarm", dict(alarm="Info"), True)
        elif str(type) == "warning":
            self.cbpi.ws.send(dict(topic=self.buzzer_topic, data={"alarm" : "Warning"} ))
            self.cbpi.push_update("cbpi/alarm", dict(alarm="Warning"), True)
        else:
            self.cbpi.ws.send(dict(topic=self.buzzer_topic, data={"alarm" : "Error"} ))
            self.cbpi.push_update("cbpi/alarm", dict(alarm="Error"), True)

    async def start_buzz(self):
        self.cbpi.ws.send(dict(topic=self.buzzer_topic, data={"alarm" : "OK"} ))
        self.cbpi.push_update("cbpi/alarm", dict(alarm="OK"), True)

def setup(cbpi):
    cbpi.plugin.register("MQTT_Buzzer", MQTT_Buzzer)
    pass