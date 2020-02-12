try:
    import usocket as socket
except:
    import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Mapper'
password = 'JokesOnYou'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.ifconfig(('192.168.12.4','255.255.255.0', '192.168.12.1', '8.8.8.8'))
ap.config(essid=ssid, password=password, authmode = 3)

while ap.active() == False:
    pass

print('Setup Successful')
print(ap.ifconfig())

def web_page(line):
    
    STATUS = line[0]
    
    html ="""<html>
    <head>
      <title>ESP Web Server</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="icon" href="data:,">
      <style>

        html {
          font-family: Helvetica;
          display: inline-block;
          margin: 0px auto;
          text-align: center;
          background-color: Black;
          color: Green;
        }

        h1 {
          color: White;
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
          padding: 16px 40px;
          text-decoration: none;
          font-size: 30px;
          margin: 1px;
          cursor: pointer;
        }

        .button2 {
          background-color: #e7bd3b;
        }
      </style>
    </head>
    <body>
      <h1>ESP Web Server</h1>
      <p>""" + STATUS + """</p>
      <p><a href="/?forward"><button class="button button2">^</button></a></p>
      <p><a href="/?left"><button class="button button2"><</button></a><a href="/?stop"><button class="button button"><span>&#9888;</span></button></a><a href="/?right"><button class="button button2">></button></a></p>
      <p><a href="/?back"><button class="button button2">v</button></a></p>
    </body>

    </html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

line = [""]

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

    if forward == 6:
        print ("Forward")
        line = ["Forward"]
    if back == 6:
        print ("Reverse")
        line = ["Reverse"]
    if left == 6:
        print ("Left")
        line = ["Left"]
    if right == 6:
        print ("Right")
        line = ["Right"]
    if stop == 6:
        print ("Stop")
        line = ["Stop"]
    
    # =====================================================================
    response = web_page(line)
    conn.send(response)
    conn.close()