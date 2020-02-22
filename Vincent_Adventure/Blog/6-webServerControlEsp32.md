# ESP32 Web Control
## Reference
I referred to this documentation on RandomNerdTutorial:   
[MicroPython: ESP32/ESP8266 Access Point (AP)](https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/)

I made some minor modification on top of the code referenced. Since I am going to use a website to control the Esp32, I added in lines of code where I change changed the address of the Website and how I want control it.

The flow will be something like this.
![]()

This is a sample code I have written:
      import usocket as socket
      except:
      import socket

      import network

      import esp
      esp.osdebug(None)

      import gc
      gc.collect()
      # =====================================================================
      import time
      import machine
      # =====================================================================
      ssid = 'Mapper'
      password = 'JokesOnYou'

      ap = network.WLAN(network.AP_IF)
      ap.active(True)
      ap.ifconfig(('192.168.16.4','255.255.255.0', '192.168.12.1', '8.8.8.8'))
      ap.config(essid=ssid, password=password, authmode = 3)

      while ap.active() == False:
      pass
      # =====================================================================
      print('Setup Successful')
      time.sleep(1)
      print(str(ap.ifconfig()))
      line = ['Setup Successful','Listening at...',str(ap.ifconfig()),'']
      time.sleep(0.1)

      def web_page(line):

      STATUS = line[0]
      STATUS2 = line[1]
      STATUS3 = line[2]

      html ="""<html>
      <head>
        <title>ESP Web Server</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="refresh" content="1; url=waiting">
        <link rel="icon" href="data:,">
        <style>

          html {
            font-family: Helvetica;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
            background-color: Black;
            color: Green;
            font-size: 20;
          }

          h1 {
            color: White;
            padding: vh;
          }
          h2 {
            color: Green;
            padding: vh;
          }

          p {
            font-size: 1.5rem;
            margin:5px;
            color: White;
          }

          .button {
            display: inline-block;
            background-color: red;
            border: none;
            border-radius: 20px;
            color: White;
            padding: 10px 20px;
            text-decoration: none;
            font-size: 30px;
            margin: 1px;
            cursor: pointer;
          }

          .button2 {
            background-color: #e7bd3b;
            display: inline-block;
            border: none;
            border-radius: 20px;
            color: White;
            padding: 10px 20px;
            text-decoration: none;
            font-size: 30px;
            margin: 1px;
            cursor: pointer;
          }
          .button3{
            background-color: #e7bd3b;
            display: inline-block;
            border: none;
            border-radius: 20px;
            color: Green;
            padding: 10px 20px;
            text-decoration: none;
            font-size: 30px;
            margin: 1px;
            cursor: pointer;
          }
          section {
            float: left;
            width: 50%;
          }
          aside {
            float: right;
            width: 50%;
          }
          .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            color: white;
            text-align: center;
          }
        </style>
      </head>
      <body>

          <h1>ESP Web Control</h1>
          <h2>""" + STATUS + """</h2>
          <h2>""" + STATUS2 + """</h2>
          <h2>""" + STATUS3 + """</h2>
        <section>
          <h1>Control</h1>
          <p><a href="/?forward"><button class="button button2">^</button></a></p>
          <p><a href="/?left"><button class="button button2"><</button></a><a href="/?stop"><button class="button button"><span>&#9888;</span></button></a><a href="/?right"><button class="button button2">></button></a></p>
          <p><a href="/?back"><button class="button button2">v</button></a></p>
        </section>
        <aside>
          <h1>Dispense</h1>
          <p><a href="/?deploy"><button class="button button3"><strong>DEPLOY!!</strong></button></a></p>
          <p><a href="/?reload"><button class="button button3"><strong>Reload</strong></button></a></p>
          <a href="/?Auto"><button class="button button3"><strong>Auto Plant</strong></button></a>
          <h1></h1>
        </aside>

      </body>

      </html>"""

      return html

      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.bind(('', 80))
      s.listen(5)

      line = ['','','','']

      while True:
      conn, addr = s.accept()
      print('Got a connection from %s' % str(addr))
      request = conn.recv(1024)
      request = str(request)
      print('Content = %s' % request)
      # =====================================================================

      forward = request.find('/?forward')
      back = request.find('/?back')
      left = request.find('/?left')
      right = request.find('/?right')
      stop = request.find('/?stop')

      if left == 6:
          print ("Left")
          line[0] = 'Left'
          mc.rotationLeft()
          time.sleep(0.1)
          print ("Stop")
          mc.stop()
      if right == 6:
          print ("Right")
          line[0] = 'Right'
          mc.rotationRight()
          time.sleep(0.1)
          print ("Stop")
          mc.stop()
      if stop == 6:
          print ("Stop")
          line[0] = 'Stop'
          mc.stop()
      if forward == 6:
          print ("Forward")
          line[0] = 'Forward'
          mc.fwd()
      if back == 6:
          print ("Reverse")
          line[0] = 'Reverse'
          mc.back()
      if dispense == 6:
          print("Dispensing")
          line[0] = 'Dispensing'
          mc.stop()
          time.sleep(1)
          o.display_(line)
          dispense_()
          line[0] = 'Dispensed'
      # =====================================================================
      response = web_page(line)
      conn.send(response)
      conn.close()

I will use Python's list to store information and update the webpage.

Refer the [MicroPython: ESP32/ESP8266 Access Point (AP)](https://randomnerdtutorials.com/micropython-esp32-esp8266-access-point-ap/) for the Understanding of code

I changed the layout of the html page which will look something like this, where the status will be updated with information from the robot.
!()[https://github.com/hamtamSP/JAV2/blob/master/Vincent_Adventure/Blog/pic/website/ESP32%20webcontrol/html_layout.png]

This line under the html section will refresh the page every 1 second and update the Url with 192.168.16.4/waiting:   

        <meta http-equiv="refresh" content="1; url=waiting">
