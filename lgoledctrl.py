from telnetlib import Telnet
LG_WEBOS_CONTROL_PORT = 9761


class WebOSRemote:
    currentFormat = 0
    currentPictureMode = 0

    def __init__(self, ip="192.168.1.1"):
        self.ip = ip

    def power_on(self):
        #power on
        self.send_command("POWER on")

    def power_off(self):
        #power off
        self.send_command("POWER off")

    def screen_mute_on(self):
        #screen mute on
        self.send_command("SCREEN_MUTE screenmuteon")

    def screen_mute_off(self):
        #screenMuteOff
        self.send_command("SCREEN_MUTE allmuteoff")

    def send_command(self, command):
        try:
            tvConnection = Telnet(self.ip, LG_WEBOS_CONTROL_PORT)
            print(tvConnection.read_eager().decode('ascii'))
            print("Command is: "+ command)
            print(command.encode('ascii') + b"\n")
            tvConnection.write(command.encode('ascii')+b"\r\n")
            print(tvConnection.read_eager().decode('ascii'))
            tvConnection.close()
        except:
            print("Could not connect to TV")
    def next_format(self):
        self.send_command("KEY_ACTION aspectratio")
        #if self.currentFormat == 0:
        #    self.send_command("ASPECT_RATIO 4by3")
        #    self.currentFormat += 1
        #if self.currentFormat == 1:
        #    self.send_command("ASPECT_RATIO 16by9")
        #    self.currentFormat +=1
        #if self.currentFormat == 2:
        #    self.send_command("ASPECT_RATIO setbyoriginal")

    def cycle_picture_mode(self):
        self.send_command("KEY_ACTION videomode")
