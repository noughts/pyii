import logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from pyii.Pyii import Pyii

class MainHandler( webapp.RequestHandler ):

	def get( self, requestUri ):
		logging.getLogger().setLevel( logging.DEBUG );
		
		# ブラウザに正常にレンダリングするために、static prop に設定
		Pyii.out = self.response.out;
		print self.response;		
		
		#self.response.out.write( 'Hello world!' + requestUri )
		
		# myapp.appspot.com/ 以降についてきた文字列を分解
		if requestUri == "":
			controllerName = "Site"
			actionName = "index"
		else:
			ary = requestUri.split( "/" )
			controllerName = ary[0]
			if len( ary ) == 1:
				actionName = "index"
			else:
				if ary[1] == "":
					actionName = "index"
				else:
					actionName = ary[1]
		controllerName = controllerName.capitalize();
		actionName = actionName[0].capitalize() + actionName[1:100]; # actionName の先頭だけ大文字に。
		
		# Controller のインスタンス化
		controllerClassName = controllerName + "Controller";
		file = __import__( "protected.controllers", globals(), locals(), [controllerClassName] )
		klass = getattr( file, controllerClassName )
		constructorFunction = getattr( klass, controllerClassName )
		controller = constructorFunction( controllerName.lower() )
		
		# Controller の action 実行
		try:
			actionFunction = getattr( controller, "action" + actionName );
		except AttributeError:
			print "can' find "+ controllerClassName +".action"+ actionName;
		else:
			actionFunction();




def main():
	application = webapp.WSGIApplication( [(r'/(.*)', MainHandler)],debug=True )
	util.run_wsgi_app( application )


if __name__ == '__main__':
	main()
      