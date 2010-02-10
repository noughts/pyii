import os
import sys
from google.appengine.ext.webapp import template
from pyii.framework.web.CBaseController import CBaseController


class CController( CBaseController ):
	
	# view ファイルのパスを返す
	def getViewFile( self, viewName ):
		path = os.path.abspath( "../protected/views/" + viewName );
		return path;
		
	
	def renderPartial( self, view, data=None ):
		viewFile = self.getViewFile( view );
		print template.render( viewFile, data )
	
	
	def render( self, view, data=None ):
		print "self";
	
	
	
	
	def renderText( self, text ):
		print text;
