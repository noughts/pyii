from pyii.framework.base.CApplication import CApplication;
from pyii.Pyii import Pyii;

class CWebApplication( CApplication ):
	
	def __init__( self ):
		self.defaultController = "site";
		self.catchAllRequest = None;
		self.controllerMap = {};
		
		CApplication.__init__( self );
	
	
	def processRequest( self ):
		if( (type(self.catchAllRequest)=="list") and (0 in self.catchAllRequest) ):
			route = self.catchAllRequest[0];
			#TODO
		else:
			route = self.getUrlManager().parseUrl( self.getRequest() );
		self.runController( route );
	
	
	def runController( self, route ):
		self.createController( route );
	
	
	def createController( self, route, owner=None ):
		if( owner is None ):
			owner = self;
		
		route = route.strip( "/" );
		if( route=="" ):
			route = self.defaultController;
		
		caseSensitive = self.getUrlManager().caseSensitive;		
		route += "/";
		while( route.find("/") >= 0 ):
			pos = route.find( "/" );
			id = route[0:pos];
			route = route[pos+1:len(route)];
			if( basePath is None ):
				if( id in owner.controllerMap ):
					if( owner==self ):
						_r1 = Pyii.createComponent( owner.controllerMap[id], id, None );
					else:
						_r1 = Pyii.createComponent( owner.controllerMap[id], id, owner );
						_r2 = self.parseActionParams( route );
					return [_r1, _r2];
				
				module = owner.getControllerPath();
				if( module != ):
		
		
		
		
			