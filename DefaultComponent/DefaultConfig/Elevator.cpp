/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: DefaultConfig
	Model Element	: Elevator
//!	Generated Date	: Tue, 6, Oct 2015  
	File Path	: DefaultComponent\DefaultConfig\Elevator.cpp
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

Elevator::Elevator(IOxfActive* theActiveContext) : currentLevel(1), direction(0), doorOpen(0), mode(1), stop(0) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Elevator, Elevator(), 0, Default_Elevator_Elevator_SERIALIZE);
    setActiveContext(theActiveContext, false);
    {
        for (int i = 0; i < 6; i++) 
            {
                itsLevel[i].setShouldDelete(false);
            }
        
    }
    system = NULL;
    initStatechart();
    //#[ operation Elevator()
    currentLevel = 1;   
    displayLevel = 0; 
    currLoad=0;
    overLoaded=0;
    MAX_LOAD=800;
    for (int i = 0; i < 6; i++) {
    	upRequests[i] = 0;
    	downRequests[i] = 0;
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
    	for (int i = currentLevel; i <= 6; i++) {
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
    	for (int i = currentLevel; i <= 6; i++) {
    		if (itsLevel[i-1].isOn() || upRequests[i-1] == 1 || downRequests[i-1] == 1) {
    			direction = 1;
    			return true;  
    		}
    	} 
    }
    else {
    	for (int i = currentLevel; i <= 6; i++) {
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
    for (int i = currentLevel; i <= 6; i++) {
    	if (itsLevel[i-1].isOn() || upRequests[i-1] == 1) {
    		return true;  
    	}
    } 
    return false;
    //#]
}

void Elevator::move() {
    NOTIFY_OPERATION(move, move(), 0, Default_Elevator_move_SERIALIZE);
    //#[ operation move()
    if (direction == 1){
    	currentLevel++;
    	displayLevel=currentLevel-1;
    }
    else if (direction == 2){
    	currentLevel--;
    	displayLevel=currentLevel-1;
    }
    
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
    	if (currentLevel == 6 && direction == 1)
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
        while (iter < 6){
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
    state_8_subState = OMNonState;
    state_8_active = OMNonState;
    state_5_subState = OMNonState;
    state_5_active = OMNonState;
    state_4_subState = OMNonState;
    state_4_active = OMNonState;
    state_4_timeout = NULL;
    state_16_subState = OMNonState;
    state_16_active = OMNonState;
    state_12_subState = OMNonState;
    state_12_active = OMNonState;
}

void Elevator::cleanUpRelations() {
    if(system != NULL)
        {
            NOTIFY_RELATION_CLEARED("system");
            system = NULL;
        }
}

void Elevator::cancelTimeouts() {
    cancel(state_4_timeout);
}

bool Elevator::cancelTimeout(const IOxfTimeout* arg) {
    bool res = false;
    if(state_4_timeout == arg)
        {
            state_4_timeout = NULL;
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
        for (int i = 0; i < 6; i++) 
            {
                itsLevel[i].setActiveContext(theActiveContext, false);
            }
        
    }
}

void Elevator::destroy() {
    {
        int iter = 0;
        while (iter < 6){
            (((LevelButton*)&itsLevel[iter]))->destroy();
            iter++;
        }
    }
    OMReactive::destroy();
}

void Elevator::load() {
    NOTIFY_OPERATION(load, load(), 0, Default_Elevator_load_SERIALIZE);
    //#[ operation load()
    currLoad+=60;
    //#]
}

void Elevator::unLoad() {
    NOTIFY_OPERATION(unLoad, unLoad(), 0, Default_Elevator_unLoad_SERIALIZE);
    //#[ operation unLoad()
    if (currLoad>0){
    	currLoad-=60;
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

int Elevator::getDisplayLevel() const {
    return displayLevel;
}

void Elevator::setDisplayLevel(int p_displayLevel) {
    displayLevel = p_displayLevel;
    NOTIFY_SET_OPERATION;
}

int Elevator::getOverLoaded() const {
    return overLoaded;
}

void Elevator::setOverLoaded(int p_overLoaded) {
    overLoaded = p_overLoaded;
    NOTIFY_SET_OPERATION;
}

void Elevator::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        rootStateEntDef();
    }
}

void Elevator::rootStateEntDef() {
    active_entDef();
}

IOxfReactive::TakeEventStatus Elevator::rootState_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State active
    if(rootState_active == active)
        {
            res = active_processEvent();
        }
    return res;
}

void Elevator::active_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.active");
    rootState_subState = active;
    rootState_active = active;
    state_4_entDef();
    state_5_entDef();
    state_8_entDef();
    state_12_entDef();
    state_16_entDef();
}

void Elevator::active_exit() {
    state_4_exit();
    switch (state_5_subState) {
        // State deactivated
        case deactivated:
        {
            NOTIFY_STATE_EXITED("ROOT.active.state_5.deactivated");
        }
        break;
        // State activated
        case activated:
        {
            NOTIFY_STATE_EXITED("ROOT.active.state_5.activated");
        }
        break;
        default:
            break;
    }
    state_5_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.active.state_5");
    switch (state_8_subState) {
        // State off
        case off:
        {
            popNullTransition();
            NOTIFY_STATE_EXITED("ROOT.active.state_8.off");
        }
        break;
        // State up
        case up:
        {
            popNullTransition();
            NOTIFY_STATE_EXITED("ROOT.active.state_8.up");
        }
        break;
        // State down
        case down:
        {
            popNullTransition();
            NOTIFY_STATE_EXITED("ROOT.active.state_8.down");
        }
        break;
        default:
            break;
    }
    state_8_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.active.state_8");
    switch (state_12_subState) {
        // State regular
        case regular:
        {
            NOTIFY_STATE_EXITED("ROOT.active.state_12.regular");
        }
        break;
        // State freight
        case freight:
        {
            NOTIFY_STATE_EXITED("ROOT.active.state_12.freight");
        }
        break;
        // State maintenance
        case maintenance:
        {
            NOTIFY_STATE_EXITED("ROOT.active.state_12.maintenance");
        }
        break;
        default:
            break;
    }
    state_12_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.active.state_12");
    switch (state_16_subState) {
        // State stopped
        case stopped:
        {
            NOTIFY_STATE_EXITED("ROOT.active.state_16.stopped");
        }
        break;
        // State non_stop
        case non_stop:
        {
            NOTIFY_STATE_EXITED("ROOT.active.state_16.non_stop");
        }
        break;
        default:
            break;
    }
    state_16_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.active.state_16");
    
    NOTIFY_STATE_EXITED("ROOT.active");
}

IOxfReactive::TakeEventStatus Elevator::active_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State state_4
    if(state_4_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(active))
                {
                    return res;
                }
        }
    // State state_5
    if(state_5_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(active))
                {
                    return res;
                }
        }
    // State state_8
    if(state_8_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(active))
                {
                    return res;
                }
        }
    // State state_12
    if(state_12_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(active))
                {
                    return res;
                }
        }
    // State state_16
    if(state_16_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(active))
                {
                    return res;
                }
        }
    
    return res;
}

