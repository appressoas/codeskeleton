from setuptools import setup, find_packages


setup(
    name='codeskeleton',
    description='General purpose code skeleton solution.',
    version='1.0',
    author='Appresso AS',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": ['codeskeleton = codeskeleton.cli.codeskeleton_cli:main']
    }
)
