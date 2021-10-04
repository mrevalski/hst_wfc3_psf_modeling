# Fit the data using either Gaussian2D or Moffatt2D functions on the interpolated images.
# e.g. fit_profile(model_type = 'gaussian/moffatt', input_data = image_array, fit_info = True/False)

def fit_profile_parallel(model_type, input_data, fit_info, star_ids, rpix, interp_grid_steps, max_iterations, verbal):

    import os
    import numpy
    from numpy import unravel_index
    import matplotlib.pyplot
    import astropy
    from astropy.io import fits
    from astropy.modeling import models
    from astropy.modeling import fitting

    x_centroids = []
    y_centroids = []

    # The data are the interpolated images.
    data = input_data

    # Create a finer grid of (x, y) coordinates for interpolation.
    x_z = numpy.around(numpy.linspace(1, (2*rpix), num=2*interp_grid_steps*rpix, endpoint=True), decimals=5)
    y_z = x_z

    # Declare the fitting algorith.
    fit_method = fitting.LevMarLSQFitter()
    amplitude = numpy.max(data)

    # Declare the type of model to fit.
    if model_type == 'gaussian':
        fit_model = models.Gaussian2D(amplitude, x_mean=interp_grid_steps*rpix, y_mean=interp_grid_steps*rpix)
    if model_type == 'moffatt':
        fit_model = models.Moffat2D(amplitude, x_0=interp_grid_steps*rpix, y_0=interp_grid_steps*rpix)

    # Generate the model array.
    ximg, yimg = numpy.indices(data.shape)

    # Fit the model to the data and evaluate.
    fit_result = fit_method(fit_model, ximg, yimg, data, maxiter=max_iterations)
    model = fit_result(ximg, yimg)
    residual = (data - model)

    # Find the locations of the peak flux value in the data and model.
    peak_location_data = numpy.unravel_index(numpy.argmax(data, axis=None), data.shape)
    peak_location_model = numpy.unravel_index(numpy.argmax(model, axis=None), model.shape)

    peak_location_data_x = x_z[peak_location_data[1]]
    peak_location_data_y = y_z[peak_location_data[0]]
    peak_location_model_x = x_z[peak_location_model[1]]
    peak_location_model_y = y_z[peak_location_model[0]]

    # Plot the data, model, and residuals side-by-side.
    figure, mysubplot = matplotlib.pyplot.subplots(1, 3, figsize=(11, 11))
    mysubplot[0].imshow(data, cmap='gray', vmin=0.0, vmax=numpy.amax(data)/100.0, origin='lower')
    mysubplot[1].imshow(model, cmap='gray', vmin=0.0, vmax=numpy.amax(model)/100.0, origin='lower')
    mysubplot[2].imshow(residual, cmap='gray', vmin=0.0, vmax=numpy.amax(residual)/100.0, origin='lower')
    matplotlib.pyplot.tight_layout()

    print('Star ID ' + str(int(star_ids)) + ':')
    print('Peak Data Flux Indices  (y,x):', peak_location_data)
    print('Peak Data Flux Center   (y,x):', peak_location_data_y, peak_location_data_x)
    print('Peak Model Flux Indices (y,x):', peak_location_model)
    print('Peak Model Flux Center  (y,x):', peak_location_model_y, peak_location_model_x)
    print('\n              DATA:                          MODEL:                           RESIDUAL:\n')
    matplotlib.pyplot.show()

    # Extract the model (x, y) centers.
    x_centroids.append(peak_location_model_x)
    y_centroids.append(peak_location_model_y)

    # Print detailed information of the fit if there is an error.
    if fit_info == True:
        print('fit_method.fit_info = ', fit_method.fit_info)

    # Announce completion.
    if verbal == True:
        os.system("say 'fitting complete'")

    # Return the lists of (x,y) centroids.
    return x_centroids, y_centroids

# End of function.
