# Graphics-Cards-List-Filter

The purpose of this mini project is to let user choose the specification they
require from a graphics card either for their graphics intensive jobs, researchs
or gaming in general.

It simple to use, just move the sliders in the sidebar and the graphics card list
will be filtered.

*Note: Only popular graphics cards from year 2010 are listed in this table!*

This project is done using **Python language** and the .py coding is written inside
**Spyder software** available in the [**Anaconda Navigator**](https://www.anaconda.com/).

The database source can be found [here](https://www.techpowerup.com/gpu-specs/). I have to tweak *a bit*
the .csv file in the Excel to make sure the data is easy to read by the program and convert certain columns format
from *object* to *int64*. Important since I cannot filter both *string* and *integer* in a column without accidentally 
removing an entire rows during the filter process.

The .py and .csv files is then uploaded here, **GitHub**, for the next step, turning this coding into *a web application*. 
(**Streamlit**)[https://streamlit.io/] is an incredible tool for begginer like me to create an application. It
really simple, it just require a GitHub account and a repository containing the project. Then register a **Streamlit** account
and allow the site to access the **GitHub** account and create a new application by picking a repository containing the .py file and
*voila*, an application is created!

