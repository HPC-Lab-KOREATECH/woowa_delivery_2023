
"use strict";

let Lamps = require('./Lamps.js');
let ObjectStatusListExtended = require('./ObjectStatusListExtended.js');
let PREvent = require('./PREvent.js');
let SensorPosControl = require('./SensorPosControl.js');
let SkateboardCtrlCmd = require('./SkateboardCtrlCmd.js');
let SyncModeCmdResponse = require('./SyncModeCmdResponse.js');
let ObjectStatusList = require('./ObjectStatusList.js');
let EgoVehicleStatusExtended = require('./EgoVehicleStatusExtended.js');
let ScenarioLoad = require('./ScenarioLoad.js');
let SetTrafficLight = require('./SetTrafficLight.js');
let EventInfo = require('./EventInfo.js');
let DillyCmdResponse = require('./DillyCmdResponse.js');
let EgoVehicleStatus = require('./EgoVehicleStatus.js');
let WoowaDillyStatus = require('./WoowaDillyStatus.js');
let MoraiTLInfo = require('./MoraiTLInfo.js');
let RadarDetection = require('./RadarDetection.js');
let NpcGhostCmd = require('./NpcGhostCmd.js');
let MapSpec = require('./MapSpec.js');
let DillyCmd = require('./DillyCmd.js');
let SyncModeAddObject = require('./SyncModeAddObject.js');
let CollisionData = require('./CollisionData.js');
let ERP42Info = require('./ERP42Info.js');
let GPSMessage = require('./GPSMessage.js');
let VehicleSpecIndex = require('./VehicleSpecIndex.js');
let MoraiSimProcHandle = require('./MoraiSimProcHandle.js');
let SkateboardStatus = require('./SkateboardStatus.js');
let PRStatus = require('./PRStatus.js');
let VehicleSpec = require('./VehicleSpec.js');
let CtrlCmd = require('./CtrlCmd.js');
let SyncModeSetGear = require('./SyncModeSetGear.js');
let MoraiSimProcStatus = require('./MoraiSimProcStatus.js');
let SyncModeCtrlCmd = require('./SyncModeCtrlCmd.js');
let VehicleCollision = require('./VehicleCollision.js');
let MoraiTLIndex = require('./MoraiTLIndex.js');
let SkidSteer6wUGVCtrlCmd = require('./SkidSteer6wUGVCtrlCmd.js');
let ReplayInfo = require('./ReplayInfo.js');
let SaveSensorData = require('./SaveSensorData.js');
let SyncModeCmd = require('./SyncModeCmd.js');
let IntersectionStatus = require('./IntersectionStatus.js');
let WaitForTickResponse = require('./WaitForTickResponse.js');
let SkidSteer6wUGVStatus = require('./SkidSteer6wUGVStatus.js');
let SyncModeResultResponse = require('./SyncModeResultResponse.js');
let TrafficLight = require('./TrafficLight.js');
let PRCtrlCmd = require('./PRCtrlCmd.js');
let MultiPlayEventRequest = require('./MultiPlayEventRequest.js');
let SyncModeRemoveObject = require('./SyncModeRemoveObject.js');
let VehicleCollisionData = require('./VehicleCollisionData.js');
let MultiPlayEventResponse = require('./MultiPlayEventResponse.js');
let MapSpecIndex = require('./MapSpecIndex.js');
let WaitForTick = require('./WaitForTick.js');
let GhostMessage = require('./GhostMessage.js');
let NpcGhostInfo = require('./NpcGhostInfo.js');
let IntersectionControl = require('./IntersectionControl.js');
let GetTrafficLightStatus = require('./GetTrafficLightStatus.js');
let ObjectStatus = require('./ObjectStatus.js');
let ObjectStatusExtended = require('./ObjectStatusExtended.js');
let DdCtrlCmd = require('./DdCtrlCmd.js');
let SyncModeInfo = require('./SyncModeInfo.js');
let MoraiSrvResponse = require('./MoraiSrvResponse.js');
let EgoDdVehicleStatus = require('./EgoDdVehicleStatus.js');
let RadarDetections = require('./RadarDetections.js');
let IntscnTL = require('./IntscnTL.js');
let MultiEgoSetting = require('./MultiEgoSetting.js');
let SyncModeScenarioLoad = require('./SyncModeScenarioLoad.js');

