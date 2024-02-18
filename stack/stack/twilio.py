from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

def send_test(number, content):
    message = client.messages.create(
        to=number, #replace
        from_="+15017250604", #replace
        body=content)
