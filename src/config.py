from decouple import config

class DefaultDevelopmentConfiguration():
    DEBUG = True
    CORS_HEADERS = 'Content-Type'

configuration = {
    'development' : DefaultDevelopmentConfiguration
}