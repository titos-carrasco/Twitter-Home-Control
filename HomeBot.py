#-*- coding: utf-8 -*-

import time
from espeak import espeak
import pyfirmata

class HomeBot:
    def __init__( self, board_port ):
        try:
            self.board = pyfirmata.Arduino( board_port )
        except:
            self.board = None

    def speak( self, text ):
        espeak.synth( text )
        while( espeak.is_playing() ):
            time.sleep( 0.1 )

    def run( self, cmd_id, cmd_date, cmd_from, cmd_to, cmd ):
        if( self.board == None ):
            return False
        cmd = cmd.lower()
        if( cmd == "encender led de prueba" ):
            self.speak( "Encendiendo LED de prueba.")
            self.board.digital[13].write( 1 )
        elif( cmd == "apagar led de prueba" ):
            self.speak( "Apagando LED de prueba.")
            self.board.digital[13].write( 0 )
        elif( cmd == "animar led de prueba" ):
            self.speak( "Animando LED de prueba.")
            for i in range( 20 ):
                self.board.digital[13].write( 1 )
                time.sleep( 0.05 )
                self.board.digital[13].write( 0 )
                time.sleep( 0.05 )
        elif( cmd == "shutdown" ):
            self.speak( "El sistema está siendo apagado.")
        else:
            return False
        return True
