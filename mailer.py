import smtplib
import configparser
from bs4 import BeautifulSoup as bs
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#open and read config for smtp auth and destination
config = configparser.ConfigParser()
config.read("config.ini")

#generate message. Traffic.get used to pass usage data from the main
def genMsg(adres, up, down):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Tor Relay Traffic Report"
    msg["From"] = "Admin <admin@charliealgert.com>"
    msg["to"] = str(adres)
    a_file = open("mail_template.html", "r")
    list_of_lines = a_file.readlines()
    list_of_lines[202] = "<p id=\"GB up\" style=\"margin: 0; font-size: 22px;\">%s </p>" % up
    list_of_lines[257] = "<p id=\"GB down\" style=\"margin: 0; font-size: 22px;\">%s </p>" % down
    a_file = open("mail_template.html", "w")
    a_file.writelines(list_of_lines)
    a_file.close()
    html = MIMEText(a_file.read(), "html")
    msg.attach(html)
    return msg
    #msg = "To: User <" + str(adres) +">\nFrom: Admin <admin@charliealgert.com>\nSubject: TOR Relay Traffic Report\nBytes UP: " + str(up) + "\nBytes DOWN: " + str(down)
    #return msg


#send the report
def sendMail(recievingAddr, up, down):
    #checks
    print("sending mail")
    print(str(up))
    #email to which the report will be sent
    address = recievingAddr['SMTP_OUTPUT']['receivingAddr']
    #conenct to smtp
    server = smtplib.SMTP_SSL('smtp.hostinger.com', 465)
    #access auth data from config.ini
    server.login(str(config['SMTP_AUTH']['smtpUser']), str(config['SMTP_AUTH']['smtpPass']))
    server.sendmail(
      "admin@charliealgert.com",
      address,
        (genMsg(address, up, down)).as_string())
    #disconnect
    server.quit()
