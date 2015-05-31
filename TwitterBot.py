#!/usr/bin/env python
#-*- coding: utf-8 -*-

from espeak import espeak
import time
from twython import TwythonStreamer
from HomeBot import HomeBot

class TwitterBot( TwythonStreamer ):
    def on_success( self, data ):
        if( 'direct_message' in data ):
            dm = data['direct_message']
            created_at = dm['created_at']
            id_str = dm['id_str']
            recipient_screen_name = dm['recipient_screen_name']
            sender_screen_name = dm['sender_screen_name']
            text = dm['text'].strip()
            print "%s, %s, %s, %s" % (id_str, created_at, sender_screen_name, recipient_screen_name  )
            print text
            if( self.homeBot.run( id_str, created_at, sender_screen_name, recipient_screen_name, text ) ):
                pass
            else:
                self.speak( "He recibido un comando inválido." )
                self.speak( text )

    def on_error( self, status_code, data ):
        print "Stream Error", status_code
        # self.disconnect()

    def speak( self, text ):
        espeak.synth( text )
        while( espeak.is_playing() ):
            time.sleep( 0.1 )

    def run( self, homeBot ):
        espeak.set_parameter( espeak.Parameter.Rate, 170 )
        espeak.set_parameter( espeak.Parameter.Volume, 100 )
        espeak.set_parameter( espeak.Parameter.Pitch, 0 )
        espeak.set_parameter( espeak.Parameter.Range, 99 )
        espeak.set_parameter( espeak.Parameter.Wordgap, 10 )
        espeak.set_voice( name="spanish-mbrola-2", gender=espeak.Gender.Female );
        self.homeBot = homeBot
        self.user();
