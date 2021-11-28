# -*- coding: utf-8 -*-

import nox


@nox.session
def tests(session):
    session.run("poetry", "install")
    session.install("pytest")
    session.run("pytest")


@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8")
