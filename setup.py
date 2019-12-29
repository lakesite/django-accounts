from setuptools import setup, find_packages


setup(
    name='django-accounts',
    version='0.1',
    description='A Django app template for accounts (login, logout, etc).',
    packages=find_packages(),
    zip_safe=False,

    author='Andy Duncan',
    author_email='andy@lakesite.net',
    license='MIT',
    url='https://github.com/lakesite/django-accounts',

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
