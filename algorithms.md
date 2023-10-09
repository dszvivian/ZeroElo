## Algorithms i tried 

- Return the first Legal Move
    - Always ends in a Silly threeFold repitition / draw
    ![Alt text](/images/i1.png)

- Check if there is a checkmate or Return random Legal Move
    ![Alt text](/images/i2.png)

- Check if there is checkmate,Look for the Best Capture if exists or Return Random Move
    - Observations: Less stalemates,more pieces on the board,Quick Games on Average
    ![Alt text](/images/i3.png)



## Todo 

- Try Different Learning Algorithms
    - minimax search
    - alpha-beta pruning
    - ordered search 

# Algorithms :



## Evaluation Function

### BoardEvaluation
> Checks all the square   
> if there is a piece   
>   it calcualtes it's value   
>   value = value_of_piece + value_of_piece_at_that_Square(ie:using mapping)  
> then it sums the value of all the pieces   
> if it is Black turn then it Returns -total else +total  


### move_value
> if move leads to promotion --> then it return +inf or -inf   
> else  
> calculates value  
> value = value_at_to_sqare +  value_at_from_square  
> if there exists a capture    
> total = capture_value + value   
>if B => -total else +total  



