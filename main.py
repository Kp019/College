import smtplib
l = input("enter the mail id:")
pas = input("password:")
mg = input("""enter the mail:""")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(l, pas)
sender = l
rec = ['krishnaprasadr666@gmail.com','krishnaprasad_kp@ieee.org']
n = ['kp','Krishnaprasad R']
msg = mg
for i in range(2):
    server.sendmail(sender, rec[i],'hi '+n[i]+' '+msg)

