class CellPhone:


    def __init__(self, cell_phone_model, vibrate_set):
        self.cell_phone_model = cell_phone_model
        self.phone_number = 3475559911 
        # self.contacts = contacts
        # self.messages = messages
        self.vibrate = vibrate_set

    def kind_of_cell_phone(self, cell_phone_model):
        self.cell_phone_model = cell_phone_model

    def send_text_messages(self, send_messages):
        self.messages = send_messages

    def receive_text_messages(self, receive_messages):
        self.messages = receive_messages
        