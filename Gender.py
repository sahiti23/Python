from sklearn import tree

# decision tree
# [height, weight, strength_scale]

x =   [[160, 45,3], [181,70, 7], [190,78,9], [192,45,2],[130,40,1]]
y = ['female','male','male','male','female']

classifier = tree.DecisionTreeClassifier()

classifier = classifier.fit(x,y)

prediction = classifier.predict([[190,100,10]])

print(prediction)

tree.plot_tree(classifier.fit(x,y))