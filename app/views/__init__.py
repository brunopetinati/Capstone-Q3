from flask import Flask


def init_app(app: Flask):
    
    from app.views.projetos_views import bp_projetos
    from app.views.integrantes_view import bp_integrantes
    from app.views.auth_view import bp
    from app.views.home_view import bp_home
    from app.views.token_view import bp_token
    from app.views.solicitacoes_view import bp_solicitacoes
    from app.views.register_view import bp_register

    app.register_blueprint(bp_projetos)
    app.register_blueprint(bp_integrantes)
    app.register_blueprint(bp)
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_token)
    app.register_blueprint(bp_solicitacoes)
    app.register_blueprint(bp_register)