# Defining Class Message
class Message:
    def __init__(self, sender, recipient):
        # Initialize Message object with sender, recipient, and an empty message body
        self.sender = sender
        self.recipient = recipient
        self.message_body = []

    def get_sender(self):
        # Return the sender of the message
        return self.sender

    def get_recipient(self):
        # Return the recipient of the message
        return self.recipient

    def append(self, line):
        # Append a line to the message body
        self.message_body.append(line)

    def toString(self):
        # Initialize an empty string to store the message
        message_str = ""
        # Add the sender and recipient information to the message
        message_str += "From: " + self.sender + "\n"
        message_str += "To: " + self.recipient + "\n"
        # Add each line of the message body to the message
        for line in self.message_body:
            message_str += line + "\n"
        # Return the final message as a string
        return message_str


# Example usage:
if __name__ == '__main__':
    # Create a Message object with sender "Harry Morgan" and recipient "Rudolf Reindeer"
    message = Message("Harry Morgan", "Rudolf Reindeer")
    # Append lines to the message body
    message.append("Dear Rudolf,")
    message.append("Merry Christmas!")
    message.append("Best regards,")
    message.append("Harry")
    # Convert the message to string and print it
    print(message.toString())