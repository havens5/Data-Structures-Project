# Trees

* [Introduction – What is a Tree?](#introduction)
    * Structure
* [When to use a Tree?](#when-to-use-a-tree)
* [Elements of Linked Lists](#elements-of-trees)
    * Recursion
    * Binary Search Tree
    * Balanced Binary Search Tree
    * Inserting to a Binary Search Tree
    * Navigating a Binary Search Tree 
* [Performance](#performance)
* [Example](#example)
* [Problem to Solve](#problem-to-solve)

## Introduction
Trees are very similar to linked list. The reason being that they both have nodes that are connected by pointers. The difference is that trees can connect to many different nodes. There are a few different trees but essentially they build upon one another. 

![Tree Build](treebuild.jpg)

To start off lets in talking about a 

## When to use a Tree?
Some reasons that you might want to use a tree is when you need to store information into a hiarchy of data. for example the file system that you have in your computer. That file system of yours is basically your own personalized tree to keep all of your files as you see fit.
## Elements of Trees

### Recursion
In order to fully understand trees we need to talk about recursion. Recursion is where a functions calls itself. For example:

```python
 def ice_cream():
     print("You scream, I scream, We all scream for Ice cream!!")
     ice_cream() # this will call the same function 
```

Now with recursion there are rules that need to be followed so we dont have a infinate loop of a function calling itself. These two rules are:
1. **Base case** - this is the case in which we will stop the recursion calling
1. Making it **closer to the base case** with each recursion call.

Now lets use the same example as before with these rules

```python
def ice_cream(numFlavors):
    if numFlavors <= 0:  # Base case
        return 
    else:
        print("You scream, I scream, We all scream for Ice cream!!")
        ice_cream(numFlavors - 1) # getting closer to the base case 
```

### Binary Search Tree

### Balanced Binary Search Tree

### Inserting to a Binary Search Tree

### Navigating a Binary Search Tree


## Performance

## Example

```python

```

## Problem to Solve


## Resourses

CSE 212 Readings

[Applications of tree data structure](https://www.geeksforgeeks.org/applications-of-tree-data-structure/)


-------
[Overview](../README.md) | [Previous Lesson ](../3-LinkedList/LinkedList.md)