class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


final_emails = []

command = input()
while command != 'Stop':
    sender, receiver, content = command.split()
    email_info = Email(sender, receiver, content)
    final_emails.append(email_info)
    command = input()

sent_emails = [int(x) for x in input().split(", ")]

for index in sent_emails:
    final_emails[index].send()

for email in final_emails:
    print(email.get_info())
