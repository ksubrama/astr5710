conda init powershell
# Fixup profile.
conda create -n astro 
conda activate astro
conda config --add channels defaults --env
conda install -n astro scipy astropy jupyter ipython matplotlib

# As user
jupyter notebook
