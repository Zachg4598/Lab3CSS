import tornado.web

UserProfiles = {
    "alice": {
        "Real Name": "Alice Smith",
        "Login": "alice",
        "DOB": "Jan. 1",
        "email": "alice@example.com",
    },
    "bob": {
        "Real Name": "Bob Jones",
        "Login": "bob",
        "DOB": "Dec. 31",
        "email": "bob@bob.xyz",
    },
    "carol": {
        "Real Name": "Carol Ling",
        "Login": "Carol",
        "DOB": "Jul. 17",
        "email": "carol@example.com",
    },
    "dave": {
        "Real Name": "Dave N. Port",
        "Login": "dave",
        "DOB": "Mar. 14",
        "email": "dave@dave.dave",
    },
}

class UserProfileHandler(tornado.web.RequestHandler):
    def get(self, user_login):
        if user_login in UserProfiles:
            user_profile = UserProfiles[user_login]
            self.render("profile.html", user_profile=user_profile, user_login=user_login)
        else:
            self.write("Login not found")