/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: Debug
	Model Element	: Elevator
//!	Generated Date	: Tue, 29, Sep 2015  
	File Path	: DefaultComponent\Debug\Elevator.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "Elevator.h"
//## link system
#include "SystemController.h"
//## auto_generated
#include <iostream>
//#[ ignore
#define Default_Elevator_setDownRequests_SERIALIZE \
    aomsmethod->addAttribute("level", x2String(level));\
    aomsmethod->addAttribute("i", x2String(i));
#define Default_Elevator_setUpRequests_SERIALIZE \
    aomsmethod->addAttribute("level", x2String(level));\
    aomsmethod->addAttribute("i", x2String(i));
#define Default_Elevator_Elevator_SERIALIZE OM_NO_OP

#define Default_Elevator_getCurrentLevel_SERIALIZE OM_NO_OP

#define Default_Elevator_getDirection_SERIALIZE OM_NO_OP

#define Default_Elevator_getDownRequests_SERIALIZE aomsmethod->addAttribute("level", x2String(level));

#define Default_Elevator_getMode_SERIALIZE OM_NO_OP

#define Default_Elevator_getUpRequests_SERIALIZE aomsmethod->addAttribute("level", x2String(level));

#define Default_Elevator_haveDownRequests_SERIALIZE OM_NO_OP

#define Default_Elevator_haveRequests_SERIALIZE OM_NO_OP

#define Default_Elevator_haveUpRequests_SERIALIZE OM_NO_OP

#define Default_Elevator_load_SERIALIZE OM_NO_OP

#define Default_Elevator_move_SERIALIZE OM_NO_OP

#define Default_Elevator_needStop_SERIALIZE OM_NO_OP

#define Default_Elevator_unLoad_SERIALIZE OM_NO_OP
//#]

//## package Default

//## class Elevator

using namespace std;

Elevator::Elevator(IOxfActive* theActiveContext) : currLoad(0), currentLevel(1), direction(0), doorOpen(0), mode(1), overLoaded(0), stop(0) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Elevator, Elevator(), 0, Default_Elevator_Elevator_SERIALIZE);
    setActiveContext(theActiveContext, false);
    {
        for (int i = 0; i < 5; i++) 
            {
                itsLevel[i].setShouldDelete(false);
            }
        
    }
    system = NULL;
    initStatechart();
    //#[ operation Elevator()
    currentLevel = 1;
    currLoad=0;
    doorOpen=0; 
    for (int i = 0; i < 5; i++) {
    	upRequests[i] = 0;
    	downRequests[i] = 0;
    }
    if (mode==1){
    	MAX_LOAD=8;
    }else if (mode==2){
    	MAX_LOAD=800;
    }
    //#]
}

Elevator::~Elevator() {
    NOTIFY_DESTRUCTOR(~Elevator, true);
    cleanUpRelations();
    cancelTimeouts();
}

int Elevator::getCurrentLevel() {
    NOTIFY_OPERATION(getCurrentLevel, getCurrentLevel(), 0, Default_Elevator_getCurrentLevel_SERIALIZE);
    //#[ operation getCurrentLevel()
    return currentLevel;
    //#]
}

int Elevator::getDirection() {
    NOTIFY_OPERATION(getDirection, getDirection(), 0, Default_Elevator_getDirection_SERIALIZE);
    //#[ operation getDirection()
    return direction;
    //#]
}

int Elevator::getDownRequests(int level) {
    NOTIFY_OPERATION(getDownRequests, getDownRequests(int), 1, Default_Elevator_getDownRequests_SERIALIZE);
    //#[ operation getDownRequests(int)
    return downRequests[level];
    //#]
}

int Elevator::getMode() {
    NOTIFY_OPERATION(getMode, getMode(), 0, Default_Elevator_getMode_SERIALIZE);
    //#[ operation getMode()
    return mode;
    //#]
}

int Elevator::getUpRequests(int level) {
    NOTIFY_OPERATION(getUpRequests, getUpRequests(int), 1, Default_Elevator_getUpRequests_SERIALIZE);
    //#[ operation getUpRequests(int)
    return upRequests[level];
    //#]
}

bool Elevator::haveDownRequests() {
    NOTIFY_OPERATION(haveDownRequests, haveDownRequests(), 0, Default_Elevator_haveDownRequests_SERIALIZE);
    //#[ operation haveDownRequests()
    for (int i = currentLevel; i > 0; i--) {
    	if (itsLevel[i-1].isOn() || downRequests[i-1] == 1) {  
    		return true;  
    	} 
    }
    return false;
    //#]
}

