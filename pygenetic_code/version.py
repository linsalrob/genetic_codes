"""
Get the version number for the scripts
"""

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('pygenetic_code').version
except pkg_resources.DistributionNotFound as e:
    __version__ = 'unknown'
