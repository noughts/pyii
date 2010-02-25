class Pyii:
	
	MainHandler = None;
	
	def __init__( self ):
		print "constructor"
	
	
	
	
	# ブラウザに表示
	@staticmethod
	def write( content ):
		Pyii.MainHandler.response.out.write( content );
