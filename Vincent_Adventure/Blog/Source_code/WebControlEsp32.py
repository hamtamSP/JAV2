# Complete project details at https://RandomNerdTutorials.com
# 0.6A to run normally
import wifimgr
from time import sleep
import machine
# =====================================================================
int1 = 15 #Brown
int2 = 2  #Red
int3 = 0  #Orange
int4 = 4  #Yellow
# =====================================================================
motor1a = machine.Pin(int1,machine.Pin.OUT)
motor1b = machine.Pin(int2,machine.Pin.OUT)
motor2a = machine.Pin(int3,machine.Pin.OUT)
motor2b = machine.Pin(int4,machine.Pin.OUT)

# =====================================================================
def fwd():
    motor1a(1)
    motor1b(0)
    motor2a(1)
    motor2b(0)
def stop():
    motor1a(0)
    motor1b(0)
    motor2a(0)
    motor2b(0)
def back():
    motor1a(0)
    motor1b(1)
    motor2a(0)
    motor2b(1)
def rotationLeft():
    motor1a(1)
    motor1b(0)
    motor2a(0)
    motor2b(1)
def rotationRight():
    motor1a(0)
    motor1b(1)
    motor2a(1)
    motor2b(0)
def rest():
    stop()
    time.sleep(1)
# =====================================================================
try:
  import usocket as socket
except:
  import socket

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D

# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")

def web_page():
    gpio_state="ON"

    html = """<html><head><title>ESP Web Server</title><meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"><style>html {font-family: Helvetica;display: inline-block;margin: 0px auto;text-align: center;
    }h1 {color: #0F3376;padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block;background-color: #e7bd3b;border: none;
    border-radius: 4px;color: white;padding: 16px 40px;text-decoration: none;font-size: 30px;margin: 2px;cursor: pointer;}
    .button2 {background-color: #4286f4;}</style></head><body><h1>ESP Web Server</h1><p>GPIO state:<strong>
    """ + gpio_state + """
    </strong></p>
    <p><a href="/?forward=true"><button class="button">Up</button></a></p>
    <p><a href="/?rotateLeft=true"><button class="button button2">Left</button></a><a href="/?rotateRight=true"><button class="button button2">Right</button></a></p>
    <p><a href="/?reverse=true"><button class="button button4">Back</button></a></p>
    </body></html>"""
    return html

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind(('', 80))
  s.listen(5)
except OSError as e:
  machine.reset()

while True:
  try:
    conn, addr = s.accept()
    conn.settimeout(3.0)
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    conn.settimeout(None)
    request = str(request)
    print('Content = %s' % request)
    forward = request.find('/?forward=true')
    back = request.find('/?reverse=true')
    left = request.find('/?rotateLeft=true')
    right = request.find('/?rotateRight=true')

    if forward == 6:
        print('forward')
        fwd()
    if back == 6:
        print('back')
        back()
    if left == 6:
        print('left')
        rotationLeft()
    if right == 6:
        print('right')
        rotationRight()

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  except OSError as e:
    conn.close()
    print('Connection closed')
