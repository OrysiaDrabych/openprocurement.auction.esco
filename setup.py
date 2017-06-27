from setuptools import setup, find_packages
import os

version = '0.1.0'
install_requires = [
    'setuptools',
    'openprocurement.auction',
    'openprocurement.auction.worker'
]
extras_require = {
}
entry_points = {
    'console_scripts': [
        'auction_worker = openprocurement.auction.esco.cli:main',
    ]
}

setup(name='openprocurement.auction.esco',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
      ],
      keywords='',
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      license='Apache License 2.0',
      url='https://github.com/openprocurement/openprocurement.auction.esco',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openprocurement', 'openprocurement.auction'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points=entry_points,
      )
