import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("SUDARSHAN C", "BAB9542569068")

#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("sudarshan.c17@iiits.in", "sudarshan333u@gmail.com", msg)