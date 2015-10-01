/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: DefaultConfig
	Model Element	: DefaultConfig
//!	Generated Date	: Thu, 1, Oct 2015  
	File Path	: DefaultComponent\DefaultConfig\MainDefaultComponent.cpp
*********************************************************************/

//## auto_generated
#include "MainDefaultComponent.h"
//## auto_generated
#include "Elevator.h"
//## auto_generated
#include "Floor.h"
//## auto_generated
#include "LevelButton.h"
//## auto_generated
#include "SystemController.h"
int main(int argc, char* argv[]) {
    int status = 0;
    if(OXF::initialize(argc, argv, 6423))
        {
            Elevator * p_Elevator;
            Floor * p_Floor;
            LevelButton * p_LevelButton;
            SystemController * p_SystemController;
            p_Elevator = new Elevator;
            p_Elevator->startBehavior();
            p_Floor = new Floor;
            p_Floor->startBehavior();
            p_LevelButton = new LevelButton;
            p_LevelButton->startBehavior();
            p_SystemController = new SystemController;
            p_SystemController->startBehavior();
            //#[ configuration DefaultComponent::DefaultConfig 
            //#]
            OXF::start();
            delete p_Elevator;
            delete p_Floor;
            delete p_LevelButton;
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
