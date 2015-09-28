/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: Debug
	Model Element	: SystemController
//!	Generated Date	: Mon, 28, Sep 2015  
	File Path	: DefaultComponent\Debug\SystemController.h
*********************************************************************/

#ifndef SystemController_H
#define SystemController_H

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
//## classInstance itsElevator
#include "Elevator.h"
//## classInstance itsFloor
#include "Floor.h"
//## package Default

//## class SystemController
class SystemController : public OMReactive {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedSystemController;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## operation SystemController()
    SystemController(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~SystemController();
    
    ////    Operations    ////
    
    //## operation handleDownRequests(int)
    void handleDownRequests(int level);
    
    //## operation handleUpRequests(int)
    void handleUpRequests(int level);
    
    //## operation notifyState(int,int)
    void notifyState(int direction, int level);
    
    ////    Additional operations    ////
    
    //## auto_generated
    int getItsElevator() const;
    
    //## auto_generated
    int getItsFloor() const;
    
    //## auto_generated
    virtual bool startBehavior();

protected :

    //## auto_generated
    void initRelations();
    
    ////    Relations and components    ////
    
    Elevator itsElevator[2];		//## classInstance itsElevator
    
    Floor itsFloor[5];		//## classInstance itsFloor
    
    ////    Framework operations    ////

public :

    //## auto_generated
    void setActiveContext(IOxfActive* theActiveContext, bool activeInstance);
    
    //## auto_generated
    virtual void destroy();
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedSystemController : virtual public AOMInstance {
    DECLARE_META(SystemController, OMAnimatedSystemController)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeRelations(AOMSRelations* aomsRelations) const;
};
//#]
#endif // _OMINSTRUMENT

#endif
/*********************************************************************
	File Path	: DefaultComponent\Debug\SystemController.h
*********************************************************************/