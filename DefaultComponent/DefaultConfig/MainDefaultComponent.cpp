/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: DefaultConfig
	Model Element	: DefaultConfig
//!	Generated Date	: Tue, 6, Oct 2015  
	File Path	: DefaultComponent\DefaultConfig\MainDefaultComponent.cpp
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
            //#[ configuration DefaultComponent::DefaultConfig 
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
	File Path	: DefaultComponent\DefaultConfig\MainDefaultComponent.cpp
*********************************************************************/
