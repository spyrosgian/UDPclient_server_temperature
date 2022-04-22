# UDPserver_client_temperature
This is a Git repository that contains the Python script for Assignment 4 - Part 1 of the _Advanced Python Programming Part-Time Course_ of Cardiff University.

This python UDP client/server application converts a Centigrade temperatre into a Fahrenheit temperature. Python socket programming and GUI were used.

The client application, temperatureClient.py, sends a Centigrade temperature to the server. The server application, temperatureServer.py, converts the 
Centigrade temperature to a Fahrenheit temperature, and sends the Fahrenheit temperature back to the client application which can then 
display it. 

The client application presents the user with the following window:

![image](https://user-images.githubusercontent.com/40058400/164729605-57b7416e-8712-4524-808a-afd396f88c4d.png)

A user of the client application enters a temperature in the Centigrade Entry widget.  When the user clicks on the button Convert, a request is sent to the server to ask for the Fahrenheit temperature corresponding to the current Centigrade temperature and this is placed in the Fahrenheit Entry widget.
The program displays a message in the Status Entry widget if the server is not available.
When the user clicks on the button Clear, all Entry widgets are cleared.
When the user clicks on the button Done, the user exits the application. 
