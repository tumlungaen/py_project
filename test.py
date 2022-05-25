from sklearn import tree
features = [ [120, 5], [110, 5], [180, 12], [163, 18], [159, 13], [113, 52] ]
labels = [ "ECO Car", "Normal Car", "BUS", "VAN", "Sport Car", "" ]
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit( features, labels )

print( classifier.predict( [ [150, 12] ] ) )