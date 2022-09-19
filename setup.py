from setuptools import find_packages, setup

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pay/__init__.py
from payments import __version__ as version

setup(
	name="payments",
	version=version,
	description="Payments app for harpiya",
	author="Harpiya Software Technologies",
	author_email="hello@harpiya.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