bool Elevator::haveRequests() {
    NOTIFY_OPERATION(haveRequests, haveRequests(), 0, Default_Elevator_haveRequests_SERIALIZE);
    //#[ operation haveRequests()
    if (direction == 1) {
    	for (int i = currentLevel; i <= 5; i++) {
    		if (itsLevel[i-1].isOn() || upRequests[i-1] == 1 || downRequests[i-1] == 1) {
    			return true;  
    		}
    	} 
    	for (int i = currentLevel; i > 0; i--) {
    		if (itsLevel[i-1].isOn() || downRequests[i-1] == 1 || upRequests[i-1] == 1) {  
    			direction = 2;
    			return true;  
    		} 
    	}
    }
    else if (direction == 2) {
    	for (int i = currentLevel; i > 0; i--) {
    		if (itsLevel[i-1].isOn() || downRequests[i-1] == 1 || upRequests[i-1] == 1) {  
    			return true;  
    		} 
    	}
    	for (int i = currentLevel; i <= 5; i++) {
    		if (itsLevel[i-1].isOn() || upRequests[i-1] == 1 || downRequests[i-1] == 1) {
    			direction = 1;
    			return true;  
    		}
    	} 
    }
    else {
    	for (int i = currentLevel; i <= 5; i++) {
    		if (itsLevel[i-1].isOn() || upRequests[i-1] == 1 || downRequests[i-1] == 1) {
    			direction = 1;
    			return true;  
    		}
    	}
    	for (int i = currentLevel; i > 0; i--) {
    		if (itsLevel[i-1].isOn() || downRequests[i-1] == 1 || upRequests[i-1] == 1) {  
    			direction = 2;
    			return true;  
    		} 
    	}
    }
    return false;
    //#]
}

bool Elevator::haveUpRequests() {
    NOTIFY_OPERATION(haveUpRequests, haveUpRequests(), 0, Default_Elevator_haveUpRequests_SERIALIZE);
    //#[ operation haveUpRequests()
    for (int i = currentLevel; i <= 5; i++) {
    	if (itsLevel[i-1].isOn() || upRequests[i-1] == 1) {
    		return true;  
    	}
    } 
    return false;
    //#]
}

void Elevator::load() {
    NOTIFY_OPERATION(load, load(), 0, Default_Elevator_load_SERIALIZE);
    //#[ operation load()
    if (mode==1){
    	currLoad++;
    }else if (mode==2){
    	currLoad+=100;
    }
    //#]
}

void Elevator::move() {
    NOTIFY_OPERATION(move, move(), 0, Default_Elevator_move_SERIALIZE);
    //#[ operation move()
    if (direction == 1)
    	currentLevel++;
    else if (direction == 2)
    	currentLevel--;
    //#]
}

bool Elevator::needStop() {
    NOTIFY_OPERATION(needStop, needStop(), 0, Default_Elevator_needStop_SERIALIZE);
    //#[ operation needStop()
    if (stop == 1)
    	return true;
    
    if (!haveRequests()) {
    	direction = 0;
    	return true;
    }
    
    if (itsLevel[currentLevel-1].isOn()) {
    	itsLevel[currentLevel-1].setOff();
    	doorOpen = 1;
    	system->notifyState(direction, currentLevel-1);                            
    }
    
    if (direction == 1) {
    	if (upRequests[currentLevel-1] == 1) {
    		doorOpen = 1;
    		system->notifyState(direction, currentLevel-1);
    	}
    	if (!haveUpRequests() && downRequests[currentLevel-1] == 1) {
    		doorOpen = 1;
    		direction = 2;
    		system->notifyState(direction, currentLevel-1);
    	}
    	if (currentLevel == 5 && direction == 1)
    		direction = 0; 
    }
    
    else if (direction == 2) {
    	if (downRequests[currentLevel-1] == 1) {
    		doorOpen = 1;
    		system->notifyState(direction, currentLevel-1);
    	} 
    	if (!haveDownRequests() && upRequests[currentLevel-1] == 1) {
    		doorOpen = 1;
    		direction = 1;;
    		system->notifyState(direction, currentLevel-1);
    	}
    	if (currentLevel == 1 && direction == 2)
    		direction = 0; 
    }
    
    if (doorOpen == 1){
    	GEN(evOpen);
    	return true;
    }else{
    	return false;
    }
    //#]
}

void Elevator::setDownRequests(int level, int i) {
    NOTIFY_OPERATION(setDownRequests, setDownRequests(int,int), 2, Default_Elevator_setDownRequests_SERIALIZE);
    //#[ operation setDownRequests(int,int)
    downRequests[level] = i;
    //#]
}

void Elevator::setUpRequests(int level, int i) {
    NOTIFY_OPERATION(setUpRequests, setUpRequests(int,int), 2, Default_Elevator_setUpRequests_SERIALIZE);
    //#[ operation setUpRequests(int,int)
    upRequests[level] = i;
    //#]
}

void Elevator::unLoad() {
    NOTIFY_OPERATION(unLoad, unLoad(), 0, Default_Elevator_unLoad_SERIALIZE);
    //#[ operation unLoad()
    if (currLoad>0){
    	if (mode==1){
    		currLoad--;
    	}else if (mode==2){
    		currLoad-=100;
    	}
    }
    //#]
}

int Elevator::getMAX_LOAD() const {
    return MAX_LOAD;
}

