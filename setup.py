from setuptools import setup, find_packages

requires = []

setup(
    name='invento',
    version='0.1.0',
    description='Managing events with ease',
    author='',
    author_email='',
    url='https://www.github.com/ivcg/invento',
    license='MIT',
    install_requires=requires,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': [
            'invento=invento.commands:main',
        ]
    },
)

