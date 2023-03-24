#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for pafy.

https://github.com/mps-youtube/pafy

python setup.py sdist bdist_wheel

"""

from setuptools import setup
from pafy import __version__


def install_deps():
    """
    FROM hnykda ON GITHUB: https://github.com/pypa/pip/issues/3610#issuecomment-356687173
    Reads requirements.txt and preprocess it
    to be feed into setuptools.

    This is the only possible way (we found)
    how requirements.txt can be reused in setup.py
    using dependencies from private github repositories.

    Links must be appendend by `-{StringWithAtLeastOneNumber}`
    or something like that, so e.g. `-9231` works as well as
    `1.1.0`. This is ignored by the setuptools, but has to be there.

    Warnings:
        to make pip respect the links, you have to use
        `--process-dependency-links` switch. So e.g.:
        `pip install --process-dependency-links {git-url}`

    Returns:
         list of packages and dependency links.
    """
    default = open('requirements.txt', 'r').readlines()
    new_pkgs = []
    links = []
    for resource in default:
        if 'git+ssh' in resource:
            pkg = resource.split('#')[-1]
            links.append(resource.strip() + '-9876543210')
            new_pkgs.append(pkg.replace('egg=', '').rstrip())
        else:
            new_pkgs.append(resource.strip())
    return new_pkgs, links

pkgs, new_links = install_deps()

setup(
    name='pafy',
    packages=['pafy'],
    scripts=['scripts/ytdl'],
    version=__version__,
    description="Retrieve YouTube content and metadata",
    keywords=["pafy", "API", "YouTube", "youtube", "download", "video"],
    author="np1",
    author_email="np1nagev@gmail.com",
    url="https://github.com/mps-youtube/pafy/",
    download_url="https://github.com/mps-youtube/pafy/tags",
    extras_require={
        'youtube-dl-backend': ["youtube-dl"],
    },
    install_requires=pkgs,
    dependency_links=new_links,
    package_data={"": ["LICENSE", "README.rst", "CHANGELOG", "AUTHORS"]},
    include_package_data=True,
    license='LGPLv3',
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 "
        "(LGPLv3)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS 9",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows XP",
        "Operating System :: Microsoft :: Windows :: Windows Vista",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Multimedia :: Sound/Audio :: Capture/Recording",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Video",
        "Topic :: Internet :: WWW/HTTP"],
    long_description=open("README.rst").read()
)