void Elevator::setMAX_LOAD(int p_MAX_LOAD) {
    MAX_LOAD = p_MAX_LOAD;
}

int Elevator::getCurrLoad() const {
    return currLoad;
}

void Elevator::setCurrLoad(int p_currLoad) {
    currLoad = p_currLoad;
    NOTIFY_SET_OPERATION;
}

void Elevator::setCurrentLevel(int p_currentLevel) {
    currentLevel = p_currentLevel;
    NOTIFY_SET_OPERATION;
}

void Elevator::setDirection(int p_direction) {
    direction = p_direction;
}

int Elevator::getDoorOpen() const {
    return doorOpen;
}

void Elevator::setDoorOpen(int p_doorOpen) {
    doorOpen = p_doorOpen;
    NOTIFY_SET_OPERATION;
}

int Elevator::getDownRequests(int i1) const {
    return downRequests[i1];
}

void Elevator::setMode(int p_mode) {
    mode = p_mode;
}

int Elevator::getOverLoaded() const {
    return overLoaded;
}

void Elevator::setOverLoaded(int p_overLoaded) {
    overLoaded = p_overLoaded;
}

int Elevator::getStop() const {
    return stop;
}

void Elevator::setStop(int p_stop) {
    stop = p_stop;
}

int Elevator::getUpRequests(int i1) const {
    return upRequests[i1];
}

int Elevator::getItsLevel() const {
    int iter = 0;
    return iter;
}

SystemController* Elevator::getSystem() const {
    return system;
}

void Elevator::setSystem(SystemController* p_SystemController) {
    _setSystem(p_SystemController);
}

bool Elevator::startBehavior() {
    bool done = true;
    {
        int iter = 0;
        while (iter < 5){
            done &= (((LevelButton*)&itsLevel[iter]))->startBehavior();
            iter++;
        }
    }
    done &= OMReactive::startBehavior();
    return done;
}

void Elevator::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
    state_5_subState = OMNonState;
    state_5_active = OMNonState;
    state_4_subState = OMNonState;
    state_4_active = OMNonState;
    state_3_subState = OMNonState;
    state_3_active = OMNonState;
    state_2_subState = OMNonState;
    state_2_active = OMNonState;
    state_1_subState = OMNonState;
    state_1_active = OMNonState;
    state_1_timeout = NULL;
}

void Elevator::cleanUpRelations() {
    if(system != NULL)
        {
            NOTIFY_RELATION_CLEARED("system");
            system = NULL;
        }
}

void Elevator::cancelTimeouts() {
    cancel(state_1_timeout);
}

bool Elevator::cancelTimeout(const IOxfTimeout* arg) {
    bool res = false;
    if(state_1_timeout == arg)
        {
            state_1_timeout = NULL;
            res = true;
        }
    return res;
}

void Elevator::__setSystem(SystemController* p_SystemController) {
    system = p_SystemController;
    if(p_SystemController != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("system", p_SystemController, false, true);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("system");
        }
}

void Elevator::_setSystem(SystemController* p_SystemController) {
    __setSystem(p_SystemController);
}

void Elevator::_clearSystem() {
    NOTIFY_RELATION_CLEARED("system");
    system = NULL;
}

void Elevator::setActiveContext(IOxfActive* theActiveContext, bool activeInstance) {
    OMReactive::setActiveContext(theActiveContext, activeInstance);
    {
        for (int i = 0; i < 5; i++) 
            {
                itsLevel[i].setActiveContext(theActiveContext, false);
            }
        
    }
}

void Elevator::destroy() {
    {
        int iter = 0;
        while (iter < 5){
            (((LevelButton*)&itsLevel[iter]))->destroy();
            iter++;
        }
    }
    OMReactive::destroy();
}

void Elevator::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        rootStateEntDef();
    }
}

void Elevator::rootStateEntDef() {
    Active_entDef();
}

IOxfReactive::TakeEventStatus Elevator::rootState_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State Active
    if(rootState_active == Active)
        {
            res = Active_processEvent();
        }
    return res;
}

void Elevator::Active_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Active");
    rootState_subState = Active;
    rootState_active = Active;
    state_1_entDef();
    state_2_entDef();
    state_3_entDef();
    state_4_entDef();
    state_5_entDef();
}

