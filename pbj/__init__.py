"""
short description of PBJ.

First PBJ try.
"""

# Add imports here
import bempp.api
import os
from pbj.electrostatics.solute import solute

PBJ_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
#WORKING_PATH = os.getcwd()
# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
