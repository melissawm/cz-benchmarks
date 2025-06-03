# Configuration file for the Sphinx documentation builder.
import os
import sys
import toml

sys.path.insert(0, os.path.abspath("../../src"))
with open("../../pyproject.toml", "r") as f:
    config = toml.load(f)

latest_version = config["project"]["version"]

project = "cz-benchmarks"
copyright = "2025, Chan Zuckerberg Initiative"
author = "Chan Zuckerberg Initiative"
release = str(latest_version)

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
    "sphinx_autodoc_typehints",
    "sphinx.ext.githubpages",
    "myst_nb",
    "sphinxcontrib.mermaid",
    "autoapi.extension",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx_immaterial",
    "sphinx_external_toc",
    "sphinx_design",
]

viewcode_follow_imported_members = True
autosummary_generate = True

autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]
autoapi_dirs = ["../../src/"]
# , '../../docker/geneformer',
# '../../docker/scgenept',
# '../../docker/scgpt',
# '../../docker/scvi',
# '../../docker/uce']
autoapi_type = "python"
autoapi_add_toctree_entry = False
autoapi_keep_files = True

napoleon_google_docstring = True
napoleon_numpy_docstring = True

myst_fence_as_directive = ["mermaid"]

mermaid_d3_zoom = True

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "linkify",
    "colon_fence",
]
myst_heading_anchors = 4

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "anndata": ("https://anndata.readthedocs.io/en/latest/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "scanpy": ("https://scanpy.readthedocs.io/en/stable/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_immaterial"
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
    "site_url": "https://chanzuckerberg.github.io/cz-benchmarks",
    "repo_url": "https://github.com/chanzuckerberg/cz-benchmarks/",
    "repo_name": "CZ Benchmarks Documentation",
    "edit_uri": "blob/main/docs/source",
    "globaltoc_collapse": False,
    "features": [
        "toc.follow",
        "toc.sticky",
        "navigation.tabs",
        "navigation.tabs.sticky",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "indigo",
            "accent": "blue",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "indigo",
            "accent": "blue",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    "font": {
        "text": "Inter",  # used for all the pages' text
        "code": "Roboto Mono",  # used for literal code blocks
    },
    # "version_dropdown": True,
    # "version_info": [
    #     {
    #         "version": "dev", # version number or path
    #         "title": "Stable (latest)", # title to be displayed in the dropdown
    #         "aliases": ["stable"], # list of aliases for the version
    #     },
    #     {
    #         "version": "v4.0",
    #         "title": "v4.0",
    #         "aliases": [""],
    #     },
    # ],
}

html_static_path = ["_static"]

source_suffix = [".rst", ".md"]

external_toc_path = "_toc.yml"
external_toc_exclude_missing = True

autodoc_type_aliases = {
    "BaseDataset": "czbenchmarks.datasets.BaseDataset",
    "Organism": "czbenchmarks.datasets.types.Organism",
}

inheritance_graph_attrs = dict(
    rankdir="LR", size='"18.0, 28.0 "', fontsize=16, ratio="expand", dpi=96
)

inheritance_node_attrs = dict(
    shape="box",
    fontsize=16,
    height=1,
    color="lightblue",
    style="filled",
    fontcolor="black",
)

inheritance_edge_attrs = dict(color="gray", arrowsize=1.2, style="solid")

html_css_files = ["custom.css"]

# html_js_files = [
#     "https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js",
# ]
