from pyii.framework.base.CApplicationComponent import CApplicationComponent;

class CUrlManager( CApplicationComponent ):
	
	GET_FORMAT  ='get';
	
	def init( self ):
		self._urlFormat = CUrlManager.GET_FORMAT;
		#
		CApplicationComponent.__init__( self );
		self.processRules();
	
	
	
	def processRules( self ):
		pass;
	
	
	def parseUrl( self, request ):
		pass;
	
	
	
	
	def getUrlFormat( self ):
		return self._urlFormat;
	
	