#!/usr/bin/env python
# encoding: UTF-8

import os
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

requirements = [
    "requests"
]

test_requirements = [
    "pylint",
    "black"
]

class install(_install):
    def run(self):
        print("Installing Nautilus Python extension...")
        src_file = "gsearch.py"
        dst_dir = os.path.join(
            os.path.expanduser('~'),".local/share/nautilus-python/extensions"
        )
        self.mkpath(dst_dir)
        dst_file = os.path.join(dst_dir, os.path.basename(src_file))
        self.copy_file(src_file, dst_file)
        print("Done.")

setup(
    name="Nautilus reverse Gsearch",
    version="1.1",
    description="A plugin to reverse search on Google image search from nautilus ",
    url="https://github.com/flavioelawi/gsearch-reverse-image-nautilus",
    license="GPL-2.0",
    author="Flavio Elawi",
    keywords="nautilus extension google reverse search image gnome",
    platforms=["Linux", "BSD"],
    python_requires='>3.5',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    tests_require=test_requirements,
    cmdclass={"install": install}
)
