from model import singIn,signup, sqllite, cliArgument
from route import hr_route,ca_route


def default_route():
    sqllite.connectDatabase()
    user_name = cliArgument.args.user
    user_password = cliArgument.args.password
    if cliArgument.args.login:
        if user_name and user_password:
            response = singIn.sign_in(user_name, user_password)
            if response == "hr":
                hr_route.hr_route()
            elif response == "ca":
                ca_route.ca_route()
        else:
            print("user name or password are missing")
    elif cliArgument.args.sign_up:
        if user_name and user_password:
            signup.sign_up(user_name, user_password)
        else:
            print("user name and password must entry")
    sqllite.disConnectDataBase()
