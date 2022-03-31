from bs4 import BeautifulSoup
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = "classroom.its.ac.id"
sock.connect((url, 80))
sock.send(b"GET / HTTP/1.1\r\nHost:classroom.its.ac.id\r\n\r\n")
response = sock.recv(4096)

soup = BeautifulSoup(response, 'html.parser')

print(soup.prettify())

#Bingung yang diambil yang mana karena hanya pesan redirect
