# Stack

* [Introduction - What is a Stack?](#introduction)
    * Ice Cream cone Example
    * Flow of data
* [When to use a stack?](#when-to-use-a-stack)
    * Front
    * Back 
* [Elements of stacks](#elements-of-a-stack)
    * Push 
    * Pop
    * Size
    * Empty
* [Performance](#preformance) 
* [Example](#example)
* [Try it out!](#try-it-out)

## Introduction
Now as we look at this image what comes to mind? You may be thinking "Wow someone loves ice cream" or maybe "Lactose nightmare!" but for the sake of this lesson lets think of how the ice cream is **stacked** 

![Ice cream Stack](ice-cream-example.jpg)

When you create an ice cream tower like this, it all starts at the bottom and you work your way up. Stacks work in a similar manner. It works in the manner of **Fisrt** in **Last** out. 

## When to use a Stack
Stacks are really good at tracking history of where you have been. As items are placed on the stack, with first in last out in essesnce we can see that we work from the top of the ice cream tower to the ice cream cone. So you will be able to see all the different flavors that you stacked on top one another.

![Ice cream push/pop](ice-cream-stack.jpg)

## Elements of a Stack

|Operation   |Description                                            |Python Code                   |Preformance|
|------------|-------------------------------------------------------|------------------------------|-----------|
|push("item")|Adds a "item" to the back of the stack                 |icecream.append(flavor)       |O(1)       |
|pop()       |Removes and returns the item from the back of the stack|nextFlavor = icecream.pop()   |O(1)       |
|size()      |Return the size of the stack                           |numFlavors = length(icecream) |O(1)       |
|empty()     |Returns true if the length of the stack is empty       |if len(icecream) == 0         |O(1)       | 

## Preformance

As we can see the preformance for all the operations of a stack including adding or removing to a dynamic array, returning the size and checking the size are all the preformance of O(1). The reason that this is the case is because stacks always opperate on the back of the dynamic array.  

## Example 

This example shows you how to take a string and reverse it with a stack.

```python
#string options - Live on time, emit no evil

def main(string):

    #create a empty stack
    letterStack = []

    #take each letter of the string and add it to the stack
    for letter in string:
        push(letterStack, letter)
    
    #create a new string to add letters to
    reversed = ""

    #take each letter off the stack until it is empty and add each letter to the new string
    while len(stack) > 0:
        reversed = letterStack.pop()

    #return the finished new string
    return reversed

#print the new string
print(reversed)

```

## Try it out!

Print out the sentence from a stack (not in reverse) in order one line at a time

[Solution](stacks.py)

## Resourses
ice cream image - https://www.shape.com/healthy-eating/diet-tips/healthy-ice-cream-guide-which-variety-best


[Overview](../README.md) | [Next Lesson](../3-LinkedList/LinkedList.md)