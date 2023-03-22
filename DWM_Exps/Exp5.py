"""
Experiment No :5
Decision Tree Algorithm

Name: Khan Arshad Abdulla
Roll No: 20CO24

"""
import pandas as pd
import math
import numpy as np

dataset = pd.read_csv("C:/Users/arshad/OneDrive/Desktop/DWM_Exps/dataset_computers.csv")
features = [feat for feat in dataset]
features.remove("Buys_Computer")


class Node:
    def __init__(self):
        self.children = []
        self.value = ""
        self.isLeaf = False
        self.pred = ""


def entropy(examples):
    pos = 0.0
    neg = 0.0
    for _, row in examples.iterrows():
        if row["Buys_Computer"] == "Yes":
            pos += 1
        else:
            neg += 1
    if pos == 0.0 or neg == 0.0:
        return 0.0
    else:
        p = pos / (pos + neg)
        n = neg / (pos + neg)
        return -(p * math.log(p, 2) + n * math.log(n, 2))


def info_gain(examples, attr):
    uniq = np.unique(examples[attr])
    #print ("\n",uniq)
    gain = entropy(examples)
    #print ("\n",gain)
    for u in uniq:
        subdata = examples[examples[attr] == u]
        #print ("\n",subdata)
        sub_e = entropy(subdata)
        gain -= (float(len(subdata)) / float(len(examples))) * sub_e
        #print ("\n",gain)
    return gain


def ID3(examples, attrs):
    root = Node()

    max_gain = 0
    max_feat = ""
    for feature in attrs:
        #print ("\n",examples)
        gain = info_gain(examples, feature)
        if gain > max_gain:
            max_gain = gain
            max_feat = feature
    root.value = max_feat
    #print ("\nMax feature attr",max_feat)
    uniq = np.unique(examples[max_feat])
    #print ("\n",uniq)
    for u in uniq:
        #print ("\n",u)
        subdata = examples[examples[max_feat] == u]
        #print ("\n",subdata)
        if entropy(subdata) == 0.0:
            newNode = Node()
            newNode.isLeaf = True
            newNode.value = u
            newNode.pred = np.unique(subdata["Buys_Computer"])
            root.children.append(newNode)
        else:
            dummyNode = Node()
            dummyNode.value = u
            new_attrs = attrs.copy()
            new_attrs.remove(max_feat)
            child = ID3(subdata, new_attrs)
            dummyNode.children.append(child)
            root.children.append(dummyNode)
    return root


def printTree(root: Node, depth=0):
    for i in range(depth):
        print("\t", end="")
    print(root.value, end="")
    if root.isLeaf:
        print(" -> ", root.pred)
    print()
    for child in root.children:
        printTree(child, depth + 1)


root = ID3(dataset, features)
printTree(root)

"""
dataset_computers.csv:

            Age,Income,Student,Credit_rating,Buys_Computer
            <=30,High,No,Fair,No
            <=30,High,No,Excellent,No
            31..40,High,No,Fair,Yes
            >40,Medium,No,Fair,Yes
            >40,Low,Yes,Fair,Yes
            >40,Low,Yes,Excellent,No
            31..40,Low,Yes,Excellent,Yes
            <=30,Medium,No,Fair,No
            <=30,Low,Yes,Fair,Yes
            >40,Medium,Yes,Fair,Yes
            <=30,Medium,Yes,Excellent,Yes
            31..40,Medium,No,Excellent,Yes
            31..40,High,Yes,Fair,Yes
            >40,Medium,No,Excellent,No

Output:

Age
        31..40 ->  ['Yes']

        <=30
                Student
                        No ->  ['No']       

                        Yes ->  ['Yes']     

        >40
                Credit_rating
                        Excellent ->  ['No']

                        Fair ->  ['Yes']    


"""
