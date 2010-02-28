from pyii.framework.base.CApplicationComponent import CApplicationComponent;

class CHttpRequest( CApplicationComponent ):

	def init( self ):
		CApplicationComponent.__init__( self );
		self.normalizeRequest();

	def normalizeRequest( self ):
		pass;