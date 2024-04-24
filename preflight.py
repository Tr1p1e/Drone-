import pymavlink
from pymavlink import mavutil
import time

# Create a MAVLink connection to COM5
# master = mavutil.mavlink_connection('com5')
master = mavutil.mavlink_connection('udpin:localhost:57600')

# Wait for the heartbeat
master.wait_heartbeat()
print("Connected to MAVLink device on COM5")

# Check if GPS is locked
while True:
    msg = master.recv_match(type='GPS_STATUS', blocking=True)
    if msg and msg.satellites_visible > 0:
        if msg.satellite_used < 4:
            print("Waiting for more satellites to be used for GPS lock...")
        else:
            print("GPS is locked")
            break
    else:
        print("GPS data not available")
    time.sleep(1)

# Close the connection
master.close()


