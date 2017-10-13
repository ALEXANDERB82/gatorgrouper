""" GatorGrouper randomly assigns a list of students to groups """
"""Issue #2"""

from random import shuffle
import argparse
import itertools
import sys
#default values
from defaults import *
from read_student_file import student_list_length

def parse_gatorgrader_arguments(args):
    """ Parses the arguments provided on the command-line """
    gg_parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    gg_parser.add_argument(
        "--verbose",
        help="Display verbose diagnostic information",
        action="store_true")

    gg_parser.add_argument(
        "--group-size",
        help="Number of students in a group",
        type=int,
        default=DEFAULT_TEAM_SIZE,
        required=False)
    list_size = student_list_length()

    gg_parser.add_argument(
        "--students-file",
        help="File containing last name of students",
        type=str,
        default=DEFAULT_STUDENT_FILE,
        required=False)

    gg_arguments_finished = gg_parser.parse_args(args)

    return gg_arguments_finished
