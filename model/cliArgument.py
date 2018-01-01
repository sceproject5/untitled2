import argparse
text="CV's manager"
parser=argparse.ArgumentParser(description=text)
args = None


def arg_command():
    """
    function adding all necessary argument
    """
    global args
    parser.add_argument("--login", action="store_true", help="if you want to login")
    parser.add_argument("--sign_up", "-su", action="store_true", help="if you want to sign_up")
    parser.add_argument("--fimport", "-im", action="store", help="import the json file to database")
    parser.add_argument("--fexport", "-ex", action="store_true", help="export from daatbase to json file")
    parser.add_argument("--search", "-s", action="store_true", help="the HR can search on the data base, it will open json search file .")
    parser.add_argument("-jsonformat", action="store_true", help="cv template.")
    parser.add_argument("-p", "--password", action="store", help="add password")
    parser.add_argument("-u", "--user", action="store", help="add candidate to the database")
    args = parser.parse_args()
