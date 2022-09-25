from cell_phone import CellPhone

my_cell_phone = CellPhone("iphone 14", False)
print(my_cell_phone.cell_phone_model)
print(my_cell_phone.phone_number)


if my_cell_phone.vibrate == True:
    print("Cell phone set to vibrate!")
else:
    print("Cell phone ringer on!")
