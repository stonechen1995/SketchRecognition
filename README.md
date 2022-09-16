# SketchRocognition HW1
To install all dependencies required, run command 
    pip install -r requirements.txt

## part1.py 
The purpose of part1.py is to generate 13 rubine features from provided datasets in folder data/. 

To run the script, run command 
    python part1.py

The program traverses all dataset provided. It, at the beginning, preprocess dataset by removing rows that have repeated values that are the same as the ones right above.

Next, it calculates the all 13 rubine features. Once getting all 13 features of a dataset, these 13 features will be appended to a dataframe, which stores  13 rubine features of all datasets. This dataframe will then be turned into a csv file.

## part2.py

The Purpose of part2.py is to resample the given datasets and generate new datasets with only 64 points each. 

To run the script, run command 
    python part2.py

The program traverses all dataset provided. It, at the beginning, preprocess dataset by removing rows that have repeated values that are the same as the ones right above.

Next, it calculates rubine feature 8 for each given dataset, which is the total length of a stroke. 

The function resample() does the main job to resample data. The base knowledge applied here is from the link: https://math.stackexchange.com/a/1918779.

By iterating points and using the linear interpolation to find the proper spacing, we are able to find the location where each point of 64 should be interpolated. if length of (unit spacing * No. point) from point 0  is between some points, then a sampled point can be interpolated between these two points. Otherwise, index to next point on original stroke and repeat the first step.