void Elevator::Active_exit() {
    state_1_exit();
    switch (state_2_subState) {
        // State deactivated
        case deactivated:
        {
            NOTIFY_STATE_EXITED("ROOT.Active.state_2.deactivated");
        }
        break;
        // State activated
        case activated:
        {
            NOTIFY_STATE_EXITED("ROOT.Active.state_2.activated");
        }
        break;
        default:
            break;
    }
    state_2_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Active.state_2");
    switch (state_3_subState) {
        // State off
        case off:
        {
            popNullTransition();
            NOTIFY_STATE_EXITED("ROOT.Active.state_3.off");
        }
        break;
        // State up
        case up:
        {
            popNullTransition();
            NOTIFY_STATE_EXITED("ROOT.Active.state_3.up");
        }
        break;
        // State down
        case down:
        {
            popNullTransition();
            NOTIFY_STATE_EXITED("ROOT.Active.state_3.down");
        }
        break;
        default:
            break;
    }
    state_3_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Active.state_3");
    switch (state_4_subState) {
        // State regular
        case regular:
        {
            NOTIFY_STATE_EXITED("ROOT.Active.state_4.regular");
        }
        break;
        // State freight
        case freight:
        {
            NOTIFY_STATE_EXITED("ROOT.Active.state_4.freight");
        }
        break;
        // State maintenance
        case maintenance:
        {
            NOTIFY_STATE_EXITED("ROOT.Active.state_4.maintenance");
        }
        break;
        default:
            break;
    }
    state_4_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Active.state_4");
    switch (state_5_subState) {
        // State non_stop
        case non_stop:
        {
            NOTIFY_STATE_EXITED("ROOT.Active.state_5.non_stop");
        }
        break;
        // State stopped
        case stopped:
        {
            NOTIFY_STATE_EXITED("ROOT.Active.state_5.stopped");
        }
        break;
        default:
            break;
    }
    state_5_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Active.state_5");
    
    NOTIFY_STATE_EXITED("ROOT.Active");
}

IOxfReactive::TakeEventStatus Elevator::Active_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State state_1
    if(state_1_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(Active))
                {
                    return res;
                }
        }
    // State state_2
    if(state_2_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(Active))
                {
                    return res;
                }
        }
    // State state_3
    if(state_3_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(Active))
                {
                    return res;
                }
        }
    // State state_4
    if(state_4_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(Active))
                {
                    return res;
                }
        }
    // State state_5
    if(state_5_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(Active))
                {
                    return res;
                }
        }
    
    return res;
}

void Elevator::state_5_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Active.state_5");
    NOTIFY_TRANSITION_STARTED("29");
    NOTIFY_STATE_ENTERED("ROOT.Active.state_5.non_stop");
    state_5_subState = non_stop;
    state_5_active = non_stop;
    //#[ state Active.state_5.non_stop.(Entry) 
    stop=0;
    //#]
    NOTIFY_TRANSITION_TERMINATED("29");
}

IOxfReactive::TakeEventStatus Elevator::state_5_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_5_active) {
        // State non_stop
        case non_stop:
        {
            if(IS_EVENT_TYPE_OF(evStop_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("27");
                    NOTIFY_STATE_EXITED("ROOT.Active.state_5.non_stop");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_5.stopped");
                    state_5_subState = stopped;
                    state_5_active = stopped;
                    //#[ state Active.state_5.stopped.(Entry) 
                    stop=1;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("27");
                    res = eventConsumed;
                }
            
            
        }
        break;
        // State stopped
        case stopped:
        {
            if(IS_EVENT_TYPE_OF(evStop_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("28");
                    NOTIFY_STATE_EXITED("ROOT.Active.state_5.stopped");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_5.non_stop");
                    state_5_subState = non_stop;
                    state_5_active = non_stop;
                    //#[ state Active.state_5.non_stop.(Entry) 
                    stop=0;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("28");
                    res = eventConsumed;
                }
            
            
        }
        break;
        default:
            break;
    }
    return res;
}

void Elevator::state_4_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Active.state_4");
    NOTIFY_TRANSITION_STARTED("20");
    NOTIFY_STATE_ENTERED("ROOT.Active.state_4.regular");
    state_4_subState = regular;
    state_4_active = regular;
    //#[ state Active.state_4.regular.(Entry) 
    mode=1;
    //#]
    NOTIFY_TRANSITION_TERMINATED("20");
}

