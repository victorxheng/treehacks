import requests

# mailgun integration

def send_simple_message(name, email, subject, content):
        key = "e731cf91e15411c36572b70df8fbc11f-8c8e5529-963570cb"
        response = requests.post(
            "https://api.mailgun.net/v3/sandboxd408dd7a420a425e974ff6f3a50413d0.mailgun.org/messages",
            auth=("api", key),
            data={"from": "Mailgun Sandbox <postmaster@sandboxd408dd7a420a425e974ff6f3a50413d0.mailgun.org>",
            "to": name + "<" + email + ">",
            "subject": subject,
            "text": content})