import asyncio
import tornado.web
from tornado.options import define

define("port", default=8888)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("/Volumes/files/Python/rostelekom/frontend/index.html", index=None)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/FormHandler", FormHandler)
    ],)


class FormHandler(tornado.web.RequestHandler):
    async def post(self):
        data = self.request.body_arguments
        print(data)
        self.render("/Volumes/files/Python/rostelekom/frontend/index.html")
        return data


async def main():
    app = make_app()
    app.listen(8888)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
