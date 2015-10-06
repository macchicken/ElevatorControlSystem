/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Barry
	Component	: DefaultComponent 
	Configuration 	: DefaultConfig
	Model Element	: Default
//!	Generated Date	: Tue, 6, Oct 2015  
	File Path	: DefaultComponent\DefaultConfig\Default.cpp
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
//## auto_generated
#include <iostream>
//#[ ignore
#define evUpButton_SERIALIZE OM_NO_OP

#define evUpButton_UNSERIALIZE OM_NO_OP

#define evUpButton_CONSTRUCTOR evUpButton()

#define evDownButton_SERIALIZE OM_NO_OP

#define evDownButton_UNSERIALIZE OM_NO_OP

#define evDownButton_CONSTRUCTOR evDownButton()

#define evClose_SERIALIZE OM_NO_OP

#define evClose_UNSERIALIZE OM_NO_OP

#define evClose_CONSTRUCTOR evClose()

#define evOpen_SERIALIZE OM_NO_OP

#define evOpen_UNSERIALIZE OM_NO_OP

#define evOpen_CONSTRUCTOR evOpen()

#define evAlarm_SERIALIZE OM_NO_OP

#define evAlarm_UNSERIALIZE OM_NO_OP

#define evAlarm_CONSTRUCTOR evAlarm()

#define evLevelOn_SERIALIZE OM_NO_OP

#define evLevelOn_UNSERIALIZE OM_NO_OP

#define evLevelOn_CONSTRUCTOR evLevelOn()

#define evLevelButton_SERIALIZE OM_NO_OP

#define evLevelButton_UNSERIALIZE OM_NO_OP

#define evLevelButton_CONSTRUCTOR evLevelButton()

#define evLevelButtonOff_SERIALIZE OM_NO_OP

#define evLevelButtonOff_UNSERIALIZE OM_NO_OP

#define evLevelButtonOff_CONSTRUCTOR evLevelButtonOff()

#define evLevelButtonOn_SERIALIZE OM_NO_OP

#define evLevelButtonOn_UNSERIALIZE OM_NO_OP

#define evLevelButtonOn_CONSTRUCTOR evLevelButtonOn()

#define evFreight_SERIALIZE OM_NO_OP

#define evFreight_UNSERIALIZE OM_NO_OP

#define evFreight_CONSTRUCTOR evFreight()

#define evRegular_SERIALIZE OM_NO_OP

#define evRegular_UNSERIALIZE OM_NO_OP

#define evRegular_CONSTRUCTOR evRegular()

#define evMaintenance_SERIALIZE OM_NO_OP

#define evMaintenance_UNSERIALIZE OM_NO_OP

#define evMaintenance_CONSTRUCTOR evMaintenance()

#define evStop_SERIALIZE OM_NO_OP

#define evStop_UNSERIALIZE OM_NO_OP

#define evStop_CONSTRUCTOR evStop()

#define evLoad_SERIALIZE OM_NO_OP

#define evLoad_UNSERIALIZE OM_NO_OP

#define evLoad_CONSTRUCTOR evLoad()

#define evUnLoad_SERIALIZE OM_NO_OP

#define evUnLoad_UNSERIALIZE OM_NO_OP

#define evUnLoad_CONSTRUCTOR evUnLoad()
//#]

//## package Default



using namespace std;

#ifdef _OMINSTRUMENT
static void serializeGlobalVars(AOMSAttributes* /* aomsAttributes */);

IMPLEMENT_META_PACKAGE(Default, Default)

static void serializeGlobalVars(AOMSAttributes* /* aomsAttributes */) {
}
#endif // _OMINSTRUMENT

//## event evUpButton()
evUpButton::evUpButton() {
    NOTIFY_EVENT_CONSTRUCTOR(evUpButton)
    setId(evUpButton_Default_id);
}

