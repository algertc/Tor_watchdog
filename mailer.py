import smtplib
import configparser
config = configparser.ConfigParser()
config.read("config.ini")

def genMsg(adres, up, down):
    msg = "To: User <" + str(adres) +">\nFrom: Admin <admin@charliealgert.com>\nSubject: TOR Relay Traffic Report\nBytes UP: " + str(up) + "\nBytes DOWN: " + str(down)
    return msg
def sendMail(recievingAddr, up, down):
#    server.sendmail(sender_email, address, ("Thank you for creating an account. Your Username is" + address + "\n" + "Your password is: " + passw))
    print("sending mail")
    print(str(up))
    address = recievingAddr
    server = smtplib.SMTP_SSL('smtp.hostinger.com', 465)
    server.login(str(config)['AUTH']['smtpUser'], str(config['AUTH']['smtpPass']))
    server.sendmail(
      "admin@charliealgert.com",
      address,
        (genMsg(address, up, down)))
    server.quit()
#test
#sendMail("admin@charliealgert.com")

#msg = ("From: %s\r\nTo: %s\r\n\r\n"
      # % (fromaddr, ", ".join(toaddrs)))