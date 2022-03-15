from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in efeoneweb/__init__.py
from efeoneweb import __version__ as version

setup(
	name="efeoneweb",
	version=version,
	description="website in efeone",
	author="efeone",
	author_email="athif.tp@efeone.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
