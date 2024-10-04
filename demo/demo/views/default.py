from pyramid.view import view_config


@view_config(route_name='home', renderer='demo:templates/h1.jinja2')
def my_view(request):
    return {}
