/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: Debug
	Model Element	: Default
//!	Generated Date	: Mon, 28, Sep 2015  
	File Path	: DefaultComponent\Debug\Default.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX
//#]

//## auto_generated
#include "Default.h"
//## auto_generated
#include "Elevator.h"
//## auto_generated
#include "Floor.h"
//## auto_generated
#include "LevelButton.h"
//## auto_generated
#include "SystemController.h"
//#[ ignore
#define evAlarm_SERIALIZE OM_NO_OP

#define evAlarm_UNSERIALIZE OM_NO_OP

#define evAlarm_CONSTRUCTOR evAlarm()

#define evClose_SERIALIZE OM_NO_OP

#define evClose_UNSERIALIZE OM_NO_OP

#define evClose_CONSTRUCTOR evClose()

#define evFreight_SERIALIZE OM_NO_OP

#define evFreight_UNSERIALIZE OM_NO_OP

#define evFreight_CONSTRUCTOR evFreight()

#define evMaintenance_SERIALIZE OM_NO_OP

#define evMaintenance_UNSERIALIZE OM_NO_OP

#define evMaintenance_CONSTRUCTOR evMaintenance()

#define evOpen_SERIALIZE OM_NO_OP

#define evOpen_UNSERIALIZE OM_NO_OP

#define evOpen_CONSTRUCTOR evOpen()

#define evRegular_SERIALIZE OM_NO_OP

#define evRegular_UNSERIALIZE OM_NO_OP

#define evRegular_CONSTRUCTOR evRegular()

#define evStop_SERIALIZE OM_NO_OP

#define evStop_UNSERIALIZE OM_NO_OP

#define evStop_CONSTRUCTOR evStop()

#define evDownButton_SERIALIZE OM_NO_OP

#define evDownButton_UNSERIALIZE OM_NO_OP

#define evDownButton_CONSTRUCTOR evDownButton()

#define evLevelOn_SERIALIZE OM_NO_OP

#define evLevelOn_UNSERIALIZE OM_NO_OP

#define evLevelOn_CONSTRUCTOR evLevelOn()

#define evUpButton_SERIALIZE OM_NO_OP

#define evUpButton_UNSERIALIZE OM_NO_OP

#define evUpButton_CONSTRUCTOR evUpButton()

#define evLevelButtonOn_SERIALIZE OM_NO_OP

#define evLevelButtonOn_UNSERIALIZE OM_NO_OP

#define evLevelButtonOn_CONSTRUCTOR evLevelButtonOn()
//#]

//## package Default


#ifdef _OMINSTRUMENT
static void serializeGlobalVars(AOMSAttributes* /* aomsAttributes */);

IMPLEMENT_META_PACKAGE(Default, Default)

static void serializeGlobalVars(AOMSAttributes* /* aomsAttributes */) {
}
#endif // _OMINSTRUMENT

//## event evAlarm()
evAlarm::evAlarm() {
    NOTIFY_EVENT_CONSTRUCTOR(evAlarm)
    setId(evAlarm_Default_id);
}

bool evAlarm::isTypeOf(const short id) const {
    return (evAlarm_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evAlarm, Default, Default, evAlarm())

//## event evClose()
evClose::evClose() {
    NOTIFY_EVENT_CONSTRUCTOR(evClose)
    setId(evClose_Default_id);
}

bool evClose::isTypeOf(const short id) const {
    return (evClose_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evClose, Default, Default, evClose())

//## event evFreight()
evFreight::evFreight() {
    NOTIFY_EVENT_CONSTRUCTOR(evFreight)
    setId(evFreight_Default_id);
}

bool evFreight::isTypeOf(const short id) const {
    return (evFreight_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evFreight, Default, Default, evFreight())

//## event evMaintenance()
evMaintenance::evMaintenance() {
    NOTIFY_EVENT_CONSTRUCTOR(evMaintenance)
    setId(evMaintenance_Default_id);
}

bool evMaintenance::isTypeOf(const short id) const {
    return (evMaintenance_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evMaintenance, Default, Default, evMaintenance())

//## event evOpen()
evOpen::evOpen() {
    NOTIFY_EVENT_CONSTRUCTOR(evOpen)
    setId(evOpen_Default_id);
}

bool evOpen::isTypeOf(const short id) const {
    return (evOpen_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evOpen, Default, Default, evOpen())

//## event evRegular()
evRegular::evRegular() {
    NOTIFY_EVENT_CONSTRUCTOR(evRegular)
    setId(evRegular_Default_id);
}

bool evRegular::isTypeOf(const short id) const {
    return (evRegular_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evRegular, Default, Default, evRegular())

//## event evStop()
evStop::evStop() {
    NOTIFY_EVENT_CONSTRUCTOR(evStop)
    setId(evStop_Default_id);
}

bool evStop::isTypeOf(const short id) const {
    return (evStop_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evStop, Default, Default, evStop())

//## event evDownButton()
evDownButton::evDownButton() {
    NOTIFY_EVENT_CONSTRUCTOR(evDownButton)
    setId(evDownButton_Default_id);
}

bool evDownButton::isTypeOf(const short id) const {
    return (evDownButton_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evDownButton, Default, Default, evDownButton())

//## event evLevelOn()
evLevelOn::evLevelOn() {
    NOTIFY_EVENT_CONSTRUCTOR(evLevelOn)
    setId(evLevelOn_Default_id);
}

bool evLevelOn::isTypeOf(const short id) const {
    return (evLevelOn_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evLevelOn, Default, Default, evLevelOn())

//## event evUpButton()
evUpButton::evUpButton() {
    NOTIFY_EVENT_CONSTRUCTOR(evUpButton)
    setId(evUpButton_Default_id);
}

bool evUpButton::isTypeOf(const short id) const {
    return (evUpButton_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evUpButton, Default, Default, evUpButton())

//## event evLevelButtonOn()
evLevelButtonOn::evLevelButtonOn() {
    NOTIFY_EVENT_CONSTRUCTOR(evLevelButtonOn)
    setId(evLevelButtonOn_Default_id);
}

bool evLevelButtonOn::isTypeOf(const short id) const {
    return (evLevelButtonOn_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evLevelButtonOn, Default, Default, evLevelButtonOn())

/*********************************************************************
	File Path	: DefaultComponent\Debug\Default.cpp
*********************************************************************/
