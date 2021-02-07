# Corporate Land Ownership challenge submission

## Usage
```
landTree.py [-h] [-m {full_tree,from_root,expand}] company_id
```
Example:
```
.\landTree --mode=from_root S348465388962
```

## Modes
- ```full_tree``` - the default mode that renders the full tree that a company is part of and highlights it.
- ```from_root``` - renders the direct path from the root to the selected company.
- ```expand``` - renders the subtree for the selected company.

## Notes
- I have added two additional files to make it easier to test when developing.
- The script defaults to a ```full_tree``` mode if run without a mode.
- My understanding of what the modes should show is explained above.

## Additional considerations
Further interrogation of the data is needed but the one thing that stands out the most is making the scrip handle missing, malformed or wrong data as best as possible. I have added a basic validation method that can be improved to capture issues before the script is run. The class methods can also be coded in a more defensive way to avoid any catastrophic failures. Any other considerations I will be happy to discuss in person. 
