from setuptools import setup

setup(
    name='beets-usertag',
    version='0.1',
    description='beets plugin to support user defined keyword tags',
    long_description=open('README.md').read(),
    author='Ingo Fruend',
    author_email='github@ingofruend.net',
    url='https://github.com/igordertigor/beets-usertag',
    license='MIT',
    platforms='ALL',

    packages=['beetsplug'],

    install_requires=[
        'beets>=1.3.7',
        'futures',
    ],
)
