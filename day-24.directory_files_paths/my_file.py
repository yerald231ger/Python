with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)


with open("my_file_new.txt", "a") as file:
    file.write("\nI am a student")

with open("my_file_new.txt", "w") as file:
    file.write("Hello my name is gerardo")
    
    
    
    