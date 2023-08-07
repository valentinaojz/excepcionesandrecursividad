def countdown (num):
    if num == 0: #todas la
        print("ka-booom")
    else:
        print(num)
        countdown(num - 1)    

countdown(5)