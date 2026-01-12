# Installing and building pygenetic codes

#### &copy; Rob Edwards 31/12/23 

> I have written this build from scratch using instructions from [Python packaging](https://packaging.python.org/en/latest/guides/section-build-and-publish/) 
> because I know it's time I should start using a `pyproject.toml` file. These are my notes from that proccess.

This package contains both python code that we want as an executable (`"console_scripts":
["pygenetic_code = pygenetic_code.cli:run"]`), C code that can be standalone (based on 
[get_orfs](https://github.com/linsalrob/get_orfs)), and C code that should be a module.

I use (well, I converted the build to use) [CMake](https://cmake.org/), I'm using 
[scikit-build-core](https://scikit-build-core.readthedocs.io/en/latest/)  as my backend, so I start with 

Because I'm using CMake and sci-kit-build, there is not that much else to do! You can essentially run

```python
pip install .
```

### Making a PyPi release

PyPI releases are automated through GitHub Actions using cibuildwheel to build manylinux wheels:

1. Create a new release on GitHub with a version tag (e.g., v0.21.2)
2. The `python-publish.yml` workflow will automatically:
   - Build manylinux wheels for CPython 3.10, 3.11, and 3.12 using cibuildwheel
   - Build a source distribution (sdist)
   - Run tests on the built wheels to verify they work
   - Upload both wheels and sdist to PyPI

The wheels are built using the manylinux2014 image, ensuring they have the proper `manylinux_2_14_x86_64` platform tag (not `linux_x86_64`) and are compatible with a wide range of Linux distributions.

For local testing of wheel building, you can use:
```bash
pip install cibuildwheel
cibuildwheel --platform linux
```

The built wheels will be in the `wheelhouse/` directory.

### Versioning

I am not 100% satisfied with versioning at the moment. 

There are several ways to get and use the version:

 - git has its own version that will be something like `0.15.dev7+gc8305d5.d20240103`
 - CMake uses the version in the build, but it requires a regexp like (`\d+\.\d+\.\d+\-.*`) so that doesn't work with the git versioning and breaks everything
 - pyproject.toml has a version which can be dynamic, but I can't (yet) get it to read from a file

At the moment, I'm using the `pyproject.toml` version string, and that is propogated to CMake. During build it is written to a file (`pygenetic_code/_version.py`) and we need to remember to increment it. 

Suggestions are welcome for improvements here.

