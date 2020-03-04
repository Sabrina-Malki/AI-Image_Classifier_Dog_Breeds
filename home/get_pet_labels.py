#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Sabrina M.
# DATE CREATED:  28/10/2019                                
# REVISED DATE: 03/11/2019
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir, path

# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    #The extension to add later to the filename (extension was taken with splitext)
    ext = '.jpg'
    results_dic = dict()
    filename_list_with_extension = listdir(image_dir)
    #filename list without extension but with directory
    filename_list_without_extension = []
    
    #filename list without extension and without directory name
    filename_list = []
    
    # split the extension from filename 
    for idx in range(0,len(filename_list_with_extension),1):
        if not filename_list_with_extension[idx].startswith('.'):
            filename_list_without_extension.append(path.splitext(image_dir+filename_list_with_extension[idx])[0])             
    
    #split the directory name
    for idx in range(0,len(filename_list_without_extension),1):
        filename = filename_list_without_extension[idx]
        filename_list.append(filename[filename.find(image_dir)+len(image_dir):])

    
    #Create nested list
    lower_case_split_images = [[] for i in range(len(filename_list))]
    pet_name = []
        
    #Retrieves filenames, transform them to lower case and split the filenames into words
    #and put them into a nested list (list of list)
    for idx in range(0,len(filename_list),1):        
        
        if not filename_list[idx].startswith("."):
            lower_case_split_images[idx] = filename_list[idx].lower().split('_')
    
   
    #Build the pet names
    for pet in range(0,len(lower_case_split_images),1):
        
        pet_name.append('')
        
        for word in range(0,len(lower_case_split_images[pet]),1):
            
            if lower_case_split_images[pet][word].isalpha():
                
                pet_name[pet] += lower_case_split_images[pet][word] + ' '
                       
    #Remove leading & trailing characters
    for word in range(0,len(pet_name),1):
            
            pet_name[word] = pet_name[word].strip()
    
    #Fill the dictionary     
    for idx in range(0,len(filename_list),1):
        if not filename_list[idx].startswith("."):
            results_dic[filename_list[idx]+ext] = [pet_name[idx]]
        
        elif filename_list[idx] in results_dic:
            print("** Warning: Key=", filename_list[idx], "already exists in results_dic with value =",                    results_dic[filename_list[idx]])
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    
    return results_dic
