from flask import Blueprint, request, current_app, render_template
from http import HTTPStatus
from flask_login import login_required, current_user


bp_home = Blueprint("bp_home", __name__, url_prefix="/api")

@bp_home.route('/home', methods=["GET"])
@login_required
def home():
  return render_template('home.html',user = current_user)