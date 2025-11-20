from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        self.bookings = []

    def book(self, fro, to):
        self.bookings.append((fro, to))
        print(f"✅ Ticket booked successfully!\nTrain No: {self.trainNo}\nFrom: {fro} → To: {to}")

    def get_status(self):
        print(f"🚆 Train No: {self.trainNo} is running on time.")

    def get_fare(self, fro, to):
        fare = randint(150, 2000)
        print(f"💰 Fare for journey from {fro} to {to}: ₹{fare}")

# Create train object
t = Train(randint(1000, 9999))
t.book("Rampur", "Delhi")
t.get_status()
t.get_fare("Rampur", "Delhi")
