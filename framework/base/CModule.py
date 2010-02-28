from pyii.Pyii import Pyii;

class CModule:
	
	
	
	def __init__( self ):
		print( "Cmodule" );
		self._components = {};
		self._componentConfig = {};

	
	
	def setComponents( self, components ):
		for key in components:
			component = components[key];
			if( key in self._componentConfig ):
				self._componentConfig[key].update( component );
			else:
				self._componentConfig[key] = component;


	def getComponent( self, id, createIfNull=True ):
		if( id in self._components ):
			return self._components[id];
		elif (id in self._componentConfig) and (createIfNull==True):
			config = self._componentConfig[id];
			del self._componentConfig[id];
			if (not "enabled" in config) or (config["enabled"]):
				Pyii.trace( "Loading "+ id +" application component", 'system.web.CModule' );
				if( "enabled" in config ):
					del config["enabled"];
				component = Pyii.createComponent( config );
				component.init();
				self._components[id] = component;
				return self._components[id];



