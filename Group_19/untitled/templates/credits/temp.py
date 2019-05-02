from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACe24048a852b18d18ac49658450803864'
auth_token = '7f7afc0c7b5a8e3b39b82d374af486a4'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+18649900776 ',
                              body='body',
                              to='+17792422966'
                          )
