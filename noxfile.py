# -*- coding: utf-8 -*-

from nox_poetry import session


@session
def tests(session):
    session.install(".", "pytest")
    session.run("pytest")


@session
def lint(session):
    session.install("flake8")
    session.run("flake8")
