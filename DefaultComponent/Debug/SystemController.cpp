/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: Debug
	Model Element	: SystemController
//!	Generated Date	: Tue, 29, Sep 2015  
	File Path	: DefaultComponent\Debug\SystemController.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX
//#]

//## auto_generated
#include "SystemController.h"
//## auto_generated
#include <iostream>
//#[ ignore
#define Default_SystemController_notifyState_SERIALIZE \
    aomsmethod->addAttribute("direction", x2String(direction));\
    aomsmethod->addAttribute("level", x2String(level));
#define Default_SystemController_SystemController_SERIALIZE OM_NO_OP

#define Default_SystemController_handleDownRequests_SERIALIZE aomsmethod->addAttribute("level", x2String(level));

#define Default_SystemController_handleUpRequests_SERIALIZE aomsmethod->addAttribute("level", x2String(level));
//#]

//## package Default

//## class SystemController

using namespace std;

SystemController::SystemController(IOxfActive* theActiveContext) {
    NOTIFY_REACTIVE_CONSTRUCTOR(SystemController, SystemController(), 0, Default_SystemController_SystemController_SERIALIZE);
    setActiveContext(theActiveContext, false);
    {
        for (int i = 0; i < 2; i++) 
            {
                itsElevator[i].setShouldDelete(false);
            }
        
        {
            for (int i = 0; i < 5; i++) 
                {
                    itsFloor[i].setShouldDelete(false);
                }
            
        }
    }
    initRelations();
    //#[ operation SystemController()
    for (int i = 0; i < 5; i++)
    	itsFloor[i].setLevel(i);
    //#]
}

SystemController::~SystemController() {
    NOTIFY_DESTRUCTOR(~SystemController, true);
}

void SystemController::handleDownRequests(int level) {
    NOTIFY_OPERATION(handleDownRequests, handleDownRequests(int), 1, Default_SystemController_handleDownRequests_SERIALIZE);
    //#[ operation handleDownRequests(int)
    int distance[2];
    
    if (itsElevator[0].getMode() != 3 && itsElevator[1].getMode() != 3) {
    	for (int i = 0; i < 2; i++)	{
    		if (itsElevator[i].getDirection() == 1)
    			distance[i] = 8 - level - (itsElevator[i].getCurrentLevel()-1);
    		else if (itsElevator[i].getDirection() == 2) {
    			distance[i] = (itsElevator[i].getCurrentLevel()-1) - level;
    			if (distance[i] < 0)
    				distance[i] += 8;
    		}
    		else {
    			distance[i] = (itsElevator[i].getCurrentLevel()-1) - level;
    			if (distance[i] < 0)
    				distance[i] = -distance[i];
    		}
    	}
    
    	if (distance[0] <= distance[1])
    		itsElevator[0].setDownRequests(level, 1);
    	else
    		itsElevator[1].setDownRequests(level, 1);
    }
    else if (itsElevator[0].getMode() != 3 && itsElevator[1].getMode() == 3) {
    	itsElevator[0].setDownRequests(level, 1);
    }
    else if (itsElevator[0].getMode() == 3 && itsElevator[1].getMode() != 3) {
    	itsElevator[1].setDownRequests(level, 1);
    }
    //#]
}

