class CellPhone:


    def __init__(self, cell_phone_model, vibration_is_set):
        self.cell_phone_model = cell_phone_model
        self.phone_number = 3475559911 
        self.contacts = {"Michael": 1234567890, "Jim": 2345678901, "Dwight": 3456789012, "Pam": 4567890123}
        self.messages = input("Type your message here: ")
        self.vibrate = vibration_is_set

    def kind_of_cell_phone(self, cell_phone_model):
        self.cell_phone_model = cell_phone_model

    def send_text_messages(self, send_messages):
        self.messages = send_messages

    def receive_text_messages(self, receive_messages):
        self.messages = receive_messages
        