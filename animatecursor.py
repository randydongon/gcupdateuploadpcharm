import threading
import time
import sys

class CursorAnimation(threading.Thread):
    def __init__(self):
        self.flag = True
        self.animation_char = "|/-\\"
        self.cursor='/-\|'        
        self.idx = 0
        threading.Thread.__init__(self)

    def run(self):
        
        while self.flag:
            sys.stdout.write(self.animation_char[self.idx % len(self.animation_char)])
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')            
            self.idx += 1
            

    def stop(self):
        self.flag = False

    
    

