# Program Input Data Rumah Sakit Pasien Covid 

![image](https://user-images.githubusercontent.com/78904717/183626681-30e9a97b-c752-4578-8487-82ad17a3bad6.png)


Desktop Application that can obtain data about hospitals that have responsibility to take care of COVID patients. 
I make this application as a process of applying job as a course assistant in my campus. 

## Why Create This Application?
There are several things that encouraged me to create this application, such as:
* Pandemic Situation 
* Experience as volunteer

Pandemic situations make impacts in every aspect of our lives that accelerate digitalization. As acceleration continues to grow, we need an  application to make efficient movement on 
inputting covid patient data as well. On the other hand, I have experienced in volunteering for input data for hospital that take care of covid patient. That's why, 
I am curious to make this desktop application. 

## Database
Here's the database view for this application.
![database program input data rs covid](https://user-images.githubusercontent.com/78904717/183624706-0208b6c9-2962-4ed0-8555-0e2d2ec0280e.png)

There's a file that I have uploaded for the database in sql format. But, if you want to create the database by your own, you can follow this step:
1. Creating Database
```
create database infors;
````
2. Using the database
```
use infors;
```
3. Making table name datars
```
create table datars (

    -> KRS int(10) PRIMARY KEY,

    -> NamRS varchar(30),

    -> JumPas int(5),

    -> JumBed int(3),

    -> Tanggal date,

    -> Waktu time,

    -> Penginput varchar(15) );
```
After that, the database and its table can be used. 

## Prerequisites
Before starting the application, make sure you have installed python, XAMPP, and mysql connector as well. 
* [Download Python](https://www.python.org/downloads/)
* [Download XAMPP](https://www.apachefriends.org/download.html)
* [Download MySQL Connector](https://dev.mysql.com/downloads/connector/python/)

## Package
There are several packages that I use here, such as:
![image](https://user-images.githubusercontent.com/78904717/183626964-ecd24790-5ade-4b11-a0c4-a1634cd5fd3a.png)

## Extra Note
If you have: 
* Input by clicking button save 
* Delete data by input the Kode RS and click button delete
* Edit data by entering the newest data and clicking the update button 

After that, you should click the refresh button  in order to show the newest data in the table as well. 
If you get trouble on the refresh button, just make the path from os.startfile <b> more specified </b> based on your directory.

## Closing
Thank you for reading my read.me file documentation. Hopefully this documentation can help you for using this application. Let me know, if you have any suggestion 
for improvement on this application. Thank you!


