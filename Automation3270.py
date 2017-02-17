__version__ = '0.1'

from py3270 import Emulator
import time
import os
import signal

class Automation3270(object):
    '''Library for x3270 emulator automation. More information at http://x3270.bgp.nu/'''
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def Open_3270(self, hostname):
        '''Opens emulator. Provide the hostname as argument'''
        self.em = Emulator(visible=True)
        self.em.connect(str(hostname))

    def Open_New_3270(self):
        '''Closes all previous instances before starting'''
        self.process_name='wc3270.exe'
        self.get_pid=[self.item.split()[1] for self.item in os.popen('tasklist').read().splitlines()[4:] if self.process_name in self.item.split()]
        if self.get_pid[0]=="":
            self.em = Emulator(visible=True)
            self.em.connect('prda.bcpcorp.net')
        else:
            print 'Program already open'

    def Close_3270(self):
        '''Closes emulator'''
        self.pid_proc='wc3270.exe'
        self.pid= [self.item.split()[1] for self.item in os.popen('tasklist').read().splitlines()[4:] if self.pid_proc in self.item.split()]
        print "PID number is "+self.pid[0]
        os.kill(int(self.pid[0]), signal.SIGTERM)

    def Input_Text_on_Field(self, xpos, ypos, text):
        '''Writes text on field. Last parameters requires the lenght of the word'''
        self.em.fill_field(int(xpos),int(ypos),str(text),len(text)+2)

    def Send_String(self,text,xpos,ypos):
        '''Verifies if a given string exists'''
        self.em.string_found(text,int(xpos),int(ypos))

    def Keyboard_State(self):
        '''If the keyboard is unlocked, the letter U. If the keyboard is locked waiting for a response from the host, or if not connected to a host, the letter L'''
        print self.em.status.keyboard.capitalize()

    def wait_For_Field(self):
        '''Waits for execution'''
        self.em.wait_for_field()

    def Execute_Command(self,command):
        '''Executes custom commands. See more a thttp://x3270.bgp.nu/x3270-script.html'''
        self.em.exec_command(self,command)

    def Connection_State(self):
        '''If connected to a host, the string C(hostname). Otherwise, the letter N'''
        print self.em.status.connection_state.capitalize()

    def Get_String(self,xpos,ypos,lenght):
        '''Get String based on coordinates and lenght'''
        get_text=self.em.string_get(int(xpos),int(ypos),int(lenght))
        return get_text

    def Press_Enter(self):
        '''Presses Enter key'''
        self.em.send_enter()

    def Move_cursor(self,xpos,ypos):
        '''Moves cursor to specified coordinates'''
        self.em.move_to(xpos,ypos)

    def Take_Screenshot(self):
        '''Takes printscreen'''
        self.em.save_screen()

    def Pause_Test(self):
        '''Pauses Test at a given moment'''
        self.em.app.readline()

    def Send_F3(self):
        '''Simulates F3 key'''
        self.em.send_pf3()

    def Send_F4(self):
        '''Simulates F4 key'''
        self.em.send_pf4()

    def Send_F5(self):
        '''Simulates F5 key'''
        self.em.send_pf5()

    def Send_F6(self):
        '''Simulates F6 key'''
        self.em.send_pf6()

    def Send_F7(self):
        '''Simulates F7 key'''
        self.em.send_pf7()

    def Send_F8(self):
        '''Simulates F8 key'''
        self.em.send_pf8()
