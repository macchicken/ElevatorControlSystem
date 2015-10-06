/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: DefaultConfig
	Model Element	: Floor
//!	Generated Date	: Tue, 6, Oct 2015  
	File Path	: DefaultComponent\DefaultConfig\Floor.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "Floor.h"
//## link system
#include "SystemController.h"
//## auto_generated
#include <iostream>
//#[ ignore
#define Default_Floor_Floor_SERIALIZE OM_NO_OP

#define Default_Floor_isButtonPressed_SERIALIZE OM_NO_OP

#define Default_Floor_isDown_SERIALIZE OM_NO_OP

#define Default_Floor_isUp_SERIALIZE OM_NO_OP

#define Default_Floor_setDown_SERIALIZE aomsmethod->addAttribute("n", x2String(n));

#define Default_Floor_setLevel_SERIALIZE aomsmethod->addAttribute("n", x2String(n));

#define Default_Floor_setOff_SERIALIZE OM_NO_OP

#define Default_Floor_setUp_SERIALIZE aomsmethod->addAttribute("n", x2String(n));
//#]

//## package Default

//## class Floor

using namespace std;

Floor::Floor(IOxfActive* theActiveContext) : down(0), level(0), up(0) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Floor, Floor(), 0, Default_Floor_Floor_SERIALIZE);
    setActiveContext(theActiveContext, false);
    system = NULL;
    initStatechart();
    //#[ operation Floor()
    //#]
}

Floor::~Floor() {
    NOTIFY_DESTRUCTOR(~Floor, true);
    cleanUpRelations();
}

bool Floor::isButtonPressed() {
    NOTIFY_OPERATION(isButtonPressed, isButtonPressed(), 0, Default_Floor_isButtonPressed_SERIALIZE);
    //#[ operation isButtonPressed()
    if (level == 1)
    	return true;
    else
    	return false;
    //#]
}

bool Floor::isDown() {
    NOTIFY_OPERATION(isDown, isDown(), 0, Default_Floor_isDown_SERIALIZE);
    //#[ operation isDown()
    return down == 1;
    //#]
}

bool Floor::isUp() {
    NOTIFY_OPERATION(isUp, isUp(), 0, Default_Floor_isUp_SERIALIZE);
    //#[ operation isUp()
    return up == 1;
    //#]
}

void Floor::setDown(int n) {
    NOTIFY_OPERATION(setDown, setDown(int), 1, Default_Floor_setDown_SERIALIZE);
    //#[ operation setDown(int)
    down = n;
    //#]
    NOTIFY_SET_OPERATION;
}

void Floor::setLevel(int n) {
    NOTIFY_OPERATION(setLevel, setLevel(int), 1, Default_Floor_setLevel_SERIALIZE);
    //#[ operation setLevel(int)
    level = n;
    //#]
    NOTIFY_SET_OPERATION;
}

void Floor::setOff() {
    NOTIFY_OPERATION(setOff, setOff(), 0, Default_Floor_setOff_SERIALIZE);
    //#[ operation setOff()
    level = 0;
    //#]
}

void Floor::setUp(int n) {
    NOTIFY_OPERATION(setUp, setUp(int), 1, Default_Floor_setUp_SERIALIZE);
    //#[ operation setUp(int)
    up = n;
    //#]
    NOTIFY_SET_OPERATION;
}

int Floor::getDown() const {
    return down;
}

int Floor::getLevel() const {
    return level;
}

int Floor::getUp() const {
    return up;
}

SystemController* Floor::getSystem() const {
    return system;
}

void Floor::setSystem(SystemController* p_SystemController) {
    _setSystem(p_SystemController);
}

bool Floor::startBehavior() {
    bool done = false;
    done = OMReactive::startBehavior();
    return done;
}

void Floor::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
    state_7_subState = OMNonState;
    state_7_active = OMNonState;
    state_6_subState = OMNonState;
    state_6_active = OMNonState;
    state_11_subState = OMNonState;
    state_11_active = OMNonState;
}

void Floor::cleanUpRelations() {
    if(system != NULL)
        {
            NOTIFY_RELATION_CLEARED("system");
            system = NULL;
        }
}

void Floor::__setSystem(SystemController* p_SystemController) {
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

void Floor::_setSystem(SystemController* p_SystemController) {
    __setSystem(p_SystemController);
}

void Floor::_clearSystem() {
    NOTIFY_RELATION_CLEARED("system");
    system = NULL;
}

void Floor::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        button_entDef();
    }
}

IOxfReactive::TakeEventStatus Floor::rootState_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State button
    if(rootState_active == button)
        {
            res = button_processEvent();
        }
    return res;
}

void Floor::button_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.button");
    rootState_subState = button;
    rootState_active = button;
    state_6_entDef();
    state_7_entDef();
    NOTIFY_STATE_ENTERED("ROOT.button.state_11");
}

