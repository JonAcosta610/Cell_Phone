from cell_phone import CellPhone

my_cell_phone = CellPhone("iphone 14", False)
print(my_cell_phone.cell_phone_model)
print(my_cell_phone.phone_number)
print(my_cell_phone.contacts)
print(my_cell_phone.messages)


if my_cell_phone.vibrate == True:
    print("Cell phone set to vibrate!")
else:
    print("Cell phone ringer on!")

my_cell_phone.send_text_messages("What up tho")
print(my_cell_phone.messages)


for contacts in my_cell_phone.contacts.keys():
    print(contacts)