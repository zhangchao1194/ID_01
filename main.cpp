/**************************************************************************/
 /**
* @brief main function
* @details this is where main function in
* @addtogroup example
* @author Chao Zhang
* @version 0.01
* @date 2014/07/27
******************************************************************************
* Copyright (c), 2014, SCV Lab, Iwate University.
******************************************************************************
* Edit History \n
* -------------------------------------------------------------------------\n
* DATE NAME DESCRIPTION \n
* 2014/07/27 Chao Zhang Create.\n
******************************************************************************
* @{
*****************************************************************************/
#include <iostream>

/**
  @brief this is the function to add two numbers
  */
int add (int a, int b)
{
    return a + b;
}

using namespace std;

int main()
{
    cout << "Hello World!" << add(1, 2) << endl;
    return 0;
}

 /** @}***********************************************************/
