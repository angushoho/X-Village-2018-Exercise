date = input("input date : ")
event = input("input event : ")
description = input("input description : ")

with open("note", "a+") as f:
    f.write("date : " + date + "\n")
    f.write("event : " + event + "\n")
    f.write("descroption : " + description + "\n")
    f.write("------------------\n")