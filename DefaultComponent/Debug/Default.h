/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: Debug
	Model Element	: Default
//!	Generated Date	: Tue, 29, Sep 2015  
	File Path	: DefaultComponent\Debug\Default.h
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
#define evAlarm_Default_id 18601

#define evClose_Default_id 18602

#define evFreight_Default_id 18603

#define evMaintenance_Default_id 18604

#define evOpen_Default_id 18605

#define evRegular_Default_id 18606

#define evStop_Default_id 18607

#define evDownButton_Default_id 18608

#define evLevelOn_Default_id 18609

#define evUpButton_Default_id 18610

#define evLevelButtonOn_Default_id 18611

#define evLoad_Default_id 18612

#define evUnload_Default_id 18613
//#]

//## package Default



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

//## event evUnload()
class evUnload : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevUnload;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evUnload();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevUnload : virtual public AOMEvent {
    DECLARE_META_EVENT(evUnload)
};
//#]
#endif // _OMINSTRUMENT

#endif
/*********************************************************************
	File Path	: DefaultComponent\Debug\Default.h
*********************************************************************/
