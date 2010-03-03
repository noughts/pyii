from pyii.framework.base.CApplicationComponent import CApplicationComponent;
import cgi;
import os;

class CUrlManager( CApplicationComponent ):
	
	GET_FORMAT = 'get';
	PATH_FORMAT = "path";
	
	def init( self ):
		self._urlFormat = CUrlManager.GET_FORMAT;
		self.caseSensitive = None;
		#
		CApplicationComponent.__init__( self );
		self.processRules();
	
	
	
	def processRules( self ):
		pass;
	
	
	def parseUrl( self, request ):
		if( self.getUrlFormat()==CUrlManager.PATH_FORMAT  ):
			# ontheway
			pass;
		
#		form = cgi.FieldStorage();
#		form.getvalue("hogehoge")
#		print( os.environ["PATH_INFO"] );
#		print( os.environ["QUERY_STRING"] );
		if( os.environ["QUERY_STRING"] == "" ):
			return os.environ["PATH_INFO"];
		else:
			return os.environ["PATH_INFO"] +"?" + os.environ["QUERY_STRING"];

	
	
	
	def getUrlFormat( self ):
		return self._urlFormat;
	
	