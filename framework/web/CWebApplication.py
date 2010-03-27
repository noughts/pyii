from pyii.framework.base.CApplication import CApplication;
from pyii.Pyii import Pyii;

DIRECTORY_SEPARATOR = "/";

class CWebApplication( CApplication ):
	
	
	
	def __init__( self ):
		# メンバ変数初期化
		self.defaultController = "site";
		self.catchAllRequest = None;
		self.controllerMap = {};
		self._controllerPath = None;
		
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
		
		basePath = None;
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
				if( module is not None ):
					return self.createController( route, module );
		
		
		
		
		
	def getControllerPath( self ):
		if( self._controllerPath is not None ):
			return self._controllerPath;
		else:
			self._controllerPath = self.getBasePath() + DIRECTORY_SEPARATOR + "controllers";
			return self._controllerPath;

		
		
		
			