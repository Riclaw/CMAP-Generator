# NLP-Project

The main notebook is the main_notebook.ipynb file, which contains the model for map generation. The main notebook calls the classifier.ipynb and graph.py files, and generates the maps on the evaluation set. 

The classifier.ipynb regards the training of the classifier for relation selection, while the graph.py file contains the class for the visualization of the concept map, which creates nodes and edges starting from the resulting data frame of the most important propositions. 

The files resolve_coreferences.ipynb and extract_rel.ipynb, respectively, manage the use of NeuralCoref to solve coreferences on the entire paragraph and the extraction of relations using the OpenIE Stanford tool. A guide to set up OpenIE is also provided. The handmade_maps.ipynb notebook is used to visualize human-created maps, and the baseline_test.ipynb notebook is used to generate the baseline concept maps. 

The evaluation.ipynb regards the model evaluation method implemented at the end of the project, the 2 dataframes used in the code are also provided.  
