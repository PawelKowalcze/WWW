from flask import render_template, redirect, url_for, request, flash
from . import dashboard

@dashboard.route('/dashboard')
def home():
    return render_template('dashboard/dashboard.html')