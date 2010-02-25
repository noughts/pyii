import logging
from google.appengine.ext.webapp import template
from pyii.Pyii import Pyii


class CBaseController:
	
	def __init__( self ):
		logging.info( "aaaaaaaaaaaaa" );
	
	def renderFile( self, viewFile, data=None ):
		Pyii.write( template.render( viewFile, data ) );
	
	
	
