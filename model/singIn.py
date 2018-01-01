from model import authentication


def sign_in(user_name, user_password):
    """"
    function sign in
    """
    if authentication.authentication(user_name, user_password):
        print("login successfully")
        if authentication.check_perrsmisson(user_name, user_password) == True:
            print("you're HR")
            return "hr"
        else:
            print("you're candidate")
            return "ca"
    else:
        print("user name or password wrong")