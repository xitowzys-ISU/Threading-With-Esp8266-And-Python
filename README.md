# Многопоточность через микроконтроллер ESP8266 и Python

## Установка MicroPython для микроконтроллера ESP8266

1. Установить библиотеку **esptool**

   ```bash
   pip install esptool
   ```

2. Полностью стераем прошивку

   ```bash
   esptool.py -p COM3 -b 115200 erase_flash
   ```

3. Устанавливаем **MicroPython**

   ```bash
   esptool --port COM3 --baud 460800 write_flash --flash_size=detect -fm dout 0 .\esp8266-20210902-v1.17.bin
   ```

## Как отправить Python файл в микроконтроллер ESP8266

> Обратите внимание ! Чтобы микроконтроллер при включении запускал сразу скрипт нужен стартовый файл с названием **boot.py**

1. Установить библиотеку **ampy**

   ```bash
   pip install adafruit-ampy
   ```

2. Отправить файл в микроконтроллер

   ```bash
   ampy -p /dev/cu.usbserial-1440 put boot.py
   ```

3. Посмотреть **Help**

   ```bash
   ampy
   ```

   