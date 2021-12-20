- Install Motion
   ```bash
   sudo apt-get install motion
   ```
- Navigate to the /etc/default/motion file to set Motion daemon to yes so that it will always be running. Use the below command to edit the file:
  ```bash
  sudo nano /etc/default/motion
  ```
  Then press CTRL+X > ‘Y’ > Enter to save the file.
- Use the below command to set the permission for the motion Directory (/var/lib/motion/), where it saves all the Video recordings and picture files.
  ```bash
  sudo chown motion:motion /var/lib/motion/
  ```
- Turn off the localhost inside the motion configuration file to access the video feed outside the Raspberry Pi on the same network. 
  To turn off the localhost, use the following command:
  ```bash
  sudo nano /etc/motion/motion.conf
  ```
  You can use the ctrl+W to search for a specific word inside the nano editor.

- To check the video feed, start the motion using the below command:
  ```bash
  sudo /etc/init.d/motion restart
  ``` 

- Open the video feed page using your Pi’s IP address with port 8081 (192.168.1.207:8081).
  Flask Web Framework is used to create a Web Server to control the robot. 

  Installing Flask in Raspberry Pi
   ```bash
   pip install flask
   ```
   
 - Running the code
   ```bash
   cd SurveillanceRobot
   sudo nano robot.py
   python robot.py
   ```
