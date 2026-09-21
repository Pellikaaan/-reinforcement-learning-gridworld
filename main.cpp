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

string ActionToString(ACTION action)
{
    switch(action)
    {
        case UP:
            return "UP";
        case DOWN:
            return "DOWN";
        case RIGHT:
            return "RIGHT";
        case LEFT:
            return "LEFT";
            break;
    }
}

void ValueIteration()
{
    ACTION actions [] = {UP,DOWN,LEFT,RIGHT};

    for (int i = 0; i < ROWS; ++i)
    {
        for (int j = 0; j < COLUMNS; ++j)
        {
            //TEST
            for (ACTION action : actions)
            {
                pair<int,int> nextState = makeMove(action, i, j);

                cout << nextState.first
                    << ","
                    << ActionToString(action)
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
