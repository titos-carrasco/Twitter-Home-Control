#!/usr/bin/env python
#-*- coding: utf-8 -*-

from TwitterBot import TwitterBot
from HomeBot import HomeBot

class MyApp():
    def __init__( self, keys_filename, board_port ):
        consumer_key = ''
        consumer_secret = ''
        access_token_key = ''
        access_token_secret = ''
        with open( keys_filename, "r" ) as keys_file:
            for line in keys_file:
                ( key, value ) = line.rstrip( "\n" ).strip().split( "=" )
                if( key == 'CONSUMER_KEY' ):
                    consumer_key = value
                elif( key == 'CONSUMER_SECRET' ):
                    consumer_secret = value
                elif( key == 'ACCESS_TOKEN_KEY' ):
                    access_token_key = value
                elif( key == 'ACCESS_TOKEN_SECRET' ):
                    access_token_secret = value

        self.homeBot = HomeBot( board_port )
        self.twitterBot = TwitterBot( consumer_key, consumer_secret, access_token_key, access_token_secret )

    def run( self ):
        self.twitterBot.run( self.homeBot )

###
MyApp( "Keys", "/dev/ttyACM0" ).run()

