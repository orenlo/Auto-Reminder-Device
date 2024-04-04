# Auto-Reminder-Device
Smart Eyewear Reminder System: An IoT-powered solution utilizing ESP32 microcontrollers and cloud connectivity to simulate timely notifications on users' smartphones if they forget to bring their glasses when leaving home, enhancing daily life and user convenience.


Smart Eyewear Reminder System Setup and Implementation Guide

Equipment Required:
1.	Two ESP32 microcontroller boards
2.	Smartphone with GPS capabilities
3.	USB cables for programming ESP32 boards
4.	Glasses case with space to accommodate the ESP32 board
   
Setup Instructions:
1.	ESP32 Base Station Setup:
•	Program one of the ESP32 boards as the base station.
•	Connect the base station ESP32 to your Wi-Fi network.
•	Implement code on the base station ESP32 to:
•	Establish a connection with the ESP32 in the glasses case.
•	Listen for signals from your smartphone indicating that you've left the geofenced area.
•	Check the connection status with the ESP32 in the glasses case when a signal is received.
•	Send a notification to your smartphone if the glasses are not within range.
2.	ESP32 in the Glasses Case Setup:
•	Program the second ESP32 board to fit inside the glasses case.
•	Implement code on the ESP32 in the glasses case to:
•	Establish a connection with the base station ESP32.
•	Continuously maintain the connection with the base station.
•	Send periodic signals to the base station to indicate its presence.
3.	Geofencing Setup on Smartphone:
•	Install a geofencing app or use built-in geofencing features on your smartphone.
•	Set up a geofence around your home's vicinity.
•	Configure the app to trigger an event when your smartphone leaves the geofenced area.
4.	Communication between Smartphone and Base Station:
•	Determine the communication protocol between your smartphone and the base station ESP32.
•	Implement code on the base station to receive signals from your smartphone.
•	Configure the smartphone app to send signals to the base station when you leave the geofenced area.
5.	Notification Mechanism:
•	Develop a notification system on the base station ESP32 to alert you if the glasses are not within range.
•	Customize the notification to provide a reminder to bring your glasses.
6.	Testing and Optimization:
•	Test the entire system to ensure all components function as expected.
•	Optimize the system for power efficiency and reliability.
•	Conduct real-world tests to verify the system's performance in various scenarios.
7.	Deployment:
•	Deploy the base station ESP32 in your home.
•	Place the ESP32 in the glasses case and ensure it fits securely.
•	Activate the geofencing feature on your smartphone and configure it to work with the system.

