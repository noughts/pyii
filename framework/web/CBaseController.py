import logging
from google.appengine.ext.webapp import template
from pyii.Pyii import Pyii


class CBaseController:

	def renderFile( self, viewFile, data=None ):
		Pyii.out.write( template.render( viewFile, data ) );
	
	
	
