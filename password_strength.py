def main():
    password = input()







def check_length(password):
    password_length = len(password)
    if password_length >= 8:
        return "good"
    else:
        return "bad"

def check_symbol(password):
    password_list = password.split()