void SystemController::handleUpRequests(int level) {
    NOTIFY_OPERATION(handleUpRequests, handleUpRequests(int), 1, Default_SystemController_handleUpRequests_SERIALIZE);
    //#[ operation handleUpRequests(int)
    int distance[2];
    
    if (itsElevator[0].getMode() != 3 && itsElevator[1].getMode() != 3) {
    	for (int i = 0; i < 2; i++)	{
    		if (itsElevator[i].getDirection() == 2)
    			distance[i] = level + (itsElevator[i].getCurrentLevel()-1);
    		else if (itsElevator[i].getDirection() == 1) {
    			distance[i] = level - (itsElevator[i].getCurrentLevel()-1);
    			if (distance[i] < 0)
    				distance[i] += 8;
    		}
    		else {
    			distance[i] = level - (itsElevator[i].getCurrentLevel()-1);
    			if (distance[i] < 0)
    				distance[i] = -distance[i];
    		}
    	}
    
    	if (distance[0] <= distance[1])
    		itsElevator[0].setUpRequests(level, 1);
    	else
    		itsElevator[1].setUpRequests(level, 1);
    }
    else if (itsElevator[0].getMode() != 3 && itsElevator[1].getMode() == 3) {
    	itsElevator[0].setUpRequests(level, 1);
    }
    else if (itsElevator[0].getMode() == 3 && itsElevator[1].getMode() != 3) {
    	itsElevator[1].setUpRequests(level, 1);
    }
    //#]
}

void SystemController::notifyState(int direction, int level) {
    NOTIFY_OPERATION(notifyState, notifyState(int,int), 2, Default_SystemController_notifyState_SERIALIZE);
    //#[ operation notifyState(int,int)
    if (direction == 1) {
    	itsFloor[level].setUp(0);
    	itsElevator[0].setUpRequests(level, 0); 
    	itsElevator[1].setUpRequests(level, 0); 
    }
    else if (direction == 2) {
    	itsFloor[level].setDown(0);
    	itsElevator[0].setDownRequests(level, 0); 
    	itsElevator[1].setDownRequests(level, 0); 
    }
    //#]
}

int SystemController::getItsElevator() const {
    int iter = 0;
    return iter;
}

int SystemController::getItsFloor() const {
    int iter = 0;
    return iter;
}

bool SystemController::startBehavior() {
    bool done = true;
    {
        int iter = 0;
        while (iter < 2){
            done &= (((Elevator*)&itsElevator[iter]))->startBehavior();
            iter++;
        }
    }
    {
        int iter = 0;
        while (iter < 5){
            done &= (((Floor*)&itsFloor[iter]))->startBehavior();
            iter++;
        }
    }
    done &= OMReactive::startBehavior();
    return done;
}

void SystemController::initRelations() {
    {
        int iter = 0;
        while (iter < 2){
            ((Elevator*)&itsElevator[iter])->_setSystem(this);
            iter++;
        }
    }
    {
        int iter = 0;
        while (iter < 5){
            ((Floor*)&itsFloor[iter])->_setSystem(this);
            iter++;
        }
    }
}

void SystemController::setActiveContext(IOxfActive* theActiveContext, bool activeInstance) {
    OMReactive::setActiveContext(theActiveContext, activeInstance);
    {
        for (int i = 0; i < 2; i++) 
            {
                itsElevator[i].setActiveContext(theActiveContext, false);
            }
        
        {
            for (int i = 0; i < 5; i++) 
                {
                    itsFloor[i].setActiveContext(theActiveContext, false);
                }
            
        }
    }
}

void SystemController::destroy() {
    {
        int iter = 0;
        while (iter < 2){
            (((Elevator*)&itsElevator[iter]))->destroy();
            iter++;
        }
    }
    {
        int iter = 0;
        while (iter < 5){
            (((Floor*)&itsFloor[iter]))->destroy();
            iter++;
        }
    }
    OMReactive::destroy();
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedSystemController::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsElevator", true, false);
    {
        int iter = 0;
        while (iter < 2){
            aomsRelations->ADD_ITEM(((Elevator*)&myReal->itsElevator[iter]));
            iter++;
        }
    }
    aomsRelations->addRelation("itsFloor", true, false);
    {
        int iter = 0;
        while (iter < 5){
            aomsRelations->ADD_ITEM(((Floor*)&myReal->itsFloor[iter]));
            iter++;
        }
    }
}
//#]

IMPLEMENT_REACTIVE_META_SIMPLE_P(SystemController, Default, Default, false, OMAnimatedSystemController)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: DefaultComponent\Debug\SystemController.cpp
*********************************************************************/
