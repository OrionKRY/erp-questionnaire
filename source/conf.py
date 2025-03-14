# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

# Project information
project = 'ERP Subsystem Discovery'
copyright = '2025, KR'
author = 'KR'
release = '0.1'

# General configuration
extensions = [
        "sphinx.ext.intersphinx",  # Ensures intersphinx is enabled
        "sphinx.ext.todo",  # Enables TODO notes (can be removed if not needed)
        "sphinx.ext.viewcode",  # Shows highlighted source code if needed
]

# Set theme to Furo
html_theme = "furo"
html_static_path = ["_static"]

# Theme options for Furo
# Hide "Made with Sphinx" footer text
html_show_sphinx = False
html_theme_options = {
    "sidebar_hide_name": False,  # Show project name in the sidebar
    "footer_icons": [],
    "light_css_variables": {  
        "color-footer-text": "transparent",  # Hides footer text
        "color-footer-background": "transparent",  # Makes background blend in
        "analytics_id": "G-XXTB5Q05GY"  # Replace with your actual Google Analytics ID
    },
}

# Use the custom footer template
html_context = {
    "footer_template": "_templates/footer.html"
}

# Ensure the templates folder is used
html_templates_path = ["_templates"]

# GitHub Pages settings
extensions.append("sphinx.ext.githubpages")  # Required for GitHub Pages