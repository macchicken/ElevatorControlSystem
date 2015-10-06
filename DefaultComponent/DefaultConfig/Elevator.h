/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: DefaultConfig
	Model Element	: Elevator
//!	Generated Date	: Tue, 6, Oct 2015  
	File Path	: DefaultComponent\DefaultConfig\Elevator.h
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
    
    //## operation move()
    void move();
    
    //## operation needStop()
    bool needStop();
    
    //## operation setDownRequests(int,int)
    void setDownRequests(int level, int i);
    
    //## operation setUpRequests(int,int)
    void setUpRequests(int level, int i);
    
    ////    Additional operations    ////
    
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
    
    int currentLevel;		//## attribute currentLevel
    
    int direction;		//## attribute direction
    
    int doorOpen;		//## attribute doorOpen
    
    int downRequests[6];		//## attribute downRequests
    
    int mode;		//## attribute mode
    
    int stop;		//## attribute stop
    
    int upRequests[6];		//## attribute upRequests
    
    ////    Relations and components    ////
    
    SystemController* system;		//## link system
    
    LevelButton itsLevel[6];		//## classInstance itsLevel
    
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
    
    ////    Framework    ////
    
    //## operation load()
    void load();
    
    //## operation unLoad()
    void unLoad();
    
    //## auto_generated
    int getMAX_LOAD() const;
    
    //## auto_generated
    void setMAX_LOAD(int p_MAX_LOAD);
    
    //## auto_generated
    int getCurrLoad() const;
    
    //## auto_generated
    void setCurrLoad(int p_currLoad);
    
    //## auto_generated
    int getDisplayLevel() const;
    
    //## auto_generated
    void setDisplayLevel(int p_displayLevel);
    
    //## auto_generated
    int getOverLoaded() const;
    
    //## auto_generated
    void setOverLoaded(int p_overLoaded);

protected :

    int MAX_LOAD;		//## attribute MAX_LOAD
    
    int currLoad;		//## attribute currLoad
    
    int displayLevel;		//## attribute displayLevel
    
    int overLoaded;		//## attribute overLoaded

public :

    // rootState:
    //## statechart_method
    inline bool rootState_IN() const;
    
    //## statechart_method
    virtual void rootState_entDef();
    
    //## statechart_method
    void rootStateEntDef();
    
    //## statechart_method
    virtual IOxfReactive::TakeEventStatus rootState_processEvent();
    
    // active:
    //## statechart_method
    inline bool active_IN() const;
    
    //## statechart_method
    void active_entDef();
    
    //## statechart_method
    void active_exit();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus active_processEvent();
    
    // state_8:
    //## statechart_method
    inline bool state_8_IN() const;
    
    //## statechart_method
    void state_8_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_8_processEvent();
    
    // up:
    //## statechart_method
    inline bool up_IN() const;
    
    // off:
    //## statechart_method
    inline bool off_IN() const;
    
    // down:
    //## statechart_method
    inline bool down_IN() const;
    
    // state_5:
    //## statechart_method
    inline bool state_5_IN() const;
    
    //## statechart_method
    void state_5_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_5_processEvent();
    
    // deactivated:
    //## statechart_method
    inline bool deactivated_IN() const;
    
    // activated:
    //## statechart_method
    inline bool activated_IN() const;
    
    // state_4:
    //## statechart_method
    inline bool state_4_IN() const;
    
    //## statechart_method
    void state_4_entDef();
    
    //## statechart_method
    void state_4_exit();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_4_processEvent();
    
    // running:
    //## statechart_method
    inline bool running_IN() const;
    
    // over_load:
    //## statechart_method
    inline bool over_load_IN() const;
    
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
    
    // state_16:
    //## statechart_method
    inline bool state_16_IN() const;
    
    //## statechart_method
    void state_16_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_16_processEvent();
    
    // stopped:
    //## statechart_method
    inline bool stopped_IN() const;
    
    // non_stop:
    //## statechart_method
    inline bool non_stop_IN() const;
    
    // state_12:
    //## statechart_method
    inline bool state_12_IN() const;
    
    //## statechart_method
    void state_12_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_12_processEvent();
    
    // regular:
    //## statechart_method
    inline bool regular_IN() const;
    
    // maintenance:
    //## statechart_method
    inline bool maintenance_IN() const;
    
    // freight:
    //## statechart_method
    inline bool freight_IN() const;

protected :

//#[ ignore
    enum Elevator_Enum {
        OMNonState = 0,
        active = 1,
        state_8 = 2,
        up = 3,
        off = 4,
        down = 5,
        state_5 = 6,
        deactivated = 7,
        activated = 8,
        state_4 = 9,
        running = 10,
        over_load = 11,
        idle = 12,
        door_open = 13,
        state_16 = 14,
        stopped = 15,
        non_stop = 16,
        state_12 = 17,
        regular = 18,
        maintenance = 19,
        freight = 20
    };
    
    int rootState_subState;
    
    int rootState_active;
    
    int state_8_subState;
    
    int state_8_active;
    
    int state_5_subState;
    
    int state_5_active;
    
    int state_4_subState;
    
    int state_4_active;
    
    IOxfTimeout* state_4_timeout;
    
    int state_16_subState;
    
    int state_16_active;
    
    int state_12_subState;
    
    int state_12_active;
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
    void active_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_8_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void up_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void off_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void down_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_5_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void deactivated_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void activated_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_4_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void running_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void over_load_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void idle_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void door_open_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_16_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void stopped_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void non_stop_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_12_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void regular_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void maintenance_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void freight_serializeStates(AOMSState* aomsState) const;
};
//#]
#endif // _OMINSTRUMENT

inline bool Elevator::rootState_IN() const {
    return true;
}

inline bool Elevator::active_IN() const {
    return rootState_subState == active;
}

inline bool Elevator::state_8_IN() const {
    return active_IN();
}

inline bool Elevator::up_IN() const {
    return state_8_subState == up;
}

inline bool Elevator::off_IN() const {
    return state_8_subState == off;
}

inline bool Elevator::down_IN() const {
    return state_8_subState == down;
}

inline bool Elevator::state_5_IN() const {
    return active_IN();
}

inline bool Elevator::deactivated_IN() const {
    return state_5_subState == deactivated;
}

inline bool Elevator::activated_IN() const {
    return state_5_subState == activated;
}

inline bool Elevator::state_4_IN() const {
    return active_IN();
}

inline bool Elevator::running_IN() const {
    return state_4_subState == running;
}

inline bool Elevator::over_load_IN() const {
    return state_4_subState == over_load;
}

inline bool Elevator::idle_IN() const {
    return state_4_subState == idle;
}

inline bool Elevator::door_open_IN() const {
    return state_4_subState == door_open;
}

inline bool Elevator::state_16_IN() const {
    return active_IN();
}

inline bool Elevator::stopped_IN() const {
    return state_16_subState == stopped;
}

inline bool Elevator::non_stop_IN() const {
    return state_16_subState == non_stop;
}

inline bool Elevator::state_12_IN() const {
    return active_IN();
}

inline bool Elevator::regular_IN() const {
    return state_12_subState == regular;
}

inline bool Elevator::maintenance_IN() const {
    return state_12_subState == maintenance;
}

inline bool Elevator::freight_IN() const {
    return state_12_subState == freight;
}

#endif
/*********************************************************************
	File Path	: DefaultComponent\DefaultConfig\Elevator.h
*********************************************************************/
