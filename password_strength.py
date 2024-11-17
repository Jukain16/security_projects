def main():
    password = input()
    check_length(password)
    check_symbol(password)







def check_length(password):
    password_length = len(password)
    if password_length >= 8:
        return "good"
    else:
        return "bad"

def check_symbol(password):
    password_list = password.split()






main()
