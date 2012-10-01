from setuptools import setup, find_packages

setup(
    name='django-atlas',
    version='0.0.1-beta',
    description='Geolocation models, data and tools using GeoDjango',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/Rizziepit/django-atlas',
    packages = find_packages(),
    dependency_links = [
        'http://github.com/praekelt/django-photologue/tarball/2.6.praekelt#egg=django-photologue-2.6.praekelt',
        'http://github.com/praekelt/django-photologue/tarball/2.7.praekelt#egg=django-photologue-2.7.praekelt',
    ],
    install_requires = [
        'django-tastypie',
        'django-photologue',
        'django-category',
    ],
    include_package_data=True,
    tests_require=[
        'django-setuptest',
    ],
    test_suite="setuptest.SetupTestSuite",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
