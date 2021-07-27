# hst_wfc3_psf_modeling
A Jupyter Notebook that extracts, aligns, and stacks stars from HST WFC3 images to generate PSF models.

This Jupyter Notebook was created by Dr. Mitchell Revalski to generate Point Spread Function (PSF) models for Hubble Space Telescope (HST) Wide Field Camera 3 (WFC3) data. The user may select from two types of PSF modeling methodologies depending on their science goals. The two modeling options are:

Stellar: The code will generate a PSF model by stacking stars extracted from a drizzled science image. This requires a Source Extractor type catalog, or a list of (x,y) coordinates, that correspond to the stars the user would like to stack. The user may set a variety of selection criteria and manually exclude objects.

Empirical: The code will generate a PSF model by stacking STScI PSFs from a drizzle created using Varun Bajaj's *wfc3tools* make_model_star_image(). This requires a list of PSF coordinates generated using make_model_star_image(), or a list of (x,y) coordinates corresponding to the model positions in the drizzle.

See: [https://github.com/Vb2341/wfc3tools](https://github.com/Vb2341/wfc3tools)  and  [ISR WFC3 2016-12: Empirical Models for the WFC3/IR PSF - Jay Anderson - Mar 17, 2016](https://www.stsci.edu/files/live/sites/www/files/home/hst/instrumentation/wfc3/documentation/instrument-science-reports-isrs/_documents/2016/WFC3-2016-12.pdf)

The second decision is for the user to select whether to create a PSF model of the entire image, or create independent PSF models of the inner and outer portions of their science image. This is useful for mosaics with a longer effective exposure time in the center and a shorter exposure time near the edges.

Please send questions, comments, and suggestions to Mitchell Revalski. Thank you, and have a nice day!
