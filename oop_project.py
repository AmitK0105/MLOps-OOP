class chatbook:
    def __init__(self):
        self.user_name=" "
        self.password= " "
        self.loggedin= "False"
        self.menu()

    def menu(self):
        user_input= input("""Welcome to chatbook ! How you would like to proceed ?
                          1. Press 1 for signup
                          2. Press 2 for Signin
                          3. Press 3 for write a post
                          4. Press 4 for message a friend
                          5. Press any other key for exit """)
        if user_input =="1":
            pass
        elif user_input =="2":
            pass
        elif user_input =="3":
            pass
        elif user_input =="4":
            pass
        else:
            exit()

obj= chatbook()