from distutils.core import setup

setup(
    name='TOR_Traffic_reporter',
    version='0.1.0',
    author='Charlie Algert',
    author_email='algertc*at*gmail*dot*com',
    packages=['TOR_TR'],
    url='https://github.com/algertc/TOR_Traffic_Reporter',
    license='LICENSE.txt',
    description='TOR Relay traffic monitoring, logging, and reporting',
    long_description=open('../README.txt').read(),
    install_requires=[
        "bidict >= 0.21.4",
        "certifi == 2021.10.8",
        "charset-normalizer == 2.0.12",
        "controller == 0.1.0",
        "idna == 3.3",
        "pip == 21.1.2",
        "python-engineio == 4.3.1",
        "python-socketio == 5.5.2",
        "requests == 2.27.1",
        "setuptools == 57.0.0",
        "stem == 1.8.0",
        "urllib3 == 1.26.8",
        "wheel == 0.36.2",
        "mysql-connector == 2.2.0",
    ],
)