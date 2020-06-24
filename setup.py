import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cellpose",
    version="0.0.2.8",
    license="BSD",
    author="Marius Pachitariu and Carsen Stringer",
    author_email="stringerc@janelia.hhmi.org",
    description="anatomical segmentation algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MouseLand/cellpose",
    packages=setuptools.find_packages(),
    install_requires = ['numpy', 'scipy', 'natsort',
                        'tqdm', 'numba', 'opencv-python-headless'],
    extras_require = {
      "default": [
        'mxnet_mkl',
        'matplotlib',
        'scikit-image',
        'Pillow<=7.0.0'
      ],
      "mxnet": ["mxnet"],
      "mxnet_mkl": ["mxnet_mkl"],
      "docs": [
        'sphinx>=3.0',
        'sphinxcontrib-apidoc',
        'sphinx_rtd_theme',
      ],
      'gui': [
        'pyqtgraph==0.11.0rc0', 
        'PyQt5', 
        'google-cloud-storage'
        ]
    },
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ),
)
