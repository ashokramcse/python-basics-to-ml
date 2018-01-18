# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 01:54:23 2018

"""
# Importing ABC Module will make help us with Abstract class implementation.
from abc import ABC, abstractmethod

# W cannot able to create instance for ImageTask
class ImageTask(ABC):
    
    @abstractmethod
    def create_image(self):
        pass
    
class ImageSubTask(ImageTask):
    def create_image(self):
        return "Image Ready"
    
subtask = ImageSubTask()
print (subtask.create_image())