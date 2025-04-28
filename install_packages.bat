@echo off

REM List of packages to install
set packages=django djangorestframework psycopg2 pillow

REM Install each package using pip
for %%p in (%packages%) do (
    pip install %%p
)
