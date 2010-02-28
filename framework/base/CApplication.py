from pyii.framework.base.CModule import CModule;

class CApplication( CModule ):
	
	
	def __init__( self ):
		CModule.__init__(self);
		self.registerCoreComponents();
	
	
	
	
	def run( self ):
		print "run";
		self.processRequest();
	
	
	def getUrlManager( self ):
		return self.getComponent( "urlManager" );
	def getRequest( self ):
		return self.getComponent( "request" );
	
	
	
	def registerCoreComponents( self ):
		components = {
			"coreMessages" : {
				'class' : 'CPhpMessageSource',
				'language' : 'en_us',
				'basePath' : "hoge",
			},
			"db" : {
				"class" : "CDbConnection"
			},
			"messages" : {
				"class" : "CPhpMessageSource"
			},
			"errorHandler" : {
				"class" : "CErrorHandler"
			},
			"securityManager" : {
				"class" : "CSecurityManager"
			},
			"statePersister" : {
				"class" : "CStatePersister"
			},
			"urlManager" : {
				"class" : "CUrlManager"
			},
			"request" : {
				"class" : "CHttpRequest"
			},
			"format" : {
				"class" : "CFormatter"
			}
		}
		self.setComponents( components );