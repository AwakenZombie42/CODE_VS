import emoji

def emojize_text():
    user_input = input()
    
    emojized_string = emoji.emojize(user_input)
    
    print(emojized_string)

if __name__ == "__main__":
    emojize_text()