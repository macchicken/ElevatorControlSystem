/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: DefaultConfig
	Model Element	: Default
//!	Generated Date	: Thu, 1, Oct 2015  
	File Path	: DefaultComponent\DefaultConfig\Default.h
*********************************************************************/

#ifndef Default_H
#define Default_H

//## auto_generated
#include <oxf\oxf.h>
//## auto_generated
#include <aom\aom.h>
//## auto_generated
#include <oxf\event.h>
//## auto_generated
class Elevator;

//## auto_generated
class Floor;

//## auto_generated
class LevelButton;

//## auto_generated
class SystemController;

//#[ ignore
#define evUpButton_Default_id 18601

#define evDownButton_Default_id 18602

#define evClose_Default_id 18603

#define evOpen_Default_id 18604

#define evAlarm_Default_id 18605

#define evLevelOn_Default_id 18606

#define evLevelButton_Default_id 18607

#define evLevelButtonOff_Default_id 18608

#define evLevelButtonOn_Default_id 18609

#define evFreight_Default_id 18610

#define evRegular_Default_id 18611

#define evMaintenance_Default_id 18612

#define evStop_Default_id 18613

#define evLoad_Default_id 18614

#define evUnLoad_Default_id 18615
//#]

//## package Default



//## event evUpButton()
class evUpButton : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevUpButton;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evUpButton();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevUpButton : virtual public AOMEvent {
    DECLARE_META_EVENT(evUpButton)
};
//#]
#endif // _OMINSTRUMENT

//## event evDownButton()
class evDownButton : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevDownButton;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evDownButton();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevDownButton : virtual public AOMEvent {
    DECLARE_META_EVENT(evDownButton)
};
//#]
#endif // _OMINSTRUMENT

//## event evClose()
class evClose : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevClose;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evClose();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevClose : virtual public AOMEvent {
    DECLARE_META_EVENT(evClose)
};
//#]
#endif // _OMINSTRUMENT

//## event evOpen()
class evOpen : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevOpen;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evOpen();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevOpen : virtual public AOMEvent {
    DECLARE_META_EVENT(evOpen)
};
//#]
#endif // _OMINSTRUMENT

//## event evAlarm()
class evAlarm : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevAlarm;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evAlarm();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevAlarm : virtual public AOMEvent {
    DECLARE_META_EVENT(evAlarm)
};
//#]
#endif // _OMINSTRUMENT

//## event evLevelOn()
class evLevelOn : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevLevelOn;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evLevelOn();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevLevelOn : virtual public AOMEvent {
    DECLARE_META_EVENT(evLevelOn)
};
//#]
#endif // _OMINSTRUMENT

//## event evLevelButton()
class evLevelButton : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevLevelButton;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evLevelButton();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevLevelButton : virtual public AOMEvent {
    DECLARE_META_EVENT(evLevelButton)
};
//#]
#endif // _OMINSTRUMENT

//## event evLevelButtonOff()
class evLevelButtonOff : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevLevelButtonOff;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evLevelButtonOff();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevLevelButtonOff : virtual public AOMEvent {
    DECLARE_META_EVENT(evLevelButtonOff)
};
//#]
#endif // _OMINSTRUMENT

//## event evLevelButtonOn()
class evLevelButtonOn : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevLevelButtonOn;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evLevelButtonOn();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevLevelButtonOn : virtual public AOMEvent {
    DECLARE_META_EVENT(evLevelButtonOn)
};
//#]
#endif // _OMINSTRUMENT

//## event evFreight()
class evFreight : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevFreight;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evFreight();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevFreight : virtual public AOMEvent {
    DECLARE_META_EVENT(evFreight)
};
//#]
#endif // _OMINSTRUMENT

//## event evRegular()
class evRegular : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevRegular;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evRegular();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevRegular : virtual public AOMEvent {
    DECLARE_META_EVENT(evRegular)
};
//#]
#endif // _OMINSTRUMENT

//## event evMaintenance()
class evMaintenance : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevMaintenance;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evMaintenance();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevMaintenance : virtual public AOMEvent {
    DECLARE_META_EVENT(evMaintenance)
};
//#]
#endif // _OMINSTRUMENT

//## event evStop()
class evStop : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevStop;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evStop();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevStop : virtual public AOMEvent {
    DECLARE_META_EVENT(evStop)
};
//#]
#endif // _OMINSTRUMENT

//## event evLoad()
class evLoad : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevLoad;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evLoad();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevLoad : virtual public AOMEvent {
    DECLARE_META_EVENT(evLoad)
};
//#]
#endif // _OMINSTRUMENT

//## event evUnLoad()
class evUnLoad : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevUnLoad;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evUnLoad();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevUnLoad : virtual public AOMEvent {
    DECLARE_META_EVENT(evUnLoad)
};
//#]
#endif // _OMINSTRUMENT

#endif
/*********************************************************************
	File Path	: DefaultComponent\DefaultConfig\Default.h
*********************************************************************/
