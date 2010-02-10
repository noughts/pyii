import os
import sys
import logging

from google.appengine.ext.webapp import template
from pyii.framework.web.CBaseController import CBaseController


class CController( CBaseController ):
	
	__name = "";

	def __init__( self, name ):
		self.__name = name;
		return;


	
	# view ファイルのパスを返す
	def getViewFile( self, viewName ):
		path = os.path.abspath( "../protected/views/"+ self.__name +"/"+ viewName );
		logging.info( path );
		return path;
		
	
	def renderPartial( self, view, data=None ):
		viewFile = self.getViewFile( view );
		print template.render( viewFile, data )
	
	
	def render( self, view, data=None ):
		print "self";
	
	
	
	
	def renderText( self, text ):
		print text;
