class chatbook:
    def __init__(self):
        self.user_name=" "
        self.password= " "
        self.loggedin= False
        self.menu()

    def menu(self):
        user_input= input("""Welcome to chatbook ! How you would like to proceed ?
                          1. Press 1 for signup
                          2. Press 2 for Signin
                          3. Press 3 for write a post
                          4. Press 4 for message a friend
                          5. Press any other key for exit """)
        if user_input =="1":
            self.signup()
        elif user_input =="2":
            self.signin()
        elif user_input =="3":
            pass
        elif user_input =="4":
            pass
        else:
            exit()


    def signup(self):
        email= input("Enter your email here -->")
        pass1= input("Enter your password here -->")
        self.user_name=email
        self.password= pass1
        print("You have signedup successfully !")
        print("\n")
        self.menu()


    def signin(self):
        if self.user_name==" " and self.password==" ":
            print("Please first signup to get access of this platform")
        else:
            username= input("Enter your email here --->")
            pwd1= input("Enter your paasword here -->")
            if self.user_name==username and self.password==pwd1:
                print("You have signedin successfully")
                self.loggedin=True
            else:
                print("Please input correct credentials")

        print("\n")
        self.menu()

obj= chatbook()