# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import datetime
import django

sys.path.insert(0, os.path.abspath(".."))
os.environ["DATABASE_URL"] = "sqlite:///readthedocs.db"
os.environ["REDIS_URL"] = "redis://dummy:dummy@localhost:6379/0"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

if True:
    from config import app

current_year = datetime.datetime.now().year
if 2024 == current_year:
    date = current_year
else:
    date = "2024-{}".format(current_year)


project = app.name
copyright = f"{date}, {app.author_name}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "django": (
        "https://docs.djangoproject.com/en/4.2/",
        "https://docs.djangoproject.com/en/4.2/_objects/",
    ),
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
