import splitfolders
input_folder = "RGB ArSL dataset"
output_folder = "Dataset"
splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(0.9, 0.1))