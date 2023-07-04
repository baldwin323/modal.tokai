```python
from setuptools import setup, find_packages

setup(
    name='OnlyfansManagerAI',
    version='1.0.0',
    url='https://github.com/yourusername/OnlyfansManagerAI',
    author='Author Name',
    author_email='author@gmail.com',
    description='An advanced chatbot application designed to assist creators on the Onlyfans platform.',
    packages=find_packages(),    
    install_requires=[
                      'numpy',
                      'pandas',
                      'scikit-learn',
                      'tensorflow',
                      'keras',
                      'nltk',
                      'flask',
                      'requests',
                      'beautifulsoup4',
                     ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
```