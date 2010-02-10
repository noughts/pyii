from pyii.framework.web.CBaseController import CBaseController


class CController( CBaseController ):

	def render( self, view, data=None ):
		print "self"
	
	
	
	
	def renderText( self, text ):
		print text
