from setuptools import setup,find_packages

setup(name='OpenGL-Sandbox',
    version='0.1',
    description='',
    url='http://xiacon.tk',
    author='DeaSTL',
    author_email='doomlaboratory@gmail.com',
    license='',
    packages=find_packages(),
    install_requires=[
          'numpy',
          'pygame',
          'pyglet',
          'opensimplex'
      ],
    zip_safe=False,
)
