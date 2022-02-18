import smtplib
import configparser
#open and read config for smtp auth and destination
config = configparser.ConfigParser()
config.read("config.ini")

#generate message. Traffic.get used to pass usage data from the main
def genMsg(adres, up, down):
    msg = "To: User <" + str(adres) +">\nFrom: Admin <admin@charliealgert.com>\nSubject: TOR Relay Traffic Report\nBytes UP: " + str(up) + "\nBytes DOWN: " + str(down)
    return msg

#send the report
def sendMail(recievingAddr, up, down):
    #checks
    print("sending mail")
    print(str(up))
    #email to which the report will be sent
    address = recievingAddr
    #conenct to smtp
    server = smtplib.SMTP_SSL('smtp.hostinger.com', 465)
    #access auth data from config.ini
    server.login(str(config['AUTH']['smtpUser']), str(config['AUTH']['smtpPass']))
    server.sendmail(
      "admin@charliealgert.com",
      address,
        (genMsg(address, up, down)))
    #disconnect
    server.quit()
