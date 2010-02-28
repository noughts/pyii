import logging;
from pyii.PyiiBase import PyiiBase;

class Pyii( PyiiBase ):
	
	MainHandler = None;
	
	def __init__( self ):
		print "constructor"
	
	
	
	
	
	
	
	# ブラウザに表示
	@staticmethod
	def write( content ):
		Pyii.MainHandler.response.out.write( content );
	
	