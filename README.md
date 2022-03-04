# Graphics-Cards-List-Filter

The purpose of this mini project is to let user choose the specification they
require from a graphics card either for their graphics intensive jobs, researchs
or gaming in general.

It simple to use, just move the sliders in the sidebar and the graphics card list
will be filtered.

*Note: Only popular graphics cards from year 2010 are listed in this table!*

This project is done using **Python language** and the coding is written inside
**Spyder software** available in the [**Anaconda Navigator**](https://www.anaconda.com/).

The database source can be found [here](https://www.techpowerup.com/gpu-specs/). I have to tweak *a bit*
the database in the Excel to make sure the data is easy to read by the program and change certain columns format
from *object* to *int64*. Important since I cannot filter both *string* and *integer* without accidentally 
removing an entire column during the filter process.


