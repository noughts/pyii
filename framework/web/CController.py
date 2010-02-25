import os
import sys
import logging

from pyii.framework.web.CBaseController import CBaseController


class CController( CBaseController ):
	
	__name = "";
	layout = "main";

	def __init__( self, name ):
		self.__name = name;
		return;


	
	# view ファイルのパスを返す
	def getViewFile( self, viewName ):
		path = os.path.abspath( "../protected/views/"+ self.__name +"/"+ viewName +".html" );
		return path;
		
	# layout ファイルのパスを返す
	def getLayoutFile( self, layoutName ):
		path = os.path.abspath( "../protected/views/layout/"+ layoutName +".html" );
		return path;
		
		
	
	def renderPartial( self, view, data=None ):
		viewFile = self.getViewFile( view );
		self.renderFile( viewFile, data );
		
	
	
	def renderText( self, text ):
		layoutFile = self.getLayoutFile( self.layout );
		params = {
			'content': text,
		}
		self.renderFile( layoutFile, params );
	
	
	
	def render( self, view, data=None ):
		print "self";
	
	
	
	
