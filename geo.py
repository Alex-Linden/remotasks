import bluetooth

def nearby_devices():
    nearby_devices = bluetooth.discover_devices()
    print("Nearby devices:")
    for device in nearby_devices:
        print(f"Device: {device}")
    print("")

nearby_devices()