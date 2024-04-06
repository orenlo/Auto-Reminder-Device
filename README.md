# Auto-Reminder-Device
Smart Eyewear Reminder System: An IoT-powered solution utilizing ESP32 microcontrollers and cloud connectivity to issue timely notifications on users' smartphones if they forget to bring their glasses when leaving home, enhancing daily life and user convenience. **The information is theoretical.**


Smart Eyewear Reminder System Setup and Implementation Guide

Equipment Required:
1.	Two ESP32 microcontroller boards, light, LCD screen and battery
2.	Smartphone with WIFI 
3.	USB cables for programming ESP32 boards
4.	Glasses case with space to accommodate the ESP32 board
   
   
Setup Instructions:
1.	ESP32 Base Station Setup: 
•	Copy the code of the ESP32 boards as the base station . 
•	Connect the base station ESP32 to your Wi-Fi network.
2.	ESP32 in the Glasses Case Setup:
•	Copy the second ESP32 board to fit inside the glasses case.
3.	Geofencing Setup on Smartphone:
•	Install a geofencing app or use built-in geofencing features on your smartphone.
•	Set up a geofence around your home's vicinity.
•	Configure the app to trigger an event when your smartphone leaves the geofenced area.
4.	Communication between Smartphone and Base Station:
•	Determine the communication protocol between your smartphone and the base station ESP32.
•	Implement code on the base station to receive signals from your smartphone.
•	Configure the smartphone app to send signals to the base station when you leave the geofenced area.
5.	Notification Mechanism:
•	Develop a notification system on the base station ESP32 to alert you if the glasses are not within range. https://www.youtube.com/watch?v=XRJBFWlOSJ8&ab_channel=CumulusCycles

•	Use AWS cloud to do so - https://www.youtube.com/watch?v=z8T4hAERuOg&ab_channel=AWSIoT
•	Customize the notification to provide a reminder to bring your glasses.