void Floor::button_exit() {
    switch (state_6_subState) {
        // State off
        case off:
        {
            NOTIFY_STATE_EXITED("ROOT.button.state_6.off");
        }
        break;
        // State on
        case on:
        {
            popNullTransition();
            NOTIFY_STATE_EXITED("ROOT.button.state_6.on");
        }
        break;
        default:
            break;
    }
    state_6_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.button.state_6");
    switch (state_7_subState) {
        // State off
        case state_7_off:
        {
            NOTIFY_STATE_EXITED("ROOT.button.state_7.off");
        }
        break;
        // State on
        case state_7_on:
        {
            popNullTransition();
            NOTIFY_STATE_EXITED("ROOT.button.state_7.on");
        }
        break;
        default:
            break;
    }
    state_7_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.button.state_7");
    state_11_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.button.state_11");
    
    NOTIFY_STATE_EXITED("ROOT.button");
}

IOxfReactive::TakeEventStatus Floor::button_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State state_6
    if(state_6_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(button))
                {
                    return res;
                }
        }
    // State state_7
    if(state_7_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(button))
                {
                    return res;
                }
        }
    
    return res;
}

void Floor::state_7_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.button.state_7");
    NOTIFY_TRANSITION_STARTED("1");
    NOTIFY_STATE_ENTERED("ROOT.button.state_7.off");
    state_7_subState = state_7_off;
    state_7_active = state_7_off;
    NOTIFY_TRANSITION_TERMINATED("1");
}

IOxfReactive::TakeEventStatus Floor::state_7_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_7_active) {
        // State off
        case state_7_off:
        {
            if(IS_EVENT_TYPE_OF(evDownButton_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("3");
                    NOTIFY_STATE_EXITED("ROOT.button.state_7.off");
                    //#[ transition 3 
                    down=1;
                    system->handleDownRequests(level);
                    //#]
                    NOTIFY_STATE_ENTERED("ROOT.button.state_7.on");
                    pushNullTransition();
                    state_7_subState = state_7_on;
                    state_7_active = state_7_on;
                    NOTIFY_TRANSITION_TERMINATED("3");
                    res = eventConsumed;
                }
            
            
        }
        break;
        // State on
        case state_7_on:
        {
            if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 5 
                    if(down==0)
                        {
                            NOTIFY_TRANSITION_STARTED("5");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.button.state_7.on");
                            NOTIFY_STATE_ENTERED("ROOT.button.state_7.off");
                            state_7_subState = state_7_off;
                            state_7_active = state_7_off;
                            NOTIFY_TRANSITION_TERMINATED("5");
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

void Floor::state_6_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.button.state_6");
    NOTIFY_TRANSITION_STARTED("0");
    NOTIFY_STATE_ENTERED("ROOT.button.state_6.off");
    state_6_subState = off;
    state_6_active = off;
    NOTIFY_TRANSITION_TERMINATED("0");
}

IOxfReactive::TakeEventStatus Floor::state_6_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_6_active) {
        // State off
        case off:
        {
            if(IS_EVENT_TYPE_OF(evUpButton_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("2");
                    NOTIFY_STATE_EXITED("ROOT.button.state_6.off");
                    //#[ transition 2 
                    up=1;
                    system->handleUpRequests(level);
                    //#]
                    NOTIFY_STATE_ENTERED("ROOT.button.state_6.on");
                    pushNullTransition();
                    state_6_subState = on;
                    state_6_active = on;
                    NOTIFY_TRANSITION_TERMINATED("2");
                    res = eventConsumed;
                }
            
            
        }
        break;
        // State on
        case on:
        {
            if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 4 
                    if(up==0)
                        {
                            NOTIFY_TRANSITION_STARTED("4");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.button.state_6.on");
                            NOTIFY_STATE_ENTERED("ROOT.button.state_6.off");
                            state_6_subState = off;
                            state_6_active = off;
                            NOTIFY_TRANSITION_TERMINATED("4");
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

IOxfReactive::TakeEventStatus Floor::state_11_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    return res;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedFloor::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("up", x2String(myReal->up));
    aomsAttributes->addAttribute("down", x2String(myReal->down));
    aomsAttributes->addAttribute("level", x2String(myReal->level));
}

void OMAnimatedFloor::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("system", false, true);
    if(myReal->system)
        {
            aomsRelations->ADD_ITEM(myReal->system);
        }
}

void OMAnimatedFloor::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    if(myReal->rootState_subState == Floor::button)
        {
            button_serializeStates(aomsState);
        }
}

void OMAnimatedFloor::button_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.button");
    state_6_serializeStates(aomsState);
    state_7_serializeStates(aomsState);
    state_11_serializeStates(aomsState);
}

void OMAnimatedFloor::state_7_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.button.state_7");
    switch (myReal->state_7_subState) {
        case Floor::state_7_off:
        {
            state_7_off_serializeStates(aomsState);
        }
        break;
        case Floor::state_7_on:
        {
            state_7_on_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedFloor::state_7_on_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.button.state_7.on");
}

void OMAnimatedFloor::state_7_off_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.button.state_7.off");
}

void OMAnimatedFloor::state_6_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.button.state_6");
    switch (myReal->state_6_subState) {
        case Floor::off:
        {
            off_serializeStates(aomsState);
        }
        break;
        case Floor::on:
        {
            on_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedFloor::on_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.button.state_6.on");
}

void OMAnimatedFloor::off_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.button.state_6.off");
}

void OMAnimatedFloor::state_11_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.button.state_11");
}
//#]

IMPLEMENT_REACTIVE_META_P(Floor, Default, Default, false, OMAnimatedFloor)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: DefaultComponent\DefaultConfig\Floor.cpp
*********************************************************************/
