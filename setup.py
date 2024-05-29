"""Setup the project"""

from setuptools import setup, find_packages

setup(
    name='dj-translator',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django module for text translation using local editor.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/amiroooamiran/django-translator',
    author='Amirhossein Amiran',
    author_email='amiran.amirhossein@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 5.0', 
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=5.0',
        'django-tinymce',
    ],
)
