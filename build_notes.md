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