IOxfReactive::TakeEventStatus Elevator::state_4_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_4_active) {
        // State regular
        case regular:
        {
            if(IS_EVENT_TYPE_OF(evFreight_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("21");
                    NOTIFY_STATE_EXITED("ROOT.Active.state_4.regular");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_4.freight");
                    state_4_subState = freight;
                    state_4_active = freight;
                    //#[ state Active.state_4.freight.(Entry) 
                    mode=2;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("21");
                    res = eventConsumed;
                }
            else if(IS_EVENT_TYPE_OF(evMaintenance_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("26");
                    NOTIFY_STATE_EXITED("ROOT.Active.state_4.regular");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_4.maintenance");
                    state_4_subState = maintenance;
                    state_4_active = maintenance;
                    //#[ state Active.state_4.maintenance.(Entry) 
                    mode=3;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("26");
                    res = eventConsumed;
                }
            
            
        }
        break;
        // State freight
        case freight:
        {
            if(IS_EVENT_TYPE_OF(evRegular_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("22");
                    NOTIFY_STATE_EXITED("ROOT.Active.state_4.freight");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_4.regular");
                    state_4_subState = regular;
                    state_4_active = regular;
                    //#[ state Active.state_4.regular.(Entry) 
                    mode=1;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("22");
                    res = eventConsumed;
                }
            else if(IS_EVENT_TYPE_OF(evMaintenance_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("24");
                    NOTIFY_STATE_EXITED("ROOT.Active.state_4.freight");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_4.maintenance");
                    state_4_subState = maintenance;
                    state_4_active = maintenance;
                    //#[ state Active.state_4.maintenance.(Entry) 
                    mode=3;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("24");
                    res = eventConsumed;
                }
            
            
        }
        break;
        // State maintenance
        case maintenance:
        {
            if(IS_EVENT_TYPE_OF(evFreight_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("23");
                    NOTIFY_STATE_EXITED("ROOT.Active.state_4.maintenance");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_4.freight");
                    state_4_subState = freight;
                    state_4_active = freight;
                    //#[ state Active.state_4.freight.(Entry) 
                    mode=2;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("23");
                    res = eventConsumed;
                }
            else if(IS_EVENT_TYPE_OF(evRegular_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("25");
                    NOTIFY_STATE_EXITED("ROOT.Active.state_4.maintenance");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_4.regular");
                    state_4_subState = regular;
                    state_4_active = regular;
                    //#[ state Active.state_4.regular.(Entry) 
                    mode=1;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("25");
                    res = eventConsumed;
                }
            
            
        }
        break;
        default:
            break;
    }
    return res;
}

void Elevator::state_3_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Active.state_3");
    NOTIFY_TRANSITION_STARTED("13");
    NOTIFY_STATE_ENTERED("ROOT.Active.state_3.off");
    pushNullTransition();
    state_3_subState = off;
    state_3_active = off;
    NOTIFY_TRANSITION_TERMINATED("13");
}

IOxfReactive::TakeEventStatus Elevator::state_3_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_3_active) {
        // State off
        case off:
        {
            if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 14 
                    if(direction==1)
                        {
                            NOTIFY_TRANSITION_STARTED("14");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.Active.state_3.off");
                            NOTIFY_STATE_ENTERED("ROOT.Active.state_3.up");
                            pushNullTransition();
                            state_3_subState = up;
                            state_3_active = up;
                            NOTIFY_TRANSITION_TERMINATED("14");
                            res = eventConsumed;
                        }
                    else
                        {
                            //## transition 18 
                            if(direction==2)
                                {
                                    NOTIFY_TRANSITION_STARTED("18");
                                    popNullTransition();
                                    NOTIFY_STATE_EXITED("ROOT.Active.state_3.off");
                                    NOTIFY_STATE_ENTERED("ROOT.Active.state_3.down");
                                    pushNullTransition();
                                    state_3_subState = down;
                                    state_3_active = down;
                                    NOTIFY_TRANSITION_TERMINATED("18");
                                    res = eventConsumed;
                                }
                        }
                }
            
            
        }
        break;
        // State up
        case up:
        {
            if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 15 
                    if(direction==0)
                        {
                            NOTIFY_TRANSITION_STARTED("15");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.Active.state_3.up");
                            NOTIFY_STATE_ENTERED("ROOT.Active.state_3.off");
                            pushNullTransition();
                            state_3_subState = off;
                            state_3_active = off;
                            NOTIFY_TRANSITION_TERMINATED("15");
                            res = eventConsumed;
                        }
                    else
                        {
                            //## transition 17 
                            if(direction==2)
                                {
                                    NOTIFY_TRANSITION_STARTED("17");
                                    popNullTransition();
                                    NOTIFY_STATE_EXITED("ROOT.Active.state_3.up");
                                    NOTIFY_STATE_ENTERED("ROOT.Active.state_3.down");
                                    pushNullTransition();
                                    state_3_subState = down;
                                    state_3_active = down;
                                    NOTIFY_TRANSITION_TERMINATED("17");
                                    res = eventConsumed;
                                }
                        }
                }
            
            
        }
        break;
        // State down
        case down:
        {
            if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 16 
                    if(direction==1)
                        {
                            NOTIFY_TRANSITION_STARTED("16");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.Active.state_3.down");
                            NOTIFY_STATE_ENTERED("ROOT.Active.state_3.up");
                            pushNullTransition();
                            state_3_subState = up;
                            state_3_active = up;
                            NOTIFY_TRANSITION_TERMINATED("16");
                            res = eventConsumed;
                        }
                    else
                        {
                            //## transition 19 
                            if(direction==0)
                                {
                                    NOTIFY_TRANSITION_STARTED("19");
                                    popNullTransition();
                                    NOTIFY_STATE_EXITED("ROOT.Active.state_3.down");
                                    NOTIFY_STATE_ENTERED("ROOT.Active.state_3.off");
                                    pushNullTransition();
                                    state_3_subState = off;
                                    state_3_active = off;
                                    NOTIFY_TRANSITION_TERMINATED("19");
                                    res = eventConsumed;
                                }
                        }
                }
            
            
        }
        break;
        default:
            break;
    }
    return res;
}

