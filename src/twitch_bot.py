# This project is a Twitch chat robot project.
# 
# For more detail, please refer to Twitch IRC https://help.twitch.tv/customer/portal/articles/1302780-twitch-irc.

import socket, string

HOST = "irc.twitch.tv"
PORT = 6667
PASS = "oauth:chae6dn0fowwptak5bx4b0uboxctk3" # Change Oauth key here
NICK = "cyhuang17" # Change your Twitch user name here
readbuffer = ""
MODT = True

def send_message(message):
	command = "PRIVMSG #" + NICK + ": " + message + "\r\n"
	print("send_message: " + command)
	s.send(command.encode())

s = socket.socket()
s.connect((HOST, PORT))
s.send(("PASS " + PASS + "\r\n").encode())
s.send(("NICK " + NICK + "\r\n").encode())
s.send(("JOIN #" + NICK + " \r\n").encode())

while True:
	readbuffer = readbuffer + s.recv(1024).decode()
	#print("+++++++readbuffer: " + readbuffer)
	temp = readbuffer.split("\n")
	readbuffer = temp.pop()

	for line in temp:
		#print("+++++++++line: " + line)

		if (line[0] == "PING"):
			s.send(("PONG %s\r\n" % line[1]).encode())
		else:
			parts = line.split(":")

			for part in parts:
				print(part)

			print("part[1] " + parts[1])

			if "jawawa" in parts:
				jawawaCmd = parts[len(parts) - 1].lower()
				print("JAWAWA command: " + jawawaCmd)
				if jawawaCmd == 'up':
					print("JAWAWA UP")
				elif jawawaCmd == 'down':
					print("JAWAWA DOWN")
				elif jawawaCmd == 'forward':
					print("JAWAWA FORWARD")
				elif jawawaCmd == 'back':
					print("JAWAWA BACK")
				elif jawawaCmd == 'left':
					print("JAWAWA LEFT")
				elif jawawaCmd == 'right':
					print("JAWAWA RIGHT")
				else:
					print("Unknow command")

			elif "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
				try:
					message = parts[2][:len(parts[2])]
				except:
					message = ""

				usernamesplit = parts[1].split("!")
				username = usernamesplit[0]

				if MODT:
					print(username + ": " + message)
					if message == "Hey":
						send_message("Welcome to my stream, " + username)

				for l in parts:
					if "End of /NAME lis" in l:
						MODT = True
			else:
				print("EVENT: " + parts[1])