module.exports = {
  Lamps: Lamps,
  ObjectStatusListExtended: ObjectStatusListExtended,
  PREvent: PREvent,
  SensorPosControl: SensorPosControl,
  SkateboardCtrlCmd: SkateboardCtrlCmd,
  SyncModeCmdResponse: SyncModeCmdResponse,
  ObjectStatusList: ObjectStatusList,
  EgoVehicleStatusExtended: EgoVehicleStatusExtended,
  ScenarioLoad: ScenarioLoad,
  SetTrafficLight: SetTrafficLight,
  EventInfo: EventInfo,
  DillyCmdResponse: DillyCmdResponse,
  EgoVehicleStatus: EgoVehicleStatus,
  WoowaDillyStatus: WoowaDillyStatus,
  MoraiTLInfo: MoraiTLInfo,
  RadarDetection: RadarDetection,
  NpcGhostCmd: NpcGhostCmd,
  MapSpec: MapSpec,
  DillyCmd: DillyCmd,
  SyncModeAddObject: SyncModeAddObject,
  CollisionData: CollisionData,
  ERP42Info: ERP42Info,
  GPSMessage: GPSMessage,
  VehicleSpecIndex: VehicleSpecIndex,
  MoraiSimProcHandle: MoraiSimProcHandle,
  SkateboardStatus: SkateboardStatus,
  PRStatus: PRStatus,
  VehicleSpec: VehicleSpec,
  CtrlCmd: CtrlCmd,
  SyncModeSetGear: SyncModeSetGear,
  MoraiSimProcStatus: MoraiSimProcStatus,
  SyncModeCtrlCmd: SyncModeCtrlCmd,
  VehicleCollision: VehicleCollision,
  MoraiTLIndex: MoraiTLIndex,
  SkidSteer6wUGVCtrlCmd: SkidSteer6wUGVCtrlCmd,
  ReplayInfo: ReplayInfo,
  SaveSensorData: SaveSensorData,
  SyncModeCmd: SyncModeCmd,
  IntersectionStatus: IntersectionStatus,
  WaitForTickResponse: WaitForTickResponse,
  SkidSteer6wUGVStatus: SkidSteer6wUGVStatus,
  SyncModeResultResponse: SyncModeResultResponse,
  TrafficLight: TrafficLight,
  PRCtrlCmd: PRCtrlCmd,
  MultiPlayEventRequest: MultiPlayEventRequest,
  SyncModeRemoveObject: SyncModeRemoveObject,
  VehicleCollisionData: VehicleCollisionData,
  MultiPlayEventResponse: MultiPlayEventResponse,
  MapSpecIndex: MapSpecIndex,
  WaitForTick: WaitForTick,
  GhostMessage: GhostMessage,
  NpcGhostInfo: NpcGhostInfo,
  IntersectionControl: IntersectionControl,
  GetTrafficLightStatus: GetTrafficLightStatus,
  ObjectStatus: ObjectStatus,
  ObjectStatusExtended: ObjectStatusExtended,
  DdCtrlCmd: DdCtrlCmd,
  SyncModeInfo: SyncModeInfo,
  MoraiSrvResponse: MoraiSrvResponse,
  EgoDdVehicleStatus: EgoDdVehicleStatus,
  RadarDetections: RadarDetections,
  IntscnTL: IntscnTL,
  MultiEgoSetting: MultiEgoSetting,
  SyncModeScenarioLoad: SyncModeScenarioLoad,
};