void Elevator::state_2_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Active.state_2");
    NOTIFY_TRANSITION_STARTED("10");
    NOTIFY_STATE_ENTERED("ROOT.Active.state_2.deactivated");
    state_2_subState = deactivated;
    state_2_active = deactivated;
    NOTIFY_TRANSITION_TERMINATED("10");
}

IOxfReactive::TakeEventStatus Elevator::state_2_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_2_active) {
        // State deactivated
        case deactivated:
        {
            if(IS_EVENT_TYPE_OF(evAlarm_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("11");
                    NOTIFY_STATE_EXITED("ROOT.Active.state_2.deactivated");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_2.activated");
                    state_2_subState = activated;
                    state_2_active = activated;
                    NOTIFY_TRANSITION_TERMINATED("11");
                    res = eventConsumed;
                }
            
            
        }
        break;
        // State activated
        case activated:
        {
            if(IS_EVENT_TYPE_OF(evAlarm_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("12");
                    NOTIFY_STATE_EXITED("ROOT.Active.state_2.activated");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_2.deactivated");
                    state_2_subState = deactivated;
                    state_2_active = deactivated;
                    NOTIFY_TRANSITION_TERMINATED("12");
                    res = eventConsumed;
                }
            
            
        }
        break;
        default:
            break;
    }
    return res;
}

void Elevator::state_1_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Active.state_1");
    NOTIFY_TRANSITION_STARTED("0");
    NOTIFY_STATE_ENTERED("ROOT.Active.state_1.idle");
    pushNullTransition();
    state_1_subState = idle;
    state_1_active = idle;
    state_1_timeout = scheduleTimeout(600, "ROOT.Active.state_1.idle");
    NOTIFY_TRANSITION_TERMINATED("0");
}

void Elevator::state_1_exit() {
    switch (state_1_subState) {
        // State idle
        case idle:
        {
            popNullTransition();
            cancel(state_1_timeout);
            NOTIFY_STATE_EXITED("ROOT.Active.state_1.idle");
        }
        break;
        // State door_open
        case door_open:
        {
            cancel(state_1_timeout);
            NOTIFY_STATE_EXITED("ROOT.Active.state_1.door_open");
        }
        break;
        // State running
        case running:
        {
            popNullTransition();
            cancel(state_1_timeout);
            NOTIFY_STATE_EXITED("ROOT.Active.state_1.running");
        }
        break;
        // State overLoad
        case overLoad:
        {
            popNullTransition();
            NOTIFY_STATE_EXITED("ROOT.Active.state_1.overLoad");
        }
        break;
        default:
            break;
    }
    state_1_subState = OMNonState;
    
    NOTIFY_STATE_EXITED("ROOT.Active.state_1");
}

IOxfReactive::TakeEventStatus Elevator::state_1_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_1_active) {
        // State idle
        case idle:
        {
            res = idle_handleEvent();
        }
        break;
        // State door_open
        case door_open:
        {
            res = door_open_handleEvent();
        }
        break;
        // State running
        case running:
        {
            if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
                {
                    if(getCurrentEvent() == state_1_timeout)
                        {
                            NOTIFY_TRANSITION_STARTED("9");
                            popNullTransition();
                            cancel(state_1_timeout);
                            NOTIFY_STATE_EXITED("ROOT.Active.state_1.running");
                            //#[ transition 9 
                            move();
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.Active.state_1.running");
                            pushNullTransition();
                            state_1_subState = running;
                            state_1_active = running;
                            state_1_timeout = scheduleTimeout(1500, "ROOT.Active.state_1.running");
                            NOTIFY_TRANSITION_TERMINATED("9");
                            res = eventConsumed;
                        }
                }
            else if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 8 
                    if(needStop())
                        {
                            NOTIFY_TRANSITION_STARTED("8");
                            popNullTransition();
                            cancel(state_1_timeout);
                            NOTIFY_STATE_EXITED("ROOT.Active.state_1.running");
                            NOTIFY_STATE_ENTERED("ROOT.Active.state_1.idle");
                            pushNullTransition();
                            state_1_subState = idle;
                            state_1_active = idle;
                            state_1_timeout = scheduleTimeout(600, "ROOT.Active.state_1.idle");
                            NOTIFY_TRANSITION_TERMINATED("8");
                            res = eventConsumed;
                        }
                }
            
            
        }
        break;
        // State overLoad
        case overLoad:
        {
            if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 1 
                    if(currLoad<=MAX_LOAD)
                        {
                            NOTIFY_TRANSITION_STARTED("34");
                            NOTIFY_TRANSITION_STARTED("1");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.Active.state_1.overLoad");
                            //#[ transition 1 
                            cout<<"door closed"<<endl;
                            doorOpen=0;
                            overLoaded=0;
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.Active.state_1.idle");
                            pushNullTransition();
                            state_1_subState = idle;
                            state_1_active = idle;
                            state_1_timeout = scheduleTimeout(600, "ROOT.Active.state_1.idle");
                            NOTIFY_TRANSITION_TERMINATED("1");
                            NOTIFY_TRANSITION_TERMINATED("34");
                            res = eventConsumed;
                        }
                    else
                        {
                            NOTIFY_TRANSITION_STARTED("34");
                            NOTIFY_TRANSITION_STARTED("36");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.Active.state_1.overLoad");
                            //#[ transition 36 
                            overLoaded=1;
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.Active.state_1.door_open");
                            state_1_subState = door_open;
                            state_1_active = door_open;
                            state_1_timeout = scheduleTimeout(4000, "ROOT.Active.state_1.door_open");
                            NOTIFY_TRANSITION_TERMINATED("36");
                            NOTIFY_TRANSITION_TERMINATED("34");
                            res = eventConsumed;
                        }
                }
            
            
        }
        break;
        default:
            break;
    }
    return res;
}

