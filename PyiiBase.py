import logging;

class PyiiBase:
	
	_imports = {};
	_classes = {};
	_coreClasses = {
		'CUrlManager' : '.web.CUrlManager',
		'CHttpRequest' : '.web.CHttpRequest',
	};
	
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
	def createComponent( config, *args ):
		if( type(config)=="str" ):
			type_str = config;
			config = {};
		elif( "class" in config ):
			type_str = config["class"];
			del config["class"];
		else:
			raise Exception('Object configuration must be an array containing a "class" element.');
		
		
		try:
			klass = eval( type_str +"()" );
		except:
			PyiiBase.importc( type_str, True );
		
		n = len( args );
		if( n > 1 ):
			# ontheway
			pass;
		else:
			pass;
			klass = eval( type_str +"()" );
			object = klass;
		
		for key in config:
			PyiiBase.trace( config[key] );
		
		return object;







	@staticmethod
	def importc( alias, forceInclude=False ):
		# すでにインポートされている場合
		if( alias in PyiiBase._imports ):
			return PyiiBase._imports[alias];
		
		try:
			klass = eval( alias +"()" );
			PyiiBase._imports[alias] = alias;
			return PyiiBase._imports[alias];
		except:
			pass;
		
		# シンプルなクラス名の場合
		if( not "." in alias ):
			if( forceInclude==True and PyiiBase.autoload(alias) ):
				PyiiBase._imports[alias] = alias;
			return PyiiBase._imports[alias];
		
		





	@staticmethod
	def autoload( className ):
		if( className in PyiiBase._coreClasses ):
			exec "from pyii.framework"+ PyiiBase._coreClasses[className] +" import "+ className in globals();
		elif( className in PyiiBase._classes ):
			# ontheway
			exec "from pyii";
		else:
			# ontheway
			pass;
		return True;




	@staticmethod
	def trace( msg, caterogy="application" ):
		logging.info( msg );










