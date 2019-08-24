## CSS / HTML SELECTOR SPECIFICITY
## PLEASE VISIT OUR WEB SITES (OUR PROBLEM-SOLVING PROGRAMMING, CODING, & DEVELOPMENT SERVICES ARE AVAILABLE FOR HIRE):
## www.JerusalemProgrammer.com
## www.JerusalemProgrammers.com
## www.JerusalemProgramming.com

## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

import re

## BEGIN DEFINE FUNCTIONS
## BEGIN DEFINE FUNCTIONS
## BEGIN DEFINE FUNCTIONS

## BEGIN DEFINE FUNCTION - REMOVE WHITE SPACE
def fn_RemoveWhiteSpace(AorB):

    ## DECLARE VARIABLES
    ListX = []
    
    ## IF SELECTOR A OR B INCLUDES WHITE SPACE
    if (' ' in AorB) == True:
        ListX = AorB.split()
        
    ## ELIF SELECTOR A OR B DOES NOT INCLUDE WHITE SPACE    
    elif (' ' in AorB) == False:
        ListX.append(AorB)
                
    ## RETURN VARIABLES
    return(ListX)
    
## END DEFINE FUNCTION - REMOVE WHITE SPACE
    
    
## BEGIN DEFINE FUNCTION - SPLIT AND SORT WITH REGULAR EXPRESSIONS
def fn_SplitAndSortRE(ListX):
    
    ## DECLARE VARIABLES
    ListMasterX = []
        
    ## BEGIN FOR LOOP SELECTOR A OR SELCTOR B - SPLIT AND SORT WITH REGULAR EXPRESSIONS
    for each in ListX:
        
        ListTempX = re.findall('^\w+|[#]+[a-zA-Z0-9]*|[.]+[a-zA-Z0-9]*', each)
        
        ListMasterX.extend(ListTempX)
    
    ## END FOR LOOP SELECTOR A OR SELECTOR B - SPLIT AND SORT WITH REGULAR EXPRESSIONS
    
    ## RETURN VARIABLES
    return(ListMasterX)
    
## END DEFINE FUNCTION - SPLIT AND SORT WITH REGULAR EXPRESSIONS 
    
    
## BEGIN DEFINE FUNCTION - COUNT SELECTORS 
def fn_CountSelectors(ListMasterX):

    ## DECLARE VARIABLES
    CountIDsX = 0
    CountClassesX = 0
    CountElementsX = 0
    
    ## BEGIN FOR LOOP SELECTOR ListMasterA OR ListMasterB - COUNT SELECTORS    
    for each in ListMasterX:
        
        if each[0] == '#':
            CountIDsX += 1
        
        elif each[0] == '.':
            CountClassesX += 1
            
        else:
            CountElementsX += 1
            
    ## END FOR LOOP SELECTOR ListMasterA OR ListMasterB - COUNT SELECTORS
    
    ## RETURN VARIABLES
    return(CountIDsX, CountClassesX, CountElementsX)
    
## END DEFINE FUNCTION - COUNT SELECTORS 
    
    
## BEGIN DEFINE FUNCTION - COMPARE
def compare(a, b):
    
    ## CALL FUNCTION - REMOVE WHITE SPACE FOR A
    ListA = fn_RemoveWhiteSpace(a)
    
    ## CALL FUNCTION - REMOVE WHITE SPACE FOR B
    ListB = fn_RemoveWhiteSpace(b)
        
    ## CALL FUNCTION - SPLIT AND SORT WITH REGULAR EXPRESSIONS FOR A
    ListMasterA = fn_SplitAndSortRE(ListA)
    
    ## CALL FUNCTION - SPLIT AND SORT WITH REGULAR EXPRESSIONS FOR B
    ListMasterB = fn_SplitAndSortRE(ListB)
              
    ## CALL FUNCTION - COUNT SELECTORS FOR A
    SpecificityA = fn_CountSelectors(ListMasterA)
    
    ## CALL FUNCTION - COUNT SELECTORS FOR B
    SpecificityB = fn_CountSelectors(ListMasterB)
    
    ## IF SPECIFICITY OF A IS GREATER THAN SPECIFICITY OF B
    if SpecificityA > SpecificityB:
        return(a)
        
    ## ELSE IF SPECIFICITY OF A IS LESS THAN SPECIFICITY OF B
    elif SpecificityA < SpecificityB:
        return(b)
        
    ## ELSE IF SPECIFICITY OF A EQUALS THE SPECIFICITY OF B    
    elif SpecificityA == SpecificityB:
        return(b)
        
# END DEFINE FUNCTION - COMPARE

## END DEFINE FUNCTIONS   
## END DEFINE FUNCTIONS
## END DEFINE FUNCTIONS


## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
            
## CALL FUNCTION
Selector1 = compare("body p", "div") # returns "body p"
Selector2 = compare(".class", "#id") # returns "#id"
Selector3 = compare("div.big", ".small") # returns "div.big"
Selector4 = compare(".big", ".small") # returns ".small" (because it appears later)


## END MAIN PROGRAM
## END MAIN PROGRAM
## END MAIN PROGRAM

## GAME OVER
## GAME OVER
## GAME OVER

## WE HOPE YOU ENJOYED AND THAT THIS HELPS YOUR UNDERSTANDING OF USING PYTHON LANGUAGE TO SOLVE PROBLEMS WITH PROGRAMMING
## PLEASE COME BACK AGAIN SOON
## PLEASE VISIT OUR WEB SITES (OUR PROBLEM-SOLVING PROGRAMMING, CODING, & DEVELOPMENT SERVICES ARE AVAILABLE FOR HIRE):
## www.JerusalemProgrammer.com
## www.JerusalemProgrammers.com
## www.JerusalemProgramming.com