IOxfReactive::TakeEventStatus Elevator::idle_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
        {
            if(getCurrentEvent() == state_1_timeout)
                {
                    NOTIFY_TRANSITION_STARTED("3");
                    popNullTransition();
                    cancel(state_1_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Active.state_1.idle");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_1.idle");
                    pushNullTransition();
                    state_1_subState = idle;
                    state_1_active = idle;
                    state_1_timeout = scheduleTimeout(600, "ROOT.Active.state_1.idle");
                    NOTIFY_TRANSITION_TERMINATED("3");
                    res = eventConsumed;
                }
        }
    else if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            //## transition 4 
            if(doorOpen==0&&mode!=3&&stop==0)
                {
                    //## transition 5 
                    if(haveRequests())
                        {
                            if(TRUE)
                                {
                                    NOTIFY_TRANSITION_STARTED("4");
                                    NOTIFY_TRANSITION_STARTED("5");
                                    NOTIFY_TRANSITION_STARTED("7");
                                    popNullTransition();
                                    cancel(state_1_timeout);
                                    NOTIFY_STATE_EXITED("ROOT.Active.state_1.idle");
                                    NOTIFY_STATE_ENTERED("ROOT.Active.state_1.running");
                                    pushNullTransition();
                                    state_1_subState = running;
                                    state_1_active = running;
                                    state_1_timeout = scheduleTimeout(1500, "ROOT.Active.state_1.running");
                                    NOTIFY_TRANSITION_TERMINATED("7");
                                    NOTIFY_TRANSITION_TERMINATED("5");
                                    NOTIFY_TRANSITION_TERMINATED("4");
                                    res = eventConsumed;
                                }
                        }
                }
        }
    else if(IS_EVENT_TYPE_OF(evOpen_Default_id))
        {
            NOTIFY_TRANSITION_STARTED("2");
            popNullTransition();
            cancel(state_1_timeout);
            NOTIFY_STATE_EXITED("ROOT.Active.state_1.idle");
            //#[ transition 2 
            doorOpen=1;
            //#]
            NOTIFY_STATE_ENTERED("ROOT.Active.state_1.door_open");
            state_1_subState = door_open;
            state_1_active = door_open;
            state_1_timeout = scheduleTimeout(4000, "ROOT.Active.state_1.door_open");
            NOTIFY_TRANSITION_TERMINATED("2");
            res = eventConsumed;
        }
    
    
    return res;
}

IOxfReactive::TakeEventStatus Elevator::door_open_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
        {
            if(getCurrentEvent() == state_1_timeout)
                {
                    NOTIFY_TRANSITION_STARTED("32");
                    cancel(state_1_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Active.state_1.door_open");
                    NOTIFY_STATE_ENTERED("ROOT.Active.state_1.overLoad");
                    pushNullTransition();
                    state_1_subState = overLoad;
                    state_1_active = overLoad;
                    NOTIFY_TRANSITION_TERMINATED("32");
                    res = eventConsumed;
                }
        }
    else if(IS_EVENT_TYPE_OF(evLoad_Default_id))
        {
            NOTIFY_TRANSITION_STARTED("30");
            cancel(state_1_timeout);
            NOTIFY_STATE_EXITED("ROOT.Active.state_1.door_open");
            //#[ transition 30 
            load();
            //#]
            NOTIFY_STATE_ENTERED("ROOT.Active.state_1.door_open");
            state_1_subState = door_open;
            state_1_active = door_open;
            state_1_timeout = scheduleTimeout(4000, "ROOT.Active.state_1.door_open");
            NOTIFY_TRANSITION_TERMINATED("30");
            res = eventConsumed;
        }
    else if(IS_EVENT_TYPE_OF(evClose_Default_id))
        {
            NOTIFY_TRANSITION_STARTED("33");
            cancel(state_1_timeout);
            NOTIFY_STATE_EXITED("ROOT.Active.state_1.door_open");
            NOTIFY_STATE_ENTERED("ROOT.Active.state_1.overLoad");
            pushNullTransition();
            state_1_subState = overLoad;
            state_1_active = overLoad;
            NOTIFY_TRANSITION_TERMINATED("33");
            res = eventConsumed;
        }
    else if(IS_EVENT_TYPE_OF(evUnload_Default_id))
        {
            NOTIFY_TRANSITION_STARTED("31");
            cancel(state_1_timeout);
            NOTIFY_STATE_EXITED("ROOT.Active.state_1.door_open");
            //#[ transition 31 
            unLoad();
            //#]
            NOTIFY_STATE_ENTERED("ROOT.Active.state_1.door_open");
            state_1_subState = door_open;
            state_1_active = door_open;
            state_1_timeout = scheduleTimeout(4000, "ROOT.Active.state_1.door_open");
            NOTIFY_TRANSITION_TERMINATED("31");
            res = eventConsumed;
        }
    
    
    return res;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedElevator::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("currentLevel", x2String(myReal->currentLevel));
    aomsAttributes->addAttribute("direction", x2String(myReal->direction));
    aomsAttributes->addAttribute("doorOpen", x2String(myReal->doorOpen));
    aomsAttributes->addAttribute("downRequests", array2String(5, myReal->downRequests, sizeof(int), &x2String));
    aomsAttributes->addAttribute("mode", x2String(myReal->mode));
    aomsAttributes->addAttribute("stop", x2String(myReal->stop));
    aomsAttributes->addAttribute("upRequests", array2String(5, myReal->upRequests, sizeof(int), &x2String));
    aomsAttributes->addAttribute("currLoad", x2String(myReal->currLoad));
    aomsAttributes->addAttribute("MAX_LOAD", x2String(myReal->MAX_LOAD));
    aomsAttributes->addAttribute("overLoaded", x2String(myReal->overLoaded));
}

