def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('register','/register')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('add', '/add')
    config.add_route('ecardedit', '/ecardedit/{id}')
    config.add_route('my', '/my')
    config.add_route('ecarddelete', '/ecarddelete/{id}')
    config.add_route('ecard', '/ecard/{id}')



