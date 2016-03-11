from system.core.router import routes

routes['default_controller'] = 'Whats'

routes['/showgeocode']='Whats#getallgeocode'

routes['/events']= 'Whats#event'

routes['POST']['/create_user']='Whats#create_user'

routes['POST']['/create_event']='Whats#create_event'

routes['/getcategorygeocode/<categoryid>'] = 'Whats#getcategorygeocode'

routes['POST']['/login']='Whats#login_user'

routes['/logout']='Whats#logout'

routes['/search/<searchinput>']='Whats#search'

routes['POST']['/sendsms']='Whats#sendsms'