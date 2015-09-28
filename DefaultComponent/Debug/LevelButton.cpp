/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: Debug
	Model Element	: LevelButton
//!	Generated Date	: Mon, 28, Sep 2015  
	File Path	: DefaultComponent\Debug\LevelButton.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "LevelButton.h"
//#[ ignore
#define Default_LevelButton_LevelButton_SERIALIZE OM_NO_OP

#define Default_LevelButton_isOn_SERIALIZE OM_NO_OP

#define Default_LevelButton_setOff_SERIALIZE OM_NO_OP
//#]

//## package Default

//## class LevelButton
LevelButton::LevelButton(IOxfActive* theActiveContext) {
    NOTIFY_REACTIVE_CONSTRUCTOR(LevelButton, LevelButton(), 0, Default_LevelButton_LevelButton_SERIALIZE);
    setActiveContext(theActiveContext, false);
    initStatechart();
    //#[ operation LevelButton()
    on=0;
    //#]
}

LevelButton::~LevelButton() {
    NOTIFY_DESTRUCTOR(~LevelButton, true);
}

bool LevelButton::isOn() {
    NOTIFY_OPERATION(isOn, isOn(), 0, Default_LevelButton_isOn_SERIALIZE);
    //#[ operation isOn()
    return on == 1;
    //#]
}

void LevelButton::setOff() {
    NOTIFY_OPERATION(setOff, setOff(), 0, Default_LevelButton_setOff_SERIALIZE);
    //#[ operation setOff()
    on = 0;
    //#]
}

int LevelButton::getOn() const {
    return on;
}

void LevelButton::setOn(int p_on) {
    on = p_on;
    NOTIFY_SET_OPERATION;
}

bool LevelButton::startBehavior() {
    bool done = false;
    done = OMReactive::startBehavior();
    return done;
}

void LevelButton::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
    button_subState = OMNonState;
}

void LevelButton::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        button_entDef();
    }
}

IOxfReactive::TakeEventStatus LevelButton::rootState_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (rootState_active) {
        // State off
        case off:
        {
            if(IS_EVENT_TYPE_OF(evLevelButtonOn_Default_id))
                {
                    NOTIFY_TRANSITION_STARTED("1");
                    NOTIFY_STATE_EXITED("ROOT.button.off");
                    //#[ transition 1 
                    on=1;
                    //#]
                    NOTIFY_STATE_ENTERED("ROOT.button.active");
                    pushNullTransition();
                    button_subState = active;
                    rootState_active = active;
                    NOTIFY_TRANSITION_TERMINATED("1");
                    res = eventConsumed;
                }
            
            
        }
        break;
        // State active
        case active:
        {
            if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 2 
                    if(on==0)
                        {
                            NOTIFY_TRANSITION_STARTED("2");
                            popNullTransition();
                            NOTIFY_STATE_EXITED("ROOT.button.active");
                            NOTIFY_STATE_ENTERED("ROOT.button.off");
                            button_subState = off;
                            rootState_active = off;
                            NOTIFY_TRANSITION_TERMINATED("2");
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

void LevelButton::button_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.button");
    rootState_subState = button;
    NOTIFY_TRANSITION_STARTED("0");
    NOTIFY_STATE_ENTERED("ROOT.button.off");
    button_subState = off;
    rootState_active = off;
    NOTIFY_TRANSITION_TERMINATED("0");
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedLevelButton::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("on", x2String(myReal->on));
}

void OMAnimatedLevelButton::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    if(myReal->rootState_subState == LevelButton::button)
        {
            button_serializeStates(aomsState);
        }
}

void OMAnimatedLevelButton::button_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.button");
    switch (myReal->button_subState) {
        case LevelButton::off:
        {
            off_serializeStates(aomsState);
        }
        break;
        case LevelButton::active:
        {
            active_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedLevelButton::off_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.button.off");
}

void OMAnimatedLevelButton::active_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.button.active");
}
//#]

IMPLEMENT_REACTIVE_META_P(LevelButton, Default, Default, false, OMAnimatedLevelButton)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: DefaultComponent\Debug\LevelButton.cpp
*********************************************************************/
