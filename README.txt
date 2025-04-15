We have to create and activate a virtual environment in order to install Django,

To create new virtual environment:

	python -m venv myworld

This will set up a virtual environment, and create a folder named "myworld" with subfolders and files, like this:

	   myworld
  		Include
  		Lib
  		Scripts
  		.gitignore
  		pyvenv.cfg

Then you have to activate the environment, by typing this command:

Windows:

	myworld\Scripts\activate.bat

Unix/MacOS:

	source myworld/bin/activate