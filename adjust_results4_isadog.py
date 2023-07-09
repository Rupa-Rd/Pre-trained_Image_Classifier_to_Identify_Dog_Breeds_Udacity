#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Roopa Dharshini
# DATE CREATED:   07-Jul-2023                              
# REVISED DATE: 09-Jul-2023
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if the classifier correctly
    classified images 'as a dog' or 'not a dog' especially when not a match.
    Demonstrates if the model architecture correctly classifies dog images even
    if it gets the dog breed wrong (not a match).

    Parameters:
    - results_dic: Dictionary with 'key' as the image filename and 'value' as a list.
                   The list contains the following items:
                   index 0 = pet image label (string)
                   index 1 = classifier label (string)
                   index 2 = 1/0 (int) where 1 = match between pet image and classifier labels,
                             and 0 = no match between labels
    - dogfile: A text file that contains names of all dogs from the classifier function and
               dog names from the pet image files.

    Returns:
    - None (results_dic is a mutable data type, so no return is needed)
    """

    # Creates dognames dictionary for quick matching to results_dic labels
    dognames_dic = {}

    # Reads in dognames from file, 1 name per line
    with open(dogfile, "r") as infile:
        # Process each line in file
        for line in infile:
            # Process line by removing newline character and adding it to dognames_dic
            dognames_dic[line.rstrip()] = 1

    # Iterate through results_dic to determine if labels are dogs
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        # Check if the pet label is a dog
        if pet_label in dognames_dic:
            results_dic[key].append(1)  # Pet Image Label is-a-dog
        else:
            results_dic[key].append(0)  # Pet Image Label is-NOT-a-dog

        # Check if the classifier label is a dog
        if classifier_label in dognames_dic:
            results_dic[key].append(1)  # Classifier Label is-a-dog
        else:
            results_dic[key].append(0)  # Classifier Label is-NOT-a-dog
