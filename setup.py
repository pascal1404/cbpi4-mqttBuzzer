from setuptools import setup

setup(name='cbpi4-mqttBuzzer',
      version='0.0.1',
      description='CraftBeerPi Plugin to activate a buzzer via MQTT',
      author='Pascal Scholz',
      author_email='pascal1404@gmx.de',
      url='https://github.com/pascal1404/cbpi4-mqttBuzzer',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-mqttBuzzer': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-mqttBuzzer'],
     )