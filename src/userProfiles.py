import tornado.web
import os 
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

    def post(self, user_login):
        if user_login in UserProfiles:
            user_profile = UserProfiles[user_login]
            
            new_real_name = self.get_body_argument("real_name")
            new_dob = self.get_body_argument("dob")

            if new_real_name in [profile.get("Real Name") for profile in UserProfiles.values() if profile.get("Login") != user_login]:
                self.write("Name must be unique")
                return

            user_profile["Real Name"] = new_real_name
            user_profile["DOB"] = new_dob

            profile_picture = self.request.files.get("profile_picture", None)
            if profile_picture:
                profile_picture_data = profile_picture[0]["body"]
                images_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../images"))
                with open(os.path.join(images_directory, f"{user_login}.png"), "wb") as f:
                    f.write(profile_picture_data)

            self.redirect(f"/profile/{user_login}")
        else:
            self.write("Login not found")