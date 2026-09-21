#include <iostream>
#include <vector>

using namespace std;

const int ROWS = 4;
const int COLUMNS = 4; //4x4 grid

enum CELL {
    EMPTY,
    START,
    GOAL,
    BLOCKADE
};

enum ACTION{
    UP,
    DOWN,
    LEFT,
    RIGHT
};

pair<int,int> makeMove(ACTION action, int row, int col)
{
    int newRow = row;
    int newCol = col;

    switch(action)
    {
        case UP:
            newRow -= 1;

        case DOWN:
            newRow += 1;

        case LEFT:
            newCol -= 1;

        case RIGHT:
            newCol += 1;
        break;
    }
    return {newRow,newCol};
}

void ValueIteration()
{
    for(int i = 0; i < ROWS; ++i)
    {
        for(int j = 0; j < COLUMNS; ++j)
        {
            //TEST
            for(int AllActions=0; AllActions < 4; AllActions++)
            {
                ACTION actions = static_cast<ACTION>(AllActions);
                pair<int,int> nextState = makeMove(actions, i, j);

                cout << nextState.first
                    << "," 
                    << nextState.second
                    << endl;
            }
        }
    }
};

int main()
{
    ValueIteration();   
}
