from collections import defaultdict
from csv import DictReader, DictWriter
import heapq

kHEADER = ["DISTRICT", "MARGIN"]

def district_margins(state_lines):
    """
    Return a dictionary with districts as keys, and the difference in
    percentage between the winner and the second-place as values.

    @lines The csv rows that correspond to the districts of a single state
    """

    # Complete this function
    return dict((int(x["D"]), 25.0) for x in state_lines if x["D"] and
                not (x["D"] == "H" or " - " in x["D"]))

def all_states(lines):
    """
    Return all of the states (column "STATE") in list created from a
    CsvReader object.  Don't think too hard on this; it can be written
    in one line of Python.
    """

    # Complete this function
    return set(["Alabama"])

def all_state_rows(lines, state):
    """
    Given a list of output from DictReader, filter to the rows from a single state.

    @state Only return lines from this state
    @lines Only return lines from this larger list
    """

    # Complete/correct this function
    for ii in lines[:10]:
        yield ii

if __name__ == "__main__":
    # You shouldn't need to modify this part of the code
    lines = list(DictReader(open("../data/2014_election_results.csv")))
    output = DictWriter(open("district_margins.csv", 'w'), fieldnames=kHEADER)
    output.writeheader()

    summary = {}
    with open("train.csv", 'w') as train_file, \
         open("sub.csv", 'w') as sub_file:
      train = DictWriter(train_file, fieldnames=kHEADER)
      key = DictWriter(sub_file, fieldnames=kHEADER)
    
      train.writeheader()
      key.writeheader()

      for state in all_states(lines):
        state_districts = list(all_state_rows(lines, state))
        margins = district_margins(state_districts)

        for ii in margins:
            summary[(state, ii)] = margins[ii]

      for ii, mm in sorted(summary.items(), key=lambda x: x[1]):
        if ii[0] in ["Texas", "Arizona", "Maryland"]:
            train.writerow({"DISTRICT": "%s %i" % (ii[0], ii[1]), "MARGIN": mm})
        else:
            key.writerow({"DISTRICT": "%s %i" % (ii[0], ii[1]), "MARGIN": mm})
