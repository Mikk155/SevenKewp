import os

TOKEN = os.getenv('TOKEN')
VERSION = float(os.getenv('VERSION'))

abs = os.path.abspath( "" )

print( f'Releasing version "{VERSION}"')