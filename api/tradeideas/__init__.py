from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('tradeideas.mockups')
    config.scan()
    return config.make_wsgi_app()
