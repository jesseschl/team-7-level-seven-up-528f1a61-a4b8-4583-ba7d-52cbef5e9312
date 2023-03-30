*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***         StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Valid Case North           4             5             1                     NORTH         4           4           2
Valid Case South           5             8             33                    SOUTH         5           9           34
Valid Case East            4             5             1                     EAST          5           5           2
Valid Case West            5             8             22                    WEST          4           8           23
Valid Edge Case North      9             9             1                     NORTH         9           8           2
Valid Edge Case South      0             0             33                    SOUTH         0           1           34
Valid Edge Case East       0             0             1                     EAST          1           0           2
Valid Edge Case West       9             9             22                    WEST          8           9           23
Invalid Edge Case North    0             0             5                     SOUTH         0           0           6
Invalid Edge Case South    9             9             11                    NORTH         9           9           12
Invalid Edge Case East     9             9             56                    EAST          9           9           57
Invalid Edge Case West     0             0             14                    WEST          0           0           15


*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}
