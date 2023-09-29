## Algorithms i tried 

- Return the first Legal Move
    - Always ends in a Silly threeFold repitition / draw
    ![Alt text](/images/i1.png)

- Check if there is a checkmate or Return random Legal Move
    ![Alt text](/images/i2.png)




## Todo 

- Check the Most valuable Capture out of all the Captures & Return that move 
- Evaluate Position based on the Pieces Present


## Algorithms according to function Name:

    - Whole point is to calculate how bad is the oppenents position
    - Calculating position:
        - can be found in: evaluate.py-->calculatePosition(board:chess.Board,color:bool)
        - First i set the value for each piece in the Board
        - if: color==>True-->white,false-->black
        - Algorithm:
            -it just iterates through all the 64 sqaures 
            -if it is a black piece then it adds to a score varibale
            -int the end it returns score