void Elevator::state_8_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.active.state_8");
    NOTIFY_TRANSITION_STARTED("14");
    NOTIFY_STATE_ENTERED("ROOT.active.state_8.off");
    pushNullTransition();
    state_8_subState = off;
    state_8_active = off;
    NOTIFY_TRANSITION_TERMINATED("14");
}

IOxfReactive::TakeEventStatus Elevator::state_8_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_8_active) {
        // State off
        case off:
        {
            if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 15 
                    if(direction==1)
                        {
                            NOTIFY_TRANSITION_STARTED("15");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.active.state_8.off");
                            NOTIFY_STATE_ENTERED("ROOT.active.state_8.up");
                            pushNullTransition();
                            state_8_subState = up;
                            state_8_active = up;
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
                                    NOTIFY_STATE_EXITED("ROOT.active.state_8.off");
                                    NOTIFY_STATE_ENTERED("ROOT.active.state_8.down");
                                    pushNullTransition();
                                    state_8_subState = down;
                                    state_8_active = down;
                                    NOTIFY_TRANSITION_TERMINATED("17");
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
                    //## transition 16 
                    if(direction==0)
                        {
                            NOTIFY_TRANSITION_STARTED("16");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.active.state_8.up");
                            NOTIFY_STATE_ENTERED("ROOT.active.state_8.off");
                            pushNullTransition();
                            state_8_subState = off;
                            state_8_active = off;
                            NOTIFY_TRANSITION_TERMINATED("16");
                            res = eventConsumed;
                        }
                    else
                        {
                            //## transition 19 
                            if(direction==2)
                                {
                                    NOTIFY_TRANSITION_STARTED("19");
                                    popNullTransition();
                                    NOTIFY_STATE_EXITED("ROOT.active.state_8.up");
                                    NOTIFY_STATE_ENTERED("ROOT.active.state_8.down");
                                    pushNullTransition();
                                    state_8_subState = down;
                                    state_8_active = down;
                                    NOTIFY_TRANSITION_TERMINATED("19");
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
                    //## transition 18 
                    if(direction==0)
                        {
                            NOTIFY_TRANSITION_STARTED("18");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.active.state_8.down");
                            NOTIFY_STATE_ENTERED("ROOT.active.state_8.off");
                            pushNullTransition();
                            state_8_subState = off;
                            state_8_active = off;
                            NOTIFY_TRANSITION_TERMINATED("18");
                            res = eventConsumed;
                        }
                    else
                        {
                            //## transition 20 
                            if(direction==1)
                                {
                                    NOTIFY_TRANSITION_STARTED("20");
                                    popNullTransition();
                                    NOTIFY_STATE_EXITED("ROOT.active.state_8.down");
                                    NOTIFY_STATE_ENTERED("ROOT.active.state_8.up");
                                    pushNullTransition();
                                    state_8_subState = up;
                                    state_8_active = up;
                                    NOTIFY_TRANSITION_TERMINATED("20");
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

void Elevator::state_5_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.active.state_5");
    NOTIFY_TRANSITION_STARTED("11");
    NOTIFY_STATE_ENTERED("ROOT.active.state_5.deactivated");
    state_5_subState = deactivated;
    state_5_active = deactivated;
    NOTIFY_TRANSITION_TERMINATED("11");
}

IOxfReactive::TakeEventStatus Elevator::state_5_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_5_active) {
        // State deactivated
        case deactivated:
        {
            if(IS_EVENT_TYPE_OF(evAlarm_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("12");
                    NOTIFY_STATE_EXITED("ROOT.active.state_5.deactivated");
                    NOTIFY_STATE_ENTERED("ROOT.active.state_5.activated");
                    state_5_subState = activated;
                    state_5_active = activated;
                    NOTIFY_TRANSITION_TERMINATED("12");
                    res = eventConsumed;
                }
            
            
        }
        break;
        // State activated
        case activated:
        {
            if(IS_EVENT_TYPE_OF(evAlarm_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("13");
                    NOTIFY_STATE_EXITED("ROOT.active.state_5.activated");
                    NOTIFY_STATE_ENTERED("ROOT.active.state_5.deactivated");
                    state_5_subState = deactivated;
                    state_5_active = deactivated;
                    NOTIFY_TRANSITION_TERMINATED("13");
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
    NOTIFY_STATE_ENTERED("ROOT.active.state_4");
    NOTIFY_TRANSITION_STARTED("0");
    NOTIFY_STATE_ENTERED("ROOT.active.state_4.idle");
    pushNullTransition();
    state_4_subState = idle;
    state_4_active = idle;
    state_4_timeout = scheduleTimeout(600, "ROOT.active.state_4.idle");
    NOTIFY_TRANSITION_TERMINATED("0");
}

void Elevator::state_4_exit() {
    switch (state_4_subState) {
        // State idle
        case idle:
        {
            popNullTransition();
            cancel(state_4_timeout);
            NOTIFY_STATE_EXITED("ROOT.active.state_4.idle");
        }
        break;
        // State running
        case running:
        {
            popNullTransition();
            cancel(state_4_timeout);
            NOTIFY_STATE_EXITED("ROOT.active.state_4.running");
        }
        break;
        // State door_open
        case door_open:
        {
            cancel(state_4_timeout);
            NOTIFY_STATE_EXITED("ROOT.active.state_4.door_open");
        }
        break;
        // State over_load
        case over_load:
        {
            popNullTransition();
            NOTIFY_STATE_EXITED("ROOT.active.state_4.over_load");
        }
        break;
        default:
            break;
    }
    state_4_subState = OMNonState;
    
    NOTIFY_STATE_EXITED("ROOT.active.state_4");
}

IOxfReactive::TakeEventStatus Elevator::state_4_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_4_active) {
        // State idle
        case idle:
        {
            res = idle_handleEvent();
        }
        break;
        // State running
        case running:
        {
            if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
                {
                    if(getCurrentEvent() == state_4_timeout)
                        {
                            NOTIFY_TRANSITION_STARTED("3");
                            popNullTransition();
                            cancel(state_4_timeout);
                            NOTIFY_STATE_EXITED("ROOT.active.state_4.running");
                            //#[ transition 3 
                            move();
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.active.state_4.running");
                            pushNullTransition();
                            state_4_subState = running;
                            state_4_active = running;
                            state_4_timeout = scheduleTimeout(1500, "ROOT.active.state_4.running");
                            NOTIFY_TRANSITION_TERMINATED("3");
                            res = eventConsumed;
                        }
                }
            else if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 4 
                    if(needStop())
                        {
                            NOTIFY_TRANSITION_STARTED("4");
                            popNullTransition();
                            cancel(state_4_timeout);
                            NOTIFY_STATE_EXITED("ROOT.active.state_4.running");
                            NOTIFY_STATE_ENTERED("ROOT.active.state_4.idle");
                            pushNullTransition();
                            state_4_subState = idle;
                            state_4_active = idle;
                            state_4_timeout = scheduleTimeout(600, "ROOT.active.state_4.idle");
                            NOTIFY_TRANSITION_TERMINATED("4");
                            res = eventConsumed;
                        }
                }
            
            
        }
        break;
        // State door_open
        case door_open:
        {
            res = door_open_handleEvent();
        }
        break;
        // State over_load
        case over_load:
        {
            if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 7 
                    if(currLoad<=MAX_LOAD)
                        {
                            NOTIFY_TRANSITION_STARTED("34");
                            NOTIFY_TRANSITION_STARTED("7");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.active.state_4.over_load");
                            //#[ transition 7 
                            cout<<"door closed"<<endl;
                            doorOpen=0;
                            overLoaded=0;
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.active.state_4.idle");
                            pushNullTransition();
                            state_4_subState = idle;
                            state_4_active = idle;
                            state_4_timeout = scheduleTimeout(600, "ROOT.active.state_4.idle");
                            NOTIFY_TRANSITION_TERMINATED("7");
                            NOTIFY_TRANSITION_TERMINATED("34");
                            res = eventConsumed;
                        }
                    else
                        {
                            NOTIFY_TRANSITION_STARTED("34");
                            NOTIFY_TRANSITION_STARTED("35");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.active.state_4.over_load");
                            //#[ transition 35 
                            cout<<"over loaded"<<endl;
                            overLoaded=1;
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.active.state_4.door_open");
                            state_4_subState = door_open;
                            state_4_active = door_open;
                            state_4_timeout = scheduleTimeout(4000, "ROOT.active.state_4.door_open");
                            NOTIFY_TRANSITION_TERMINATED("35");
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
            if(getCurrentEvent() == state_4_timeout)
                {
                    NOTIFY_TRANSITION_STARTED("6");
                    popNullTransition();
                    cancel(state_4_timeout);
                    NOTIFY_STATE_EXITED("ROOT.active.state_4.idle");
                    NOTIFY_STATE_ENTERED("ROOT.active.state_4.idle");
                    pushNullTransition();
                    state_4_subState = idle;
                    state_4_active = idle;
                    state_4_timeout = scheduleTimeout(600, "ROOT.active.state_4.idle");
                    NOTIFY_TRANSITION_TERMINATED("6");
                    res = eventConsumed;
                }
        }
    else if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            //## transition 8 
            if(doorOpen==0 && mode!=3 && stop==0)
                {
                    //## transition 1 
                    if(haveRequests())
                        {
                            if(TRUE)
                                {
                                    NOTIFY_TRANSITION_STARTED("8");
                                    NOTIFY_TRANSITION_STARTED("1");
                                    NOTIFY_TRANSITION_STARTED("5");
                                    popNullTransition();
                                    cancel(state_4_timeout);
                                    NOTIFY_STATE_EXITED("ROOT.active.state_4.idle");
                                    NOTIFY_STATE_ENTERED("ROOT.active.state_4.running");
                                    pushNullTransition();
                                    state_4_subState = running;
                                    state_4_active = running;
                                    state_4_timeout = scheduleTimeout(1500, "ROOT.active.state_4.running");
                                    NOTIFY_TRANSITION_TERMINATED("5");
                                    NOTIFY_TRANSITION_TERMINATED("1");
                                    NOTIFY_TRANSITION_TERMINATED("8");
                                    res = eventConsumed;
                                }
                        }
                }
        }
    else if(IS_EVENT_TYPE_OF(evOpen_Default_id))
        {
            NOTIFY_TRANSITION_STARTED("9");
            popNullTransition();
            cancel(state_4_timeout);
            NOTIFY_STATE_EXITED("ROOT.active.state_4.idle");
            //#[ transition 9 
            doorOpen=1;
            //#]
            NOTIFY_STATE_ENTERED("ROOT.active.state_4.door_open");
            state_4_subState = door_open;
            state_4_active = door_open;
            state_4_timeout = scheduleTimeout(4000, "ROOT.active.state_4.door_open");
            NOTIFY_TRANSITION_TERMINATED("9");
            res = eventConsumed;
        }
    
    
    return res;
}

IOxfReactive::TakeEventStatus Elevator::door_open_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
        {
            if(getCurrentEvent() == state_4_timeout)
                {
                    NOTIFY_TRANSITION_STARTED("31");
                    cancel(state_4_timeout);
                    NOTIFY_STATE_EXITED("ROOT.active.state_4.door_open");
                    NOTIFY_STATE_ENTERED("ROOT.active.state_4.over_load");
                    pushNullTransition();
                    state_4_subState = over_load;
                    state_4_active = over_load;
                    NOTIFY_TRANSITION_TERMINATED("31");
                    res = eventConsumed;
                }
        }
    else if(IS_EVENT_TYPE_OF(evLoad_Default_id))
        {
            NOTIFY_TRANSITION_STARTED("36");
            cancel(state_4_timeout);
            NOTIFY_STATE_EXITED("ROOT.active.state_4.door_open");
            //#[ transition 36 
            load();
            //#]
            NOTIFY_STATE_ENTERED("ROOT.active.state_4.door_open");
            state_4_subState = door_open;
            state_4_active = door_open;
            state_4_timeout = scheduleTimeout(4000, "ROOT.active.state_4.door_open");
            NOTIFY_TRANSITION_TERMINATED("36");
            res = eventConsumed;
        }
    else if(IS_EVENT_TYPE_OF(evClose_Default_id))
        {
            NOTIFY_TRANSITION_STARTED("32");
            cancel(state_4_timeout);
            NOTIFY_STATE_EXITED("ROOT.active.state_4.door_open");
            NOTIFY_STATE_ENTERED("ROOT.active.state_4.over_load");
            pushNullTransition();
            state_4_subState = over_load;
            state_4_active = over_load;
            NOTIFY_TRANSITION_TERMINATED("32");
            res = eventConsumed;
        }
    else if(IS_EVENT_TYPE_OF(evOpen_Default_id))
        {
            NOTIFY_TRANSITION_STARTED("10");
            cancel(state_4_timeout);
            NOTIFY_STATE_EXITED("ROOT.active.state_4.door_open");
            NOTIFY_STATE_ENTERED("ROOT.active.state_4.door_open");
            state_4_subState = door_open;
            state_4_active = door_open;
            state_4_timeout = scheduleTimeout(4000, "ROOT.active.state_4.door_open");
            NOTIFY_TRANSITION_TERMINATED("10");
            res = eventConsumed;
        }
    else if(IS_EVENT_TYPE_OF(evUnLoad_Default_id))
        {
            NOTIFY_TRANSITION_STARTED("37");
            cancel(state_4_timeout);
            NOTIFY_STATE_EXITED("ROOT.active.state_4.door_open");
            //#[ transition 37 
            unLoad();
            //#]
            NOTIFY_STATE_ENTERED("ROOT.active.state_4.door_open");
            state_4_subState = door_open;
            state_4_active = door_open;
            state_4_timeout = scheduleTimeout(4000, "ROOT.active.state_4.door_open");
            NOTIFY_TRANSITION_TERMINATED("37");
            res = eventConsumed;
        }
    
    
    return res;
}

void Elevator::state_16_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.active.state_16");
    NOTIFY_TRANSITION_STARTED("28");
    NOTIFY_STATE_ENTERED("ROOT.active.state_16.non_stop");
    state_16_subState = non_stop;
    state_16_active = non_stop;
    //#[ state active.state_16.non_stop.(Entry) 
    stop = 0;
    //#]
    NOTIFY_TRANSITION_TERMINATED("28");
}

IOxfReactive::TakeEventStatus Elevator::state_16_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_16_active) {
        // State stopped
        case stopped:
        {
            if(IS_EVENT_TYPE_OF(evStop_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("30");
                    NOTIFY_STATE_EXITED("ROOT.active.state_16.stopped");
                    NOTIFY_STATE_ENTERED("ROOT.active.state_16.non_stop");
                    state_16_subState = non_stop;
                    state_16_active = non_stop;
                    //#[ state active.state_16.non_stop.(Entry) 
                    stop = 0;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("30");
                    res = eventConsumed;
                }
            
            
        }
        break;
        // State non_stop
        case non_stop:
        {
            if(IS_EVENT_TYPE_OF(evStop_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("29");
                    NOTIFY_STATE_EXITED("ROOT.active.state_16.non_stop");
                    NOTIFY_STATE_ENTERED("ROOT.active.state_16.stopped");
                    state_16_subState = stopped;
                    state_16_active = stopped;
                    //#[ state active.state_16.stopped.(Entry) 
                    stop = 1;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("29");
                    res = eventConsumed;
                }
            
            
        }
        break;
        default:
            break;
    }
    return res;
}

void Elevator::state_12_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.active.state_12");
    NOTIFY_TRANSITION_STARTED("21");
    NOTIFY_STATE_ENTERED("ROOT.active.state_12.regular");
    state_12_subState = regular;
    state_12_active = regular;
    //#[ state active.state_12.regular.(Entry) 
    mode = 1;
    //#]
    NOTIFY_TRANSITION_TERMINATED("21");
}

IOxfReactive::TakeEventStatus Elevator::state_12_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_12_active) {
        // State regular
        case regular:
        {
            if(IS_EVENT_TYPE_OF(evFreight_Default_id))
                {
                    //## transition 22 
                    if(!IS_IN(running))
                        {
                            NOTIFY_TRANSITION_STARTED("22");
                            NOTIFY_STATE_EXITED("ROOT.active.state_12.regular");
                            NOTIFY_STATE_ENTERED("ROOT.active.state_12.freight");
                            state_12_subState = freight;
                            state_12_active = freight;
                            //#[ state active.state_12.freight.(Entry) 
                            mode = 2;
                            //#]
                            NOTIFY_TRANSITION_TERMINATED("22");
                            res = eventConsumed;
                        }
                }
            else if(IS_EVENT_TYPE_OF(evMaintenance_Default_id))
                {
                    //## transition 27 
                    if(!IS_IN(running))
                        {
                            NOTIFY_TRANSITION_STARTED("27");
                            NOTIFY_STATE_EXITED("ROOT.active.state_12.regular");
                            NOTIFY_STATE_ENTERED("ROOT.active.state_12.maintenance");
                            state_12_subState = maintenance;
                            state_12_active = maintenance;
                            //#[ state active.state_12.maintenance.(Entry) 
                            mode = 3;
                            //#]
                            NOTIFY_TRANSITION_TERMINATED("27");
                            res = eventConsumed;
                        }
                }
            
            
        }
        break;
        // State freight
        case freight:
        {
            if(IS_EVENT_TYPE_OF(evRegular_Default_id))
                {
                    //## transition 23 
                    if(!IS_IN(running))
                        {
                            NOTIFY_TRANSITION_STARTED("23");
                            NOTIFY_STATE_EXITED("ROOT.active.state_12.freight");
                            NOTIFY_STATE_ENTERED("ROOT.active.state_12.regular");
                            state_12_subState = regular;
                            state_12_active = regular;
                            //#[ state active.state_12.regular.(Entry) 
                            mode = 1;
                            //#]
                            NOTIFY_TRANSITION_TERMINATED("23");
                            res = eventConsumed;
                        }
                }
            else if(IS_EVENT_TYPE_OF(evMaintenance_Default_id))
                {
                    //## transition 24 
                    if(!IS_IN(running))
                        {
                            NOTIFY_TRANSITION_STARTED("24");
                            NOTIFY_STATE_EXITED("ROOT.active.state_12.freight");
                            NOTIFY_STATE_ENTERED("ROOT.active.state_12.maintenance");
                            state_12_subState = maintenance;
                            state_12_active = maintenance;
                            //#[ state active.state_12.maintenance.(Entry) 
                            mode = 3;
                            //#]
                            NOTIFY_TRANSITION_TERMINATED("24");
                            res = eventConsumed;
                        }
                }
            
            
        }
        break;
        // State maintenance
        case maintenance:
        {
            if(IS_EVENT_TYPE_OF(evFreight_Default_id))
                {
                    //## transition 25 
                    if(!IS_IN(running))
                        {
                            NOTIFY_TRANSITION_STARTED("25");
                            NOTIFY_STATE_EXITED("ROOT.active.state_12.maintenance");
                            NOTIFY_STATE_ENTERED("ROOT.active.state_12.freight");
                            state_12_subState = freight;
                            state_12_active = freight;
                            //#[ state active.state_12.freight.(Entry) 
                            mode = 2;
                            //#]
                            NOTIFY_TRANSITION_TERMINATED("25");
                            res = eventConsumed;
                        }
                }
            else if(IS_EVENT_TYPE_OF(evRegular_Default_id))
                {
                    //## transition 26 
                    if(!IS_IN(running))
                        {
                            NOTIFY_TRANSITION_STARTED("26");
                            NOTIFY_STATE_EXITED("ROOT.active.state_12.maintenance");
                            NOTIFY_STATE_ENTERED("ROOT.active.state_12.regular");
                            state_12_subState = regular;
                            state_12_active = regular;
                            //#[ state active.state_12.regular.(Entry) 
                            mode = 1;
                            //#]
                            NOTIFY_TRANSITION_TERMINATED("26");
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

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedElevator::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("currentLevel", x2String(myReal->currentLevel));
    aomsAttributes->addAttribute("direction", x2String(myReal->direction));
    aomsAttributes->addAttribute("doorOpen", x2String(myReal->doorOpen));
    aomsAttributes->addAttribute("upRequests", array2String(6, myReal->upRequests, sizeof(int), &x2String));
    aomsAttributes->addAttribute("downRequests", array2String(6, myReal->downRequests, sizeof(int), &x2String));
    aomsAttributes->addAttribute("mode", x2String(myReal->mode));
    aomsAttributes->addAttribute("stop", x2String(myReal->stop));
    aomsAttributes->addAttribute("overLoaded", x2String(myReal->overLoaded));
    aomsAttributes->addAttribute("currLoad", x2String(myReal->currLoad));
    aomsAttributes->addAttribute("MAX_LOAD", x2String(myReal->MAX_LOAD));
    aomsAttributes->addAttribute("displayLevel", x2String(myReal->displayLevel));
}

void OMAnimatedElevator::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsLevel", true, false);
    {
        int iter = 0;
        while (iter < 6){
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
    if(myReal->rootState_subState == Elevator::active)
        {
            active_serializeStates(aomsState);
        }
}

void OMAnimatedElevator::active_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active");
    state_4_serializeStates(aomsState);
    state_5_serializeStates(aomsState);
    state_8_serializeStates(aomsState);
    state_12_serializeStates(aomsState);
    state_16_serializeStates(aomsState);
}

void OMAnimatedElevator::state_8_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_8");
    switch (myReal->state_8_subState) {
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
    aomsState->addState("ROOT.active.state_8.up");
}

void OMAnimatedElevator::off_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_8.off");
}

void OMAnimatedElevator::down_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_8.down");
}

void OMAnimatedElevator::state_5_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_5");
    switch (myReal->state_5_subState) {
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
    aomsState->addState("ROOT.active.state_5.deactivated");
}

void OMAnimatedElevator::activated_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_5.activated");
}

void OMAnimatedElevator::state_4_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_4");
    switch (myReal->state_4_subState) {
        case Elevator::idle:
        {
            idle_serializeStates(aomsState);
        }
        break;
        case Elevator::running:
        {
            running_serializeStates(aomsState);
        }
        break;
        case Elevator::door_open:
        {
            door_open_serializeStates(aomsState);
        }
        break;
        case Elevator::over_load:
        {
            over_load_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedElevator::running_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_4.running");
}

void OMAnimatedElevator::over_load_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_4.over_load");
}

void OMAnimatedElevator::idle_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_4.idle");
}

void OMAnimatedElevator::door_open_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_4.door_open");
}

void OMAnimatedElevator::state_16_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_16");
    switch (myReal->state_16_subState) {
        case Elevator::stopped:
        {
            stopped_serializeStates(aomsState);
        }
        break;
        case Elevator::non_stop:
        {
            non_stop_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedElevator::stopped_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_16.stopped");
}

void OMAnimatedElevator::non_stop_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_16.non_stop");
}

void OMAnimatedElevator::state_12_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_12");
    switch (myReal->state_12_subState) {
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
    aomsState->addState("ROOT.active.state_12.regular");
}

void OMAnimatedElevator::maintenance_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_12.maintenance");
}

void OMAnimatedElevator::freight_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.active.state_12.freight");
}
//#]

IMPLEMENT_REACTIVE_META_P(Elevator, Default, Default, false, OMAnimatedElevator)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: DefaultComponent\DefaultConfig\Elevator.cpp
*********************************************************************/