bool evUpButton::isTypeOf(const short id) const {
    return (evUpButton_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evUpButton, Default, Default, evUpButton())

//## event evDownButton()
evDownButton::evDownButton() {
    NOTIFY_EVENT_CONSTRUCTOR(evDownButton)
    setId(evDownButton_Default_id);
}

bool evDownButton::isTypeOf(const short id) const {
    return (evDownButton_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evDownButton, Default, Default, evDownButton())

//## event evClose()
evClose::evClose() {
    NOTIFY_EVENT_CONSTRUCTOR(evClose)
    setId(evClose_Default_id);
}

bool evClose::isTypeOf(const short id) const {
    return (evClose_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evClose, Default, Default, evClose())

//## event evOpen()
evOpen::evOpen() {
    NOTIFY_EVENT_CONSTRUCTOR(evOpen)
    setId(evOpen_Default_id);
}

bool evOpen::isTypeOf(const short id) const {
    return (evOpen_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evOpen, Default, Default, evOpen())

//## event evAlarm()
evAlarm::evAlarm() {
    NOTIFY_EVENT_CONSTRUCTOR(evAlarm)
    setId(evAlarm_Default_id);
}

bool evAlarm::isTypeOf(const short id) const {
    return (evAlarm_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evAlarm, Default, Default, evAlarm())

//## event evLevelOn()
evLevelOn::evLevelOn() {
    NOTIFY_EVENT_CONSTRUCTOR(evLevelOn)
    setId(evLevelOn_Default_id);
}

bool evLevelOn::isTypeOf(const short id) const {
    return (evLevelOn_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evLevelOn, Default, Default, evLevelOn())

//## event evLevelButton()
evLevelButton::evLevelButton() {
    NOTIFY_EVENT_CONSTRUCTOR(evLevelButton)
    setId(evLevelButton_Default_id);
}

bool evLevelButton::isTypeOf(const short id) const {
    return (evLevelButton_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evLevelButton, Default, Default, evLevelButton())

//## event evLevelButtonOff()
evLevelButtonOff::evLevelButtonOff() {
    NOTIFY_EVENT_CONSTRUCTOR(evLevelButtonOff)
    setId(evLevelButtonOff_Default_id);
}

bool evLevelButtonOff::isTypeOf(const short id) const {
    return (evLevelButtonOff_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evLevelButtonOff, Default, Default, evLevelButtonOff())

//## event evLevelButtonOn()
evLevelButtonOn::evLevelButtonOn() {
    NOTIFY_EVENT_CONSTRUCTOR(evLevelButtonOn)
    setId(evLevelButtonOn_Default_id);
}

bool evLevelButtonOn::isTypeOf(const short id) const {
    return (evLevelButtonOn_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evLevelButtonOn, Default, Default, evLevelButtonOn())

//## event evFreight()
evFreight::evFreight() {
    NOTIFY_EVENT_CONSTRUCTOR(evFreight)
    setId(evFreight_Default_id);
}

bool evFreight::isTypeOf(const short id) const {
    return (evFreight_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evFreight, Default, Default, evFreight())

//## event evRegular()
evRegular::evRegular() {
    NOTIFY_EVENT_CONSTRUCTOR(evRegular)
    setId(evRegular_Default_id);
}

bool evRegular::isTypeOf(const short id) const {
    return (evRegular_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evRegular, Default, Default, evRegular())

//## event evMaintenance()
evMaintenance::evMaintenance() {
    NOTIFY_EVENT_CONSTRUCTOR(evMaintenance)
    setId(evMaintenance_Default_id);
}

bool evMaintenance::isTypeOf(const short id) const {
    return (evMaintenance_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evMaintenance, Default, Default, evMaintenance())

//## event evStop()
evStop::evStop() {
    NOTIFY_EVENT_CONSTRUCTOR(evStop)
    setId(evStop_Default_id);
}

bool evStop::isTypeOf(const short id) const {
    return (evStop_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evStop, Default, Default, evStop())

//## event evLoad()
evLoad::evLoad() {
    NOTIFY_EVENT_CONSTRUCTOR(evLoad)
    setId(evLoad_Default_id);
}

bool evLoad::isTypeOf(const short id) const {
    return (evLoad_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evLoad, Default, Default, evLoad())

//## event evUnLoad()
evUnLoad::evUnLoad() {
    NOTIFY_EVENT_CONSTRUCTOR(evUnLoad)
    setId(evUnLoad_Default_id);
}

bool evUnLoad::isTypeOf(const short id) const {
    return (evUnLoad_Default_id==id);
}

IMPLEMENT_META_EVENT_P(evUnLoad, Default, Default, evUnLoad())

/*********************************************************************
	File Path	: DefaultComponent\DefaultConfig\Default.cpp
*********************************************************************/
