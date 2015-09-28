/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: Debug
	Model Element	: LevelButton
//!	Generated Date	: Mon, 28, Sep 2015  
	File Path	: DefaultComponent\Debug\LevelButton.h
*********************************************************************/

#ifndef LevelButton_H
#define LevelButton_H

//## auto_generated
#include <oxf\oxf.h>
//## auto_generated
#include <aom\aom.h>
//## auto_generated
#include "Default.h"
//## auto_generated
#include <oxf\omthread.h>
//## auto_generated
#include <oxf\omreactive.h>
//## auto_generated
#include <oxf\state.h>
//## auto_generated
#include <oxf\event.h>
//## package Default

//## class LevelButton
class LevelButton : public OMReactive {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedLevelButton;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## operation LevelButton()
    LevelButton(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~LevelButton();
    
    ////    Operations    ////
    
    //## operation isOn()
    bool isOn();
    
    //## operation setOff()
    void setOff();
    
    ////    Additional operations    ////
    
    //## auto_generated
    int getOn() const;
    
    //## auto_generated
    void setOn(int p_on);
    
    //## auto_generated
    virtual bool startBehavior();

protected :

    //## auto_generated
    void initStatechart();
    
    ////    Attributes    ////
    
    int on;		//## attribute on
    
    ////    Framework operations    ////

public :

    // rootState:
    //## statechart_method
    inline bool rootState_IN() const;
    
    //## statechart_method
    virtual void rootState_entDef();
    
    //## statechart_method
    virtual IOxfReactive::TakeEventStatus rootState_processEvent();
    
    // button:
    //## statechart_method
    inline bool button_IN() const;
    
    //## statechart_method
    void button_entDef();
    
    // off:
    //## statechart_method
    inline bool off_IN() const;
    
    // active:
    //## statechart_method
    inline bool active_IN() const;
    
    ////    Framework    ////

protected :

//#[ ignore
    enum LevelButton_Enum {
        OMNonState = 0,
        button = 1,
        off = 2,
        active = 3
    };
    
    int rootState_subState;
    
    int rootState_active;
    
    int button_subState;
//#]
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedLevelButton : virtual public AOMInstance {
    DECLARE_REACTIVE_META(LevelButton, OMAnimatedLevelButton)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
    
    //## statechart_method
    void rootState_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void button_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void off_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void active_serializeStates(AOMSState* aomsState) const;
};
//#]
#endif // _OMINSTRUMENT

inline bool LevelButton::rootState_IN() const {
    return true;
}

inline bool LevelButton::button_IN() const {
    return rootState_subState == button;
}

inline bool LevelButton::off_IN() const {
    return button_subState == off;
}

inline bool LevelButton::active_IN() const {
    return button_subState == active;
}

#endif
/*********************************************************************
	File Path	: DefaultComponent\Debug\LevelButton.h
*********************************************************************/
