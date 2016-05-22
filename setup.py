# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

# To parse requirements.txt
from pip.req import parse_requirements

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Parse and convert pip requirements objects.
install_reqs = parse_requirements(
    path.join(here, 'requirements.txt'),
    session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='connect4server',
    description='A sample Python project',
    long_description=long_description,
    url='https://github.com/SoftwareCraftsmanship2016Bristol/connect4server',
    author='SC2016 Bristol Crew',
    author_email='me@daogilvie.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment :: Board Games',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='connect4 game tournament server',
    packages=find_packages(exclude=['tests']),
    install_requires=reqs,
    extras_require={
        'dev': ['check-manifest'],
        'test': ['pytest', 'pytest-runner'],
    },

    package_data={
        # 'sample': ['package_data.dat'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],
    entry_points={
        'console_scripts': [
            'connect4server=connect4server.server:main',
        ],
    },
)
