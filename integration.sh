cd package
python3 -m build # adds to the dist folder so it can be uploaded
python3 -m twine upload dist/* # uploads the dist folder
rm -r dist # removes built files. this lets this file be run again
cd src
rm -r CopperUI.egg-info # removes info from the src folder
echo "removed dist and egg-info packages. exiting..."
python3 -m pip install --upgrade copperui # first try to update
python3 -m pip install --upgrade copperui # second try to update