
###########     Sending Email without attachment

#import smtplib
#
#sender='rfidlibrarypccoe@gmail.com'
#pswd='14785269'
#to= ['gokhalehemal11@gmail.com','psprasha50@gmail.com','vineetjob8@gmail.com','sharviljadhav@gmail.com']
#subject='Message from Library'
#body= 'Wassup bruh'
#
#email_txt="""\
#From: %s
#To: %s
#Subject: %s
#
#%s
#""" % (sender,",".join(to),subject,body)
#
#try:
#	server=smtplib.SMTP('smtp.gmail.com',587)
#	server.ehlo()
#	server.starttls()
#	server.login(sender,pswd)
#	server.sendmail(sender,to,email_txt)
#	server.quit()
#except:
#	print "something wrong"	
#

##### References : https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
#####			   http://stackoverflow.com/a/27515833/2684304	  


# ===========================================================================================================================================

###########     Sending Email with attachment


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'rfidlibrarypccoe@gmail.com'				#### Sender email and password 
email_password = '14785269'

email_send = ['gokhalehemal11@gmail.com', 'vineetjob8@gmail.com','sharviljadhav@gmail.com','psprasha50@gmail.com']		## LIST of Recipients

subject = 'Test file attachment with python'			### subject


##### Setup email msg

msg = MIMEMultipart()			
msg['From'] = email_user						# sender
msg['To'] = ','.join(email_send)				# receiver	STRING					
msg['Subject'] = subject 						# subject

body = 'Open file attached' 					# body
msg.attach(MIMEText(body,'plain'))


#####   Attaching file to email

filename='file.txt'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read()) 							## encode to base64
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)												# attach attachement and convert text to STRING
text = msg.as_string()

try:
	server = smtplib.SMTP('smtp.gmail.com',587)					### connect to gmail server
	server.ehlo()												## Check connection with server
	server.starttls()											### Start server
	server.login(email_user,email_password)						### login to sender gmail account
	server.sendmail(email_user,email_send,text)					### attach LIST of recipients
	server.quit()
except:
	print "something wrong"

##### References : https://stackoverflow.com/questions/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib
#########			https://github.com/samlopezf/Python-Email/blob/master/send_email.py	


