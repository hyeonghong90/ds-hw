
Data Wrangling
===============

Overview
---------------

This homework focuses on the first steps of getting data into a usable
form to start asking very simple questions.  We'll start asking more
complicated questions very soon!

The data for this assignment are messy.  Part of this assignment is
learning how to deal with this messiness.  You're not allowed to
change the underlying data, but you may have to resort to hacks to
resolve issues with the data.

This homework should not be very difficult if you can program in
Python.  If this homework is particularly challenging, you may not
have enough of a programming background for the course and need to
quickly get up to speed or consider another course.

You do not have to use the functions provided in the template file if
you feel they are not helpful to you.  However, you must produce the
CSV file exactly as this program does to submit to Kaggle.  If you do
use the functions provided in the template file, you want to make
sure the unit tests pass.

This what a successful set of unit tests will
look like:

    $ python3 tests.py
    .....
    ----------------------------------------------------------------------
    Ran 5 tests in 0.002s
    
    OK

If you do not get this result from running the tests and you use the
functions provided, you will not get a good grade.  The converse is
not true; passing all unit tests is not sufficient to getting a good
grade.  It just means you're on the right track.  Be sure to also look
at the test file carefully, as it will give you examples of how the
functions you need to implement are supposed to work.

As with all our homeworks, we will distribute the code via git.  You
are strongly encouraged to clone the repository so that if there are
changes in the assignment (e.g., to fix an error), you can quickly
merge your modified code using git.  If you find an error, Pull
requests are quite welcome!  Another advantage of cloning this
repository is that you'll also be able to very quickly download
subsequent homeworks by pulling from this upstream repository.

District Margins (15 points)
----------------------------

In the US, our legislature is made up of representatives of individual
*districts* (unlike proportional representation systems).  Some of
these districts are competitive, meaning that the winner of the
election is not a "sure thing" based on the voters in the districts.
However, for a variety of reasons, many of these districts are not
very competitive.  We're going to look at the 2014 election for the
114th congress and see which districts are competitive.  This also
gives us a chance to play around with some continuous data (well, sort
of; we'll assume votes are continuous even though you can't have a
fractional vote).

You will output to a file with the districts sorted by how competitive
they are (with the most competitive districts first).  If an election
is uncontested, the margin should be "100", in that the percentage
difference between the first place candidate and the second is 100.  

    $ python districts.py
    $ head district_margins.csv
    STATE,DISTRICT,MARGIN
    Arizona,2,0.07000000000000028
    California,7,0.7999999999999972
    Florida,2,1.1299999999999955
    Minnesota,8,1.3999999999999986
    Maryland,6,1.4500000000000028
    California,16,1.4599999999999937
    Washington,4,1.6200000000000045
    Texas,23,2.1000000000000014
    Iowa,1,2.280000000000001
    $ tail district_margins.csv
    Florida,12,100.0
    Pennsylvania,18,100.0
    Georgia,11,100.0
    Florida,25,100.0
    Pennsylvania,14,100.0
    Georgia,13,100.0
    Texas,4,100.0
    Pennsylvania,15,100.0
    Georgia,5,100.0
    Florida,14,100.0

To complete this assignment you'll need to complete three functions:
* district_margins
* all_states
* all_state_rows

You should not need to modify the "main" function.

Submit your CSV file to [Kaggle](https://www.kaggle.com/c/2018-414-wrangling) and it will score how well you did.

Writeup (10 points)
-----------------------

Finally, include a brief plain-text file (not PDF, not Word, just a
plain ASCII text file) that explains:
* The approach you took to solve the problem
* What external resources (if any) you used
* Any interesting observations you have from your results

Submitting Your Code
-----------------------

You'll need to submit your assignment (districts.py,
and writeup.txt) on
[ELMS](https://umd.instructure.com/courses/1239622) as an
upload.

Hints
-----------------------
* Only consider general elections for the 114th congress.  Ignore primaries and special elections for unexpired terms.
* The file may have errors.  For the purposes of this assignment, you are not allowed to edit the source data.  This may result in you having to resort to dirty hacks.
* You will need to understand the file to understand what's going on.  This is part of the assignment.  Wikipedia is your friend.
* Different states handle party affiliations differently.  Don't assume that if your code works for one state, it will work for all states.  
* Make sure you have the correct number of districts in your output file.  There are 438 voting districts, plus a handful of non-voting districts.
