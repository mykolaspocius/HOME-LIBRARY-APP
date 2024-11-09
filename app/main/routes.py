from app.main import bp

@bp.route('/')
def index():
    return 'Pagina de inicio'

@bp.route('/login')
def login():
    return 'Login usuarios'

