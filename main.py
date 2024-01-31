import os
import tornado.web
import asyncio
from userProfiles import UserProfileHandler

def makeApp():
    endpoints = [
        (r"/profile/(\w+)", UserProfileHandler),
(r"/images/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "../images")})
    ]
    template_path = os.path.join(os.path.dirname(__file__), "../html")  
    app = tornado.web.Application(endpoints, template_path=template_path)
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()
