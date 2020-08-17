input_str=str(input())
message1 = input_str[0:-1:2]
message2 = input_str[1:len(input_str):2]
print(message1.strip("#") + "," + message2.strip("#"))
