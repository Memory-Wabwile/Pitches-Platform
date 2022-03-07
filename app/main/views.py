from flask import render_template,request,redirect,url_for,abort
from ..models import User
from ..models import User, Pitches,Comment,Upvote,Downvote
from . import main
from flask_login import current_user, login_required 
from .forms import UpdateProfile
from .. import db,photos

@main.route('/')
def index():
    '''
    function that returns the index page and its data
    '''
    Interview=Pitches.query.filter_by(category='Interview').all()
    Promotion=Pitches.query.filter_by(category='Promotion').all()
    Products = Pitches.query.filter_by(category='Products').all()
    PickupLines = Pitches.query.filter_by(category='PickupLines').all
    Sports = Pitches.query.filter_by(category='Sports').all()
    Entertainment = Pitches.query.filter_by(category='Entertainment').all()

    return render_template('index.html', Interview=Interview , Promotion=Promotion, Products=Products,PickupLines=PickupLines, Sports=Sports, Entertainment=Entertainment)

@main.route('/pitch')
@login_required
def pitch():
    pitch = Pitches.query.all()
    votes = Upvote.query.all()
    user = current_user
    return render_template('pitch.html' , pitch=pitch , votes=votes,user=user)



@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)