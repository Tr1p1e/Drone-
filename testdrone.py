from pymavlink import mavutil
import time

# Create a MAVLink connection to COM5
# master = mavutil.mavlink_connection('com5')
master = mavutil.mavlink_connection('udpout:localhost:57600')

# Wait for the heartbeat
master.wait_heartbeat(timeout=60)
    
# Send a command to arm the vehicle
master.mav.command_long_send(master.target_system, master.target_component,
                             mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)

# Wait for the vehicle to arm
while not master.motors_armed():
    time.sleep(1)

# Take off
master.mav.command_long_send(master.target_system, master.target_component,
                             mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 0)

# Wait for the vehicle to take off
while master.location.global_relative_frame.alt < 10:
    time.sleep(1)

# Land
master.mav.command_long_send(master.target_system, master.target_component,
                             mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, 0, 0)

# Wait for the vehicle to land
while master.motors_armed():
    time.sleep(1)

# Close the connection
master.close()
