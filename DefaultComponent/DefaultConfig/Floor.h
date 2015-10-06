/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: DefaultConfig
	Model Element	: Floor
//!	Generated Date	: Tue, 6, Oct 2015  
	File Path	: DefaultComponent\DefaultConfig\Floor.h
*********************************************************************/

#ifndef Floor_H
#define Floor_H

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
//## link system
class SystemController;

//## package Default

//## class Floor
class Floor : public OMReactive {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedFloor;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## operation Floor()
    Floor(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~Floor();
    
    ////    Operations    ////
    
    //## operation isButtonPressed()
    bool isButtonPressed();
    
    //## operation isDown()
    bool isDown();
    
    //## operation isUp()
    bool isUp();
    
    //## operation setDown(int)
    void setDown(int n);
    
    //## operation setLevel(int)
    void setLevel(int n);
    
    //## operation setOff()
    void setOff();
    
    //## operation setUp(int)
    void setUp(int n);
    
    ////    Additional operations    ////
    
    //## auto_generated
    int getDown() const;
    
    //## auto_generated
    int getLevel() const;
    
    //## auto_generated
    int getUp() const;
    
    //## auto_generated
    SystemController* getSystem() const;
    
    //## auto_generated
    void setSystem(SystemController* p_SystemController);
    
    //## auto_generated
    virtual bool startBehavior();

protected :

    //## auto_generated
    void initStatechart();
    
    //## auto_generated
    void cleanUpRelations();
    
    ////    Attributes    ////
    
    int down;		//## attribute down
    
    int level;		//## attribute level
    
    int up;		//## attribute up
    
    ////    Relations and components    ////
    
    SystemController* system;		//## link system
    
    ////    Framework operations    ////

public :

    //## auto_generated
    void __setSystem(SystemController* p_SystemController);
    
    //## auto_generated
    void _setSystem(SystemController* p_SystemController);
    
    //## auto_generated
    void _clearSystem();
    
    ////    Framework    ////
    
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
    
    //## statechart_method
    void button_exit();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus button_processEvent();
    
    // state_7:
    //## statechart_method
    inline bool state_7_IN() const;
    
    //## statechart_method
    void state_7_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_7_processEvent();
    
    // state_7_on:
    //## statechart_method
    inline bool state_7_on_IN() const;
    
    // state_7_off:
    //## statechart_method
    inline bool state_7_off_IN() const;
    
    // state_6:
    //## statechart_method
    inline bool state_6_IN() const;
    
    //## statechart_method
    void state_6_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_6_processEvent();
    
    // on:
    //## statechart_method
    inline bool on_IN() const;
    
    // off:
    //## statechart_method
    inline bool off_IN() const;
    
    // state_11:
    //## statechart_method
    inline bool state_11_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_11_processEvent();

protected :

//#[ ignore
    enum Floor_Enum {
        OMNonState = 0,
        button = 1,
        state_7 = 2,
        state_7_on = 3,
        state_7_off = 4,
        state_6 = 5,
        on = 6,
        off = 7,
        state_11 = 8
    };
    
    int rootState_subState;
    
    int rootState_active;
    
    int state_7_subState;
    
    int state_7_active;
    
    int state_6_subState;
    
    int state_6_active;
    
    int state_11_subState;
    
    int state_11_active;
//#]
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedFloor : virtual public AOMInstance {
    DECLARE_REACTIVE_META(Floor, OMAnimatedFloor)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
    
    virtual void serializeRelations(AOMSRelations* aomsRelations) const;
    
    //## statechart_method
    void rootState_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void button_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_7_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_7_on_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_7_off_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_6_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void on_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void off_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_11_serializeStates(AOMSState* aomsState) const;
};
//#]
#endif // _OMINSTRUMENT

inline bool Floor::rootState_IN() const {
    return true;
}

inline bool Floor::button_IN() const {
    return rootState_subState == button;
}

inline bool Floor::state_7_IN() const {
    return button_IN();
}

inline bool Floor::state_7_on_IN() const {
    return state_7_subState == state_7_on;
}

inline bool Floor::state_7_off_IN() const {
    return state_7_subState == state_7_off;
}

inline bool Floor::state_6_IN() const {
    return button_IN();
}

inline bool Floor::on_IN() const {
    return state_6_subState == on;
}

inline bool Floor::off_IN() const {
    return state_6_subState == off;
}

inline bool Floor::state_11_IN() const {
    return button_IN();
}

#endif
/*********************************************************************
	File Path	: DefaultComponent\DefaultConfig\Floor.h
*********************************************************************/
