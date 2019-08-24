## PAGINATION HELPER
## PLEASE VISIT OUR WEB SITES (OUR PROBLEM-SOLVING PROGRAMMING, CODING, & DEVELOPMENT SERVICES ARE AVAILABLE FOR HIRE):
## www.JerusalemProgrammer.com
## www.JerusalemProgrammers.com
## www.JerusalemProgramming.com

# TODO: complete this class

## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

import math

## BEGIN DEFINE CLASS - PAGINATION HELPER
class PaginationHelper:

  ## BEGIN DEFINE FUNCTION  
  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      
      ## DECLARE VARIABLES
      self.collection = collection
      self.items_per_page = items_per_page
          
  ## BEGIN DEFINE FUNCTION     
  # returns the number of items within the entire collection
  def item_count(self):
      
      ## CALCULATE LENGTH OF COLLECTION
      item_count = len(self.collection)
    
      ## RETURN VARIABLES
      return(item_count)
  
  ## BEGIN DEFINE FUNCTION 
  # returns the number of pages
  def page_count(self):
      
      ## DECLARE VARIABLES
      item_count = self.item_count()
      items_per_page = self.items_per_page
      
      ## CALCULATE NUMBER OF PAGES
      page_count = math.ceil(item_count / items_per_page)
      
      ## RETURN VARIABLES
      return(page_count)
  
  ## BEGIN DEFINE FUNCTION 
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      
      ## DECLARE VARIABLES
      items_per_page = self.items_per_page
      item_count = self.item_count()
      
      ## IF PAGE INDEX + 1 MULTIPLIED BY ITEMS PER PAGE IS LESS THAN OR EQUAL TO ITEM COUNT
      if (page_index + 1) * items_per_page <= item_count:
					
          ## RETURN VARIABLES
          return(items_per_page)
          
      ## ELSE IF PAGE INDEX MULTIPLIED BY ITEMS PER PAGE IS LESS THAN ITEM COUNT AND
      ## PAGE INDEX + 1 MULTIPLIED BY ITEMS PER PAGE IS GREATER THAN ITEM COUNT
      elif ((page_index * items_per_page) < item_count) and ((page_index + 1) * items_per_page > item_count):
		  
          ## CALCULATE VARIABLES - PAGE ITEM COUNT EQUALS ITEM COUNT MODULO ITEMS PER PAGE
          page_item_count = item_count % items_per_page 
          
          ## RETURN VARIABLES
          return(page_item_count)
      
      ## OTHERWISE ELSE
      else:
          
          ## RETURN VARIABLES
          return(-1)
  
  ## BEGIN DEFINE FUNCTION  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      
      ## DECLARE VARIABLES
      item_count = self.item_count()
      items_per_page = self.items_per_page
      
      ## CALCULATE PAGE NUMBER
      page_index = math.floor(item_index/items_per_page)
      
      ## IF ITEM INDEX IS LESS THAN THE TOTAL ITEM COUNT IN COLLECTION
      ## AND ITEM INDEX IS LESS OR EQUAL TO 0....
      if (item_index < item_count) and (item_index >= 0):
          
          ## RETURN VARIABLES
          return(page_index)
          
      else:
          ## RETURN VARIABLES
          return(-1)
      
## END DEFINE CLASS - PAGINATION HELPER  
      
  
## DECLARE VARIABLES
      
#collection = ['a','b','c','d','e','f']
#items_per_page = 4
 
collection = range(1,25)
items_per_page = 10
     
helper = PaginationHelper(collection, items_per_page)
helper.page_count # should == 2
helper.item_count # should == 6
helper.page_item_count(0)  # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid

## WE HOPE YOU ENJOYED AND THAT THIS HELPS YOUR UNDERSTANDING OF USING PYTHON LANGUAGE TO SOLVE PROBLEMS WITH PROGRAMMING
## PLEASE COME BACK AGAIN SOON
## PLEASE VISIT OUR WEB SITES (OUR PROBLEM-SOLVING PROGRAMMING, CODING, & DEVELOPMENT SERVICES ARE AVAILABLE FOR HIRE):
## www.JerusalemProgrammer.com
## www.JerusalemProgrammers.com
## www.JerusalemProgramming.com
