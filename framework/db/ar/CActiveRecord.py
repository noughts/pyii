import logging
from pyii.Pyii import Pyii
from google.appengine.ext import db

class CActiveRecord( db.Model ):
	
	def UserProperty( self ):
		pass;
	
	def save( self ):
		self.put();
	
	
	
