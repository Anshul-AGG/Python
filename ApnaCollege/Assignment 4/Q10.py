# OOP chat system


class User:
    def __init__(self, username):
        self.username = username


class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def display(self):
        return f"{self.sender.username} : {self.content}"


class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(f"{user.username} joined {self.room_name}")

    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.username} left {self.room_name}")

    def send_message(self, user, content):
        if user in self.users:
            msg = Message(user, content)
            self.messages.append(msg)
        else:
            print(f"{user.username} is not in the chatroom!")

    def view_history(self):
        print(f"\n--------------Chat history in {self.room_name}-------------")

        for msg in self.messages:
            print(msg.display())


# Create users
u1 = User("Anshul")
u2 = User("Riya")

# Create chatroom
room = ChatRoom("Python Learners")

# Users join
room.join(u1)
room.join(u2)

# Send messages
room.send_message(u1, "Hey everyone!")
room.send_message(u2, "Hi Anshul, excited to learn Python!")

# View chat history
room.view_history()

# User leaves
room.leave(u2)
