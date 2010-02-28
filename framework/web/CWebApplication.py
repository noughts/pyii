from pyii.framework.base.CApplication import CApplication;

class CWebApplication( CApplication ):
	
	
	
	
	def __init__( self ):
		CApplication.__init__( self );
		self.catchAllRequest = None;
	
	
	def processRequest( self ):
		if type(self.catchAllRequest)=="list" and 0 in self.catchAllRequest:
			route = self.catchAllRequest[0];
			#TODO
		else:
			route = self.getUrlManager().parseUrl( self.getRequest() );
		self.runController( route );
