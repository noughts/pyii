import logging;

class PyiiBase:
	
	_imports = {};
	
	@staticmethod
	def createWebApplication():
		logging.getLogger().setLevel( logging.DEBUG );
		return PyiiBase.createApplication( "CWebApplication" );
	
	@staticmethod
	def createApplication( className ):
		exec "import pyii.framework.web."+ className;
		klass = eval( "pyii.framework.web."+ className +"."+ className +"()" );
		return klass;

	@staticmethod
	def createComponent( config ):
		if( type(config)=="str" ):
			type_str = config;
			config = {};
		elif( "class" in config ):
			type_str = config["class"];
			del config["class"];
		else:
			raise Exception('Object configuration must be an array containing a "class" element.');
		
		print( PyiiBase );
		#PyiiBase.importc( type_str );
		
#		klass = eval( className +"()" );
#		object = klass;



	@staticmethod
	def importc( alias, forceInclude=False ):
		if( alias in self ): 





	@staticmethod
	def trace( msg, caterogy="application" ):
		logging.info( msg );










