try:
    import usocket as socket
except:
    import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()
# =====================================================================
import oLedControl as o
import motorControl as mc
import time
from hcsr04 import HCSR04
# =====================================================================
# =====================================================================
ssid = 'Mapper'
password = 'JokesOnYou'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.ifconfig(('192.168.12.4','255.255.255.0', '192.168.12.1', '8.8.8.8'))
ap.config(essid=ssid, password=password, authmode = 3)

while ap.active() == False:
    pass

print('Setup Successful')
time.sleep(1)
print(str(ap.ifconfig()))
line = ['Setup Successful','Listening at...',str(ap.ifconfig()),'']
time.sleep(1)
o.display_(line)

def web_page(line):
    
    STATUS = line[0]
    STATUS2 = line[1]
    
    html ="""<html>
    <head>
      <title>ESP Web Server</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta http-equiv="refresh" content="1; url=wait">
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
        section {
          float: left;
          margin: 0 1.5%;;
          width: 50%;
        }
        aside {
          float: right;
          margin: 0 1.5%;
          width: 50%;
        }
        .footer {
          position: absolute;
          left: 0;
          bottom: 0;
          width: 100%;
          color: white;
          text-align: center;
        }
      </style>
    </head>
    <body>

        <h1>ESP Web Server</h1>
        <h2>""" + STATUS + """</h2>
        <h2>""" + STATUS2 + """</h2>
      <section>
        <h1>Control</h1>
        <p><a href="/?forward"><button class="button button2">^</button></a></p>
        <p><a href="/?left"><button class="button button2"><</button></a><a href="/?stop"><button class="button button"><span>&#9888;</span></button></a><a href="/?right"><button class="button button2">></button></a></p>
        <p><a href="/?back"><button class="button button2">v</button></a></p>
      </section>
      <aside>
        <h1>Dispense</h1>
        <p></p>
        <p></p>
        <p></p>
        <p></p>
    </aside>

    <div class="footer">
        <h1>Settings</h1>
        <p>button</p>
        <p></p>
        <p></p>
    </div>

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
    sensor = HCSR04(trigger_pin=19, echo_pin=18)
    distance = sensor.distance_cm()
    line[1] = 'Distance: '+str(distance)+'cm'
    print('Distance:', distance, 'cm')
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
        time.sleep(3)
        print ("Stop")
        mc.stop()
    if right == 6:
        print ("Right")
        line[0] = 'Right'
        mc.rotationRight()
        time.sleep(3)
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

    o.display_(line)
    # =====================================================================
    response = web_page(line)
    conn.send(response)
    conn.close()
