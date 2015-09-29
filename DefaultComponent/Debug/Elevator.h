/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: Debug
	Model Element	: Elevator
//!	Generated Date	: Tue, 29, Sep 2015  
	File Path	: DefaultComponent\Debug\Elevator.h
*********************************************************************/

#ifndef Elevator_H
#define Elevator_H

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
//## classInstance itsLevel
#include "LevelButton.h"
//## link system
class SystemController;

//## package Default

//## class Elevator
class Elevator : public OMReactive {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedElevator;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## operation Elevator()
    Elevator(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~Elevator();
    
    ////    Operations    ////
    
    //## operation getCurrentLevel()
    int getCurrentLevel();
    
    //## operation getDirection()
    int getDirection();
    
    //## operation getDownRequests(int)
    int getDownRequests(int level);
    
    //## operation getMode()
    int getMode();
    
    //## operation getUpRequests(int)
    int getUpRequests(int level);
    
    //## operation haveDownRequests()
    bool haveDownRequests();
    
    //## operation haveRequests()
    bool haveRequests();
    
    //## operation haveUpRequests()
    bool haveUpRequests();
    
    //## operation load()
    void load();
    
    //## operation move()
    void move();
    
    //## operation needStop()
    bool needStop();
    
    //## operation setDownRequests(int,int)
    void setDownRequests(int level, int i);
    
    //## operation setUpRequests(int,int)
    void setUpRequests(int level, int i);
    
    //## operation unLoad()
    void unLoad();
    
    ////    Additional operations    ////
    
    //## auto_generated
    int getMAX_LOAD() const;
    
    //## auto_generated
    void setMAX_LOAD(int p_MAX_LOAD);
    
    //## auto_generated
    int getCurrLoad() const;
    
    //## auto_generated
    void setCurrLoad(int p_currLoad);
    
    //## auto_generated
    void setCurrentLevel(int p_currentLevel);
    
    //## auto_generated
    void setDirection(int p_direction);
    
    //## auto_generated
    int getDoorOpen() const;
    
    //## auto_generated
    void setDoorOpen(int p_doorOpen);
    
    //## auto_generated
    int getDownRequests(int i1) const;
    
    //## auto_generated
    void setMode(int p_mode);
    
    //## auto_generated
    int getOverLoaded() const;
    
    //## auto_generated
    void setOverLoaded(int p_overLoaded);
    
    //## auto_generated
    int getStop() const;
    
    //## auto_generated
    void setStop(int p_stop);
    
    //## auto_generated
    int getUpRequests(int i1) const;
    
    //## auto_generated
    int getItsLevel() const;
    
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
    
    //## auto_generated
    void cancelTimeouts();
    
    //## auto_generated
    bool cancelTimeout(const IOxfTimeout* arg);
    
    ////    Attributes    ////
    
    int MAX_LOAD;		//## attribute MAX_LOAD
    
    int currLoad;		//## attribute currLoad
    
    int currentLevel;		//## attribute currentLevel
    
    int direction;		//## attribute direction
    
    int doorOpen;		//## attribute doorOpen
    
    int downRequests[5];		//## attribute downRequests
    
    int mode;		//## attribute mode
    
    int overLoaded;		//## attribute overLoaded
    
    int stop;		//## attribute stop
    
    int upRequests[5];		//## attribute upRequests
    
    ////    Relations and components    ////
    
    LevelButton itsLevel[5];		//## classInstance itsLevel
    
    SystemController* system;		//## link system
    
    ////    Framework operations    ////

public :

    //## auto_generated
    void __setSystem(SystemController* p_SystemController);
    
    //## auto_generated
    void _setSystem(SystemController* p_SystemController);
    
    //## auto_generated
    void _clearSystem();
    
    //## auto_generated
    void setActiveContext(IOxfActive* theActiveContext, bool activeInstance);
    
    //## auto_generated
    virtual void destroy();
    
    // rootState:
    //## statechart_method
    inline bool rootState_IN() const;
    
    //## statechart_method
    virtual void rootState_entDef();
    
    //## statechart_method
    void rootStateEntDef();
    
    //## statechart_method
    virtual IOxfReactive::TakeEventStatus rootState_processEvent();
    
    // Active:
    //## statechart_method
    inline bool Active_IN() const;
    
    //## statechart_method
    void Active_entDef();
    
    //## statechart_method
    void Active_exit();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Active_processEvent();
    
    // state_5:
    //## statechart_method
    inline bool state_5_IN() const;
    
    //## statechart_method
    void state_5_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_5_processEvent();
    
    // stopped:
    //## statechart_method
    inline bool stopped_IN() const;
    
    // non_stop:
    //## statechart_method
    inline bool non_stop_IN() const;
    
    // state_4:
    //## statechart_method
    inline bool state_4_IN() const;
    
    //## statechart_method
    void state_4_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_4_processEvent();
    
    // regular:
    //## statechart_method
    inline bool regular_IN() const;
    
    // maintenance:
    //## statechart_method
    inline bool maintenance_IN() const;
    
    // freight:
    //## statechart_method
    inline bool freight_IN() const;
    
    // state_3:
    //## statechart_method
    inline bool state_3_IN() const;
    
    //## statechart_method
    void state_3_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_3_processEvent();
    
    // up:
    //## statechart_method
    inline bool up_IN() const;
    
    // off:
    //## statechart_method
    inline bool off_IN() const;
    
    // down:
    //## statechart_method
    inline bool down_IN() const;
    
    // state_2:
    //## statechart_method
    inline bool state_2_IN() const;
    
    //## statechart_method
    void state_2_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_2_processEvent();
    
    // deactivated:
    //## statechart_method
    inline bool deactivated_IN() const;
    
    // activated:
    //## statechart_method
    inline bool activated_IN() const;
    
    // state_1:
    //## statechart_method
    inline bool state_1_IN() const;
    
    //## statechart_method
    void state_1_entDef();
    
    //## statechart_method
    void state_1_exit();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_1_processEvent();
    
    // running:
    //## statechart_method
    inline bool running_IN() const;
    
    // overLoad:
    //## statechart_method
    inline bool overLoad_IN() const;
    
    // idle:
    //## statechart_method
    inline bool idle_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus idle_handleEvent();
    
    // door_open:
    //## statechart_method
    inline bool door_open_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus door_open_handleEvent();
    
    ////    Framework    ////

protected :

//#[ ignore
    enum Elevator_Enum {
        OMNonState = 0,
        Active = 1,
        state_5 = 2,
        stopped = 3,
        non_stop = 4,
        state_4 = 5,
        regular = 6,
        maintenance = 7,
        freight = 8,
        state_3 = 9,
        up = 10,
        off = 11,
        down = 12,
        state_2 = 13,
        deactivated = 14,
        activated = 15,
        state_1 = 16,
        running = 17,
        overLoad = 18,
        idle = 19,
        door_open = 20
    };
    
    int rootState_subState;
    
    int rootState_active;
    
    int state_5_subState;
    
    int state_5_active;
    
    int state_4_subState;
    
    int state_4_active;
    
    int state_3_subState;
    
    int state_3_active;
    
    int state_2_subState;
    
    int state_2_active;
    
    int state_1_subState;
    
    int state_1_active;
    
    IOxfTimeout* state_1_timeout;
//#]
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedElevator : virtual public AOMInstance {
    DECLARE_REACTIVE_META(Elevator, OMAnimatedElevator)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
    
    virtual void serializeRelations(AOMSRelations* aomsRelations) const;
    
    //## statechart_method
    void rootState_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Active_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_5_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void stopped_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void non_stop_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_4_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void regular_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void maintenance_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void freight_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_3_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void up_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void off_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void down_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_2_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void deactivated_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void activated_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_1_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void running_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void overLoad_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void idle_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void door_open_serializeStates(AOMSState* aomsState) const;
};
//#]
#endif // _OMINSTRUMENT

inline bool Elevator::rootState_IN() const {
    return true;
}

inline bool Elevator::Active_IN() const {
    return rootState_subState == Active;
}

inline bool Elevator::state_5_IN() const {
    return Active_IN();
}

inline bool Elevator::stopped_IN() const {
    return state_5_subState == stopped;
}

inline bool Elevator::non_stop_IN() const {
    return state_5_subState == non_stop;
}

inline bool Elevator::state_4_IN() const {
    return Active_IN();
}

inline bool Elevator::regular_IN() const {
    return state_4_subState == regular;
}

inline bool Elevator::maintenance_IN() const {
    return state_4_subState == maintenance;
}

inline bool Elevator::freight_IN() const {
    return state_4_subState == freight;
}

inline bool Elevator::state_3_IN() const {
    return Active_IN();
}

inline bool Elevator::up_IN() const {
    return state_3_subState == up;
}

inline bool Elevator::off_IN() const {
    return state_3_subState == off;
}

inline bool Elevator::down_IN() const {
    return state_3_subState == down;
}

inline bool Elevator::state_2_IN() const {
    return Active_IN();
}

inline bool Elevator::deactivated_IN() const {
    return state_2_subState == deactivated;
}

inline bool Elevator::activated_IN() const {
    return state_2_subState == activated;
}

inline bool Elevator::state_1_IN() const {
    return Active_IN();
}

inline bool Elevator::running_IN() const {
    return state_1_subState == running;
}

inline bool Elevator::overLoad_IN() const {
    return state_1_subState == overLoad;
}

inline bool Elevator::idle_IN() const {
    return state_1_subState == idle;
}

inline bool Elevator::door_open_IN() const {
    return state_1_subState == door_open;
}

#endif
/*********************************************************************
	File Path	: DefaultComponent\Debug\Elevator.h
*********************************************************************/