void OMAnimatedElevator::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsLevel", true, false);
    {
        int iter = 0;
        while (iter < 5){
            aomsRelations->ADD_ITEM(((LevelButton*)&myReal->itsLevel[iter]));
            iter++;
        }
    }
    aomsRelations->addRelation("system", false, true);
    if(myReal->system)
        {
            aomsRelations->ADD_ITEM(myReal->system);
        }
}

void OMAnimatedElevator::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    if(myReal->rootState_subState == Elevator::Active)
        {
            Active_serializeStates(aomsState);
        }
}

void OMAnimatedElevator::Active_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active");
    state_1_serializeStates(aomsState);
    state_2_serializeStates(aomsState);
    state_3_serializeStates(aomsState);
    state_4_serializeStates(aomsState);
    state_5_serializeStates(aomsState);
}

void OMAnimatedElevator::state_5_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_5");
    switch (myReal->state_5_subState) {
        case Elevator::non_stop:
        {
            non_stop_serializeStates(aomsState);
        }
        break;
        case Elevator::stopped:
        {
            stopped_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedElevator::stopped_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_5.stopped");
}

void OMAnimatedElevator::non_stop_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_5.non_stop");
}

void OMAnimatedElevator::state_4_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_4");
    switch (myReal->state_4_subState) {
        case Elevator::regular:
        {
            regular_serializeStates(aomsState);
        }
        break;
        case Elevator::freight:
        {
            freight_serializeStates(aomsState);
        }
        break;
        case Elevator::maintenance:
        {
            maintenance_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedElevator::regular_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_4.regular");
}

void OMAnimatedElevator::maintenance_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_4.maintenance");
}

void OMAnimatedElevator::freight_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_4.freight");
}

void OMAnimatedElevator::state_3_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_3");
    switch (myReal->state_3_subState) {
        case Elevator::off:
        {
            off_serializeStates(aomsState);
        }
        break;
        case Elevator::up:
        {
            up_serializeStates(aomsState);
        }
        break;
        case Elevator::down:
        {
            down_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedElevator::up_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_3.up");
}

void OMAnimatedElevator::off_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_3.off");
}

void OMAnimatedElevator::down_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_3.down");
}

void OMAnimatedElevator::state_2_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_2");
    switch (myReal->state_2_subState) {
        case Elevator::deactivated:
        {
            deactivated_serializeStates(aomsState);
        }
        break;
        case Elevator::activated:
        {
            activated_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedElevator::deactivated_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_2.deactivated");
}

void OMAnimatedElevator::activated_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_2.activated");
}

void OMAnimatedElevator::state_1_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_1");
    switch (myReal->state_1_subState) {
        case Elevator::idle:
        {
            idle_serializeStates(aomsState);
        }
        break;
        case Elevator::door_open:
        {
            door_open_serializeStates(aomsState);
        }
        break;
        case Elevator::running:
        {
            running_serializeStates(aomsState);
        }
        break;
        case Elevator::overLoad:
        {
            overLoad_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedElevator::running_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_1.running");
}

void OMAnimatedElevator::overLoad_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_1.overLoad");
}

void OMAnimatedElevator::idle_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_1.idle");
}

void OMAnimatedElevator::door_open_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Active.state_1.door_open");
}
//#]

IMPLEMENT_REACTIVE_META_P(Elevator, Default, Default, false, OMAnimatedElevator)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: DefaultComponent\Debug\Elevator.cpp
*********************************************************************/
