@echo off
setlocal enabledelayedexpansion

set PACKAGE_NAME=cengal

set VS2019_PYTHONS=Python38 Python39 Python310 PyPy39 PyPy310

rem Define Python version to wheel tag mapping
set "tag_Python38=cp38"
set "tag_Python39=cp39"
set "tag_Python310=cp310"
set "tag_PyPy39=pp39"
set "tag_PyPy310=pp310"

if exist "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvars64.bat" (
    set "VS2019_PATH=C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
) else (
    echo Visual Studio 2019 not found.
    exit /b 1
)

rmdir /s /q  .\build
rmdir /s /q  .\dist
rmdir /s /q  .\sdist
rmdir /s /q  .\wheel
rmdir /s /q  .\wheelhouse

for %%P in (%VS2019_PYTHONS%) do call :build_wheels %%P "%VS2019_PATH%"

echo Wheels built successfully.

echo Uploading wheels to PyPI...
"%DevCompilers%\Python310\python.exe" -m pip install --upgrade pip
"%DevCompilers%\Python310\python.exe" -m pip install --upgrade setuptools
"%DevCompilers%\Python310\python.exe" -m pip install twine
"%DevCompilers%\Python310\python.exe" -m twine upload --repository pypi dist\%PACKAGE_NAME%-*.whl

echo Upload complete.
endlocal

EXIT /B %ERRORLEVEL%

:: Functions

rem Function to build wheels
:build_wheels
set "PYTHON_DIR=%DevCompilers%\%~1"
set "VSVARS_PATH=%~2"

set "WHEEL_TAG=!tag_%~1!"

"%PYTHON_DIR%\python.exe" -m pip install --upgrade pip
"%PYTHON_DIR%\python.exe" -m pip install --upgrade setuptools
"%PYTHON_DIR%\python.exe" -m pip install -r .\requirements.txt
"%PYTHON_DIR%\python.exe" -m pip wheel . -w dist

call rename_wheel.cmd !WHEEL_TAG!

goto :eof
