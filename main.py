import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


from tornado.options import define, options, parse_command_line




define("port", default=8888, help="Powered By Tornado", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):

    	

    	stories=[["test1","test.com"],["http://www.velphin.com/","velphin"]]

    

    	self.render("main_woving.html", head_title="Woving", stories=stories,)


class NewsHandler(tornado.web.RequestHandler):
	def get(self,story_id):
		self.write("you have request the story "+ story_id)







#class PostNews(tornado.web.RequestHandler):






def main():
    application = tornado.web.Application(
    	[
            (r"/", MainHandler),
            (r"/story/([0-100]+)",NewsHandler)
            ],

            )

    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



if __name__ =="__main__":
	main()
