from setuptools import setup, find_packages

setup(
    name='django-atlas',
    version='0.1',
    description='Geolocation models, data and tools using GeoDjango',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/Rizziepit/django-atlas',
    packages = find_packages(),
    install_requires = [
        'django<1.7',
        'django-tastypie>=0.10,<0.12',  # 0.12 requires Django 1.7
        'django-photologue>=3.1',
        'django-category',
    ],
    include_package_data=True,
    tests_require=[
        'django-setuptest>=0.1.4',
        'psycopg2',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
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
