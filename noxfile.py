# -*- coding: utf-8 -*-

from nox_poetry import session, Session


@session
def black(session: Session):
    """Run black code formatter."""
    session.install("black")
    session.run("black", ".")


@session
def lint(session: Session):
    """Lint using flake8."""
    session.install(
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
        "darglint",
    )
    session.run("flake8", ".")


@session
def mypy(session: Session):
    """Type check using mypy."""
    session.install("mypy", "pytest")
    session.run("mypy", ".")


@session
def tests(session: Session):
    """Run the test suite."""
    session.install(".", "pytest")
    session.run("pytest", ".")


@session()
def coverage(session: Session) -> None:
    """Upload coverage data."""
    session.install("coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)


@session
def docs(session: Session):
    """Build the documentation."""
    session.install("sphinx", "sphinx_rtd_theme", "sphinx-autodoc-typehints")
    session.run("sphinx-build", "docs", "docs/_build")
