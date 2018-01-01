import hashlib
from model import sqllite


def authentication(userName, password):
    query = "select * from HR_users where user='"+str(userName)+"' and password='"+str(password_encrypet(password))+"'"
    if sqllite.countRow(sqllite.query(query)) == 1:
        return True
    query = "select * from candidate_users where user='" + str(userName) + "' and password='" + str(
        password_encrypet(password)) + "'"
    if sqllite.countRow(sqllite.query(query)) == 1:
        return True
    return False


def check_perrsmisson(userName, password):
    query = "select * from HR_users where user='" + str(userName) + "' and password='" + str(password_encrypet(password)) + "'"
    if sqllite.countRow(sqllite.query(query)) == 1:
        return True
    return False


def password_encrypet(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()


def check_user_exist(userName):
    query = "select * from candidate_users where user='"+str(userName)+"'"
    if sqllite.countRow(sqllite.query(query)) == 1:
        return True
    query = "select * from HR_users where user='"+str(userName)+"'"
    if sqllite.countRow(sqllite.query(query)) == 1:
        return True
    return False
