/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: Debug
	Model Element	: Debug
//!	Generated Date	: Mon, 28, Sep 2015  
	File Path	: DefaultComponent\Debug\MainDefaultComponent.cpp
*********************************************************************/

//## auto_generated
#include "MainDefaultComponent.h"
//## auto_generated
#include "SystemController.h"
int main(int argc, char* argv[]) {
    int status = 0;
    if(OXF::initialize(argc, argv, 6423))
        {
            SystemController * p_SystemController;
            p_SystemController = new SystemController;
            p_SystemController->startBehavior();
            //#[ configuration DefaultComponent::Debug 
            //#]
            OXF::start();
            delete p_SystemController;
            status = 0;
        }
    else
        {
            status = 1;
        }
    return status;
}

/*********************************************************************
	File Path	: DefaultComponent\Debug\MainDefaultComponent.cpp
*********************************************************************/
