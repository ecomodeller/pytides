pytides
=======
## About
Pytides is small Python package for the analysis and prediction of tides. Pytides can be used to extrapolate the tidal behaviour at a given location from its previous behaviour. The method used is that of harmonic constituents, in particular as presented by P. Schureman in Special Publication 98. The fitting of amplitudes and phases is handled by Scipy's leastsq minimisation function. Pytides currently supports the constituents used by NOAA, with plans to add more constituent sets. It is therefore possible to use the amplitudes and phases published by NOAA directly, without the need to perform the analysis again (although there may be slight discrepancies for some constituents).

It is recommended that all interactions with pytides which require times to be specified are in the format of naive UTC datetime instances. In particular, note that pytides makes no adjustment for summertime or any other civil variations within timezones.

## Requirements
* Numpy
* Scipy

## Installation

```pip install pytides```


## Usage
Pytides is in its infancy, and hasn't yet been fully documented. The best way to get started would be to read [this example](https://github.com/sam-cox/pytides/wiki/Example-Pytides-Usage).

After that, you might try [making your own tide table](https://github.com/sam-cox/pytides/wiki/How-to-make-your-own-Tide-Table-using-Python-and-Pytides), where you can also find a method for handling timezones.

You can find information about using NOAA published Harmonic Constituents directly [here](https://github.com/sam-cox/pytides/wiki/How-to-use-the-NOAA%27s-published-Harmonic-Constituents-in-Python-with-Pytides).

If you want to know *how* Pytides works, it would be best to read *P. Schureman, Special Publication 98*. Alternatively, there is [my attempt](https://github.com/sam-cox/pytides/wiki/Theory-of-the-Harmonic-Model-of-Tides) to explain it on the wiki (although it's a little mathematical and not yet complete).
It is certainly possible to use Pytides successfully without any knowledge of its methods.

