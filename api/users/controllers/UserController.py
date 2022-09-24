import sys
from flask import render_template, redirect, url_for, request, abort
from api.users.models.User import User
from api.users import db, conn


def create_user():
    ...


def get_user(userId):
    ...


def update_user(userId):
    ...


def delete_user(userId):
    ...