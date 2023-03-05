import lumix_control.camera as lumix
import threading
import subprocess

# This gets more and more out of sync.

IP = "10.0.1.105"  # IP of camera
control = lumix.Camera(IP)
UDP_PORT = 5111


def reload_stream():
    control.start_stream(UDP_PORT)
    # The stream times out after about 10 seconds.
    threading.Timer(10, reload_stream).start()


reload_stream()
# FFPlay handles all of the hard decoding stuff automatically
args = ["ffplay", "-v", "quiet", "udp://@:" + str(UDP_PORT)]
subprocess.check_call(args)
