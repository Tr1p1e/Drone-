import usb.core

# Find the USB device
dev = usb.core.find(idVendor=0x10C4, idProduct=0xEA60)

# Check if the device was found
if dev is None:
    raise ValueError('Device not found')

# Set the configuration of the device
dev.set_configuration()

# Example: Read data from the USB device
endpoint = dev[0][(0, 0)][0]
data = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)

# Example: Write data to the USB device
# dev.write(endpoint.bEndpointAddress, b'data_to_send')

# Close the USB device
usb.util.dispose_resources(dev)

