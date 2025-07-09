/************************** 
 * New Branding Test *
 **************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'new branding test';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcome_screenRoutineBegin());
flowScheduler.add(welcome_screenRoutineEachFrame());
flowScheduler.add(welcome_screenRoutineEnd());
flowScheduler.add(instructionRoutineBegin());
flowScheduler.add(instructionRoutineEachFrame());
flowScheduler.add(instructionRoutineEnd());
const study_brandsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(study_brandsLoopBegin(study_brandsLoopScheduler));
flowScheduler.add(study_brandsLoopScheduler);
flowScheduler.add(study_brandsLoopEnd);



flowScheduler.add(break_phaseRoutineBegin());
flowScheduler.add(break_phaseRoutineEachFrame());
flowScheduler.add(break_phaseRoutineEnd());
const test_brandsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(test_brandsLoopBegin(test_brandsLoopScheduler));
flowScheduler.add(test_brandsLoopScheduler);
flowScheduler.add(test_brandsLoopEnd);


flowScheduler.add(end_screenRoutineBegin());
flowScheduler.add(end_screenRoutineEachFrame());
flowScheduler.add(end_screenRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'studyphase.xlsx', 'path': 'studyphase.xlsx'},
    {'name': 'testphase.csv', 'path': 'testphase.csv'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var welcome_screenClock;
var welcome_text;
var key_welcome;
var instructionClock;
var Instruction_text;
var key_instruction;
var study_phaseClock;
var brands;
var slogan_2;
var fixctionClock;
var cross;
var break_phaseClock;
var break_text;
var key_break;
var feedbacktestClock;
var feedbackbrand;
var feedbackslogan;
var key_resp;
var end_screenClock;
var end_text;
var key_end;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome_screen"
  welcome_screenClock = new util.Clock();
  welcome_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_text',
    text: 'سلام\nروز خوش\n\nممنونم که ما را در انجام این آزمون همراهی می کنید\n با فشردن کلید\n space\nبه صفحه بعد منتقل می شوید',
    font: 'B Nazanin',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_welcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction"
  instructionClock = new util.Clock();
  Instruction_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instruction_text',
    text: ' سلام و خوش آمدید\n\nشما در حال شرکت در یک آزمون حافظه و توجه هستید\nاین آزمون شامل دو مرحله است\n\n «مرحله اول: «یادگیری برندها و شعارها\nدر این مرحله، تعدادی برند به\u200cهمراه شعار آن\u200cها روی صفحه نمایش داده می\u200cشوند  \nلطفاً با دقت به برند و شعار نمایش\u200cداده\u200cشده نگاه کنید و \nسعی کنید آن را به خاطر بسپارید\n"برخی از برندها ممکن است چند بار تکرار شوند"\n هر برند و شعار به مدت 5 ثانیه نمایش داده می\u200cشود\n\n« مرحله دوم: «تشخیص\nپس از پایان مرحله یادگیری، برندها و شعارهایی به شما نمایش داده می\u200cشوند  \nبرخی از آن\u200cها در مرحله یادگیری وجود داشتند و برخی جدید هستند  \nشما باید با فشردن یکی از دکمه\u200cهای زیر پاسخ دهید\n\n اگر فکر می\u200cکنید این برند و شعار در مرحله یادگیری وجود داشت، کلید\n y را فشار دهید  \n اگر فکر می\u200cکنید قبلاً این برند و شعار را ندیده\u200cاید، کلید\n n را فشار دهید\n\n سعی کنید با دقت و بدون عجله پاسخ دهید\n اطلاعات شما فقط برای اهداف پژوهشی استفاده خواهد شد\n\nبرای شروع آزمون کلید\n Space فشار دهید',
    font: 'B Nazanin',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_instruction = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "study_phase"
  study_phaseClock = new util.Clock();
  brands = new visual.TextStim({
    win: psychoJS.window,
    name: 'brands',
    text: '',
    font: 'B Nazanin',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('blue'),  opacity: undefined,
    depth: 0.0 
  });
  
  slogan_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'slogan_2',
    text: '',
    font: 'B Nazanin',
    units: undefined, 
    pos: [0, (- 0.1)], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('crimson'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "fixction"
  fixctionClock = new util.Clock();
  cross = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cross', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: 0, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "break_phase"
  break_phaseClock = new util.Clock();
  break_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'break_text',
    text: 'لطفا 5 دقیقه استراحت کنید\n\n\nبا فشردن کلید\n space\nبه صفحه بعد منتقل می شوید',
    font: 'B Nazanin',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_break = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedbacktest"
  feedbacktestClock = new util.Clock();
  feedbackbrand = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbackbrand',
    text: '',
    font: 'B Nazanin',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('blue'),  opacity: undefined,
    depth: 0.0 
  });
  
  feedbackslogan = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbackslogan',
    text: '',
    font: 'B Nazanin',
    units: undefined, 
    pos: [0, (- 0.1)], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('crimson'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end_screen"
  end_screenClock = new util.Clock();
  end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_text',
    text: 'سپاسگزارم بابت همراهی تون\nروز خوش\n\n\nلطفا کمی صبر کنید ما در حال ذخیره سازی\nاطلاعات آزمون شما هستیم\nسپس با فشردن کلید \nspace\nاز آزمون خارج شوید',
    font: 'B Nazanin',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_end = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var welcome_screenMaxDurationReached;
var _key_welcome_allKeys;
var welcome_screenMaxDuration;
var welcome_screenComponents;
function welcome_screenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome_screen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    welcome_screenClock.reset();
    routineTimer.reset();
    welcome_screenMaxDurationReached = false;
    // update component parameters for each repeat
    key_welcome.keys = undefined;
    key_welcome.rt = undefined;
    _key_welcome_allKeys = [];
    psychoJS.experiment.addData('welcome_screen.started', globalClock.getTime());
    welcome_screenMaxDuration = null
    // keep track of which components have finished
    welcome_screenComponents = [];
    welcome_screenComponents.push(welcome_text);
    welcome_screenComponents.push(key_welcome);
    
    for (const thisComponent of welcome_screenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function welcome_screenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome_screen' ---
    // get current time
    t = welcome_screenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_text* updates
    if (t >= 0.0 && welcome_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_text.tStart = t;  // (not accounting for frame time here)
      welcome_text.frameNStart = frameN;  // exact frame index
      
      welcome_text.setAutoDraw(true);
    }
    
    
    // *key_welcome* updates
    if (t >= 2 && key_welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_welcome.tStart = t;  // (not accounting for frame time here)
      key_welcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_welcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_welcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_welcome.clearEvents(); });
    }
    
    if (key_welcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_welcome.getKeys({keyList: ['space'], waitRelease: false});
      _key_welcome_allKeys = _key_welcome_allKeys.concat(theseKeys);
      if (_key_welcome_allKeys.length > 0) {
        key_welcome.keys = _key_welcome_allKeys[_key_welcome_allKeys.length - 1].name;  // just the last key pressed
        key_welcome.rt = _key_welcome_allKeys[_key_welcome_allKeys.length - 1].rt;
        key_welcome.duration = _key_welcome_allKeys[_key_welcome_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcome_screenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcome_screenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome_screen' ---
    for (const thisComponent of welcome_screenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('welcome_screen.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_welcome.corr, level);
    }
    psychoJS.experiment.addData('key_welcome.keys', key_welcome.keys);
    if (typeof key_welcome.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_welcome.rt', key_welcome.rt);
        psychoJS.experiment.addData('key_welcome.duration', key_welcome.duration);
        routineTimer.reset();
        }
    
    key_welcome.stop();
    // the Routine "welcome_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructionMaxDurationReached;
var _key_instruction_allKeys;
var instructionMaxDuration;
var instructionComponents;
function instructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instructionClock.reset();
    routineTimer.reset();
    instructionMaxDurationReached = false;
    // update component parameters for each repeat
    key_instruction.keys = undefined;
    key_instruction.rt = undefined;
    _key_instruction_allKeys = [];
    psychoJS.experiment.addData('instruction.started', globalClock.getTime());
    instructionMaxDuration = null
    // keep track of which components have finished
    instructionComponents = [];
    instructionComponents.push(Instruction_text);
    instructionComponents.push(key_instruction);
    
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction' ---
    // get current time
    t = instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instruction_text* updates
    if (t >= 0.0 && Instruction_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instruction_text.tStart = t;  // (not accounting for frame time here)
      Instruction_text.frameNStart = frameN;  // exact frame index
      
      Instruction_text.setAutoDraw(true);
    }
    
    
    // *key_instruction* updates
    if (t >= 2 && key_instruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_instruction.tStart = t;  // (not accounting for frame time here)
      key_instruction.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_instruction.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_instruction.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_instruction.clearEvents(); });
    }
    
    if (key_instruction.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_instruction.getKeys({keyList: ['space'], waitRelease: false});
      _key_instruction_allKeys = _key_instruction_allKeys.concat(theseKeys);
      if (_key_instruction_allKeys.length > 0) {
        key_instruction.keys = _key_instruction_allKeys[_key_instruction_allKeys.length - 1].name;  // just the last key pressed
        key_instruction.rt = _key_instruction_allKeys[_key_instruction_allKeys.length - 1].rt;
        key_instruction.duration = _key_instruction_allKeys[_key_instruction_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction' ---
    for (const thisComponent of instructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instruction.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_instruction.corr, level);
    }
    psychoJS.experiment.addData('key_instruction.keys', key_instruction.keys);
    if (typeof key_instruction.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_instruction.rt', key_instruction.rt);
        psychoJS.experiment.addData('key_instruction.duration', key_instruction.duration);
        routineTimer.reset();
        }
    
    key_instruction.stop();
    // the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var study_brands;
function study_brandsLoopBegin(study_brandsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    study_brands = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'studyphase.xlsx',
      seed: undefined, name: 'study_brands'
    });
    psychoJS.experiment.addLoop(study_brands); // add the loop to the experiment
    currentLoop = study_brands;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisStudy_brand of study_brands) {
      snapshot = study_brands.getSnapshot();
      study_brandsLoopScheduler.add(importConditions(snapshot));
      study_brandsLoopScheduler.add(study_phaseRoutineBegin(snapshot));
      study_brandsLoopScheduler.add(study_phaseRoutineEachFrame());
      study_brandsLoopScheduler.add(study_phaseRoutineEnd(snapshot));
      study_brandsLoopScheduler.add(fixctionRoutineBegin(snapshot));
      study_brandsLoopScheduler.add(fixctionRoutineEachFrame());
      study_brandsLoopScheduler.add(fixctionRoutineEnd(snapshot));
      study_brandsLoopScheduler.add(study_brandsLoopEndIteration(study_brandsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function study_brandsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(study_brands);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function study_brandsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var test_brands;
function test_brandsLoopBegin(test_brandsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    test_brands = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'testphase.csv',
      seed: undefined, name: 'test_brands'
    });
    psychoJS.experiment.addLoop(test_brands); // add the loop to the experiment
    currentLoop = test_brands;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTest_brand of test_brands) {
      snapshot = test_brands.getSnapshot();
      test_brandsLoopScheduler.add(importConditions(snapshot));
      test_brandsLoopScheduler.add(feedbacktestRoutineBegin(snapshot));
      test_brandsLoopScheduler.add(feedbacktestRoutineEachFrame());
      test_brandsLoopScheduler.add(feedbacktestRoutineEnd(snapshot));
      test_brandsLoopScheduler.add(test_brandsLoopEndIteration(test_brandsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function test_brandsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(test_brands);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function test_brandsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var study_phaseMaxDurationReached;
var study_phaseMaxDuration;
var study_phaseComponents;
function study_phaseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'study_phase' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    study_phaseClock.reset(routineTimer.getTime());
    routineTimer.add(5.000000);
    study_phaseMaxDurationReached = false;
    // update component parameters for each repeat
    brands.setText(brand);
    slogan_2.setText(slogan);
    psychoJS.experiment.addData('study_phase.started', globalClock.getTime());
    study_phaseMaxDuration = null
    // keep track of which components have finished
    study_phaseComponents = [];
    study_phaseComponents.push(brands);
    study_phaseComponents.push(slogan_2);
    
    for (const thisComponent of study_phaseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function study_phaseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'study_phase' ---
    // get current time
    t = study_phaseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *brands* updates
    if (t >= 0.0 && brands.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      brands.tStart = t;  // (not accounting for frame time here)
      brands.frameNStart = frameN;  // exact frame index
      
      brands.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (brands.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      brands.setAutoDraw(false);
    }
    
    
    // *slogan_2* updates
    if (t >= 0.0 && slogan_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slogan_2.tStart = t;  // (not accounting for frame time here)
      slogan_2.frameNStart = frameN;  // exact frame index
      
      slogan_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (slogan_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      slogan_2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of study_phaseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function study_phaseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'study_phase' ---
    for (const thisComponent of study_phaseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('study_phase.stopped', globalClock.getTime());
    if (study_phaseMaxDurationReached) {
        study_phaseClock.add(study_phaseMaxDuration);
    } else {
        study_phaseClock.add(5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fixctionMaxDurationReached;
var fixctionMaxDuration;
var fixctionComponents;
function fixctionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    fixctionClock.reset(routineTimer.getTime());
    routineTimer.add(0.400000);
    fixctionMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixction.started', globalClock.getTime());
    fixctionMaxDuration = null
    // keep track of which components have finished
    fixctionComponents = [];
    fixctionComponents.push(cross);
    
    for (const thisComponent of fixctionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fixctionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixction' ---
    // get current time
    t = fixctionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cross* updates
    if (t >= 0.0 && cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cross.tStart = t;  // (not accounting for frame time here)
      cross.frameNStart = frameN;  // exact frame index
      
      cross.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cross.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixctionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixctionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixction' ---
    for (const thisComponent of fixctionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fixction.stopped', globalClock.getTime());
    if (fixctionMaxDurationReached) {
        fixctionClock.add(fixctionMaxDuration);
    } else {
        fixctionClock.add(0.400000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var break_phaseMaxDurationReached;
var _key_break_allKeys;
var break_phaseMaxDuration;
var break_phaseComponents;
function break_phaseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'break_phase' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    break_phaseClock.reset();
    routineTimer.reset();
    break_phaseMaxDurationReached = false;
    // update component parameters for each repeat
    key_break.keys = undefined;
    key_break.rt = undefined;
    _key_break_allKeys = [];
    psychoJS.experiment.addData('break_phase.started', globalClock.getTime());
    break_phaseMaxDuration = null
    // keep track of which components have finished
    break_phaseComponents = [];
    break_phaseComponents.push(break_text);
    break_phaseComponents.push(key_break);
    
    for (const thisComponent of break_phaseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function break_phaseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'break_phase' ---
    // get current time
    t = break_phaseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *break_text* updates
    if (t >= 0.0 && break_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      break_text.tStart = t;  // (not accounting for frame time here)
      break_text.frameNStart = frameN;  // exact frame index
      
      break_text.setAutoDraw(true);
    }
    
    
    // *key_break* updates
    if (t >= 10 && key_break.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_break.tStart = t;  // (not accounting for frame time here)
      key_break.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_break.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_break.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_break.clearEvents(); });
    }
    
    if (key_break.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_break.getKeys({keyList: ['space'], waitRelease: false});
      _key_break_allKeys = _key_break_allKeys.concat(theseKeys);
      if (_key_break_allKeys.length > 0) {
        key_break.keys = _key_break_allKeys[_key_break_allKeys.length - 1].name;  // just the last key pressed
        key_break.rt = _key_break_allKeys[_key_break_allKeys.length - 1].rt;
        key_break.duration = _key_break_allKeys[_key_break_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of break_phaseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function break_phaseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'break_phase' ---
    for (const thisComponent of break_phaseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('break_phase.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_break.corr, level);
    }
    psychoJS.experiment.addData('key_break.keys', key_break.keys);
    if (typeof key_break.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_break.rt', key_break.rt);
        psychoJS.experiment.addData('key_break.duration', key_break.duration);
        routineTimer.reset();
        }
    
    key_break.stop();
    // the Routine "break_phase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedbacktestMaxDurationReached;
var _key_resp_allKeys;
var feedbacktestMaxDuration;
var feedbacktestComponents;
function feedbacktestRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedbacktest' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedbacktestClock.reset(routineTimer.getTime());
    routineTimer.add(5.000000);
    feedbacktestMaxDurationReached = false;
    // update component parameters for each repeat
    feedbackbrand.setText(brand);
    feedbackslogan.setText(slogan);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('feedbacktest.started', globalClock.getTime());
    feedbacktestMaxDuration = null
    // keep track of which components have finished
    feedbacktestComponents = [];
    feedbacktestComponents.push(feedbackbrand);
    feedbacktestComponents.push(feedbackslogan);
    feedbacktestComponents.push(key_resp);
    
    for (const thisComponent of feedbacktestComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbacktestRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedbacktest' ---
    // get current time
    t = feedbacktestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedbackbrand* updates
    if (t >= 0.0 && feedbackbrand.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbackbrand.tStart = t;  // (not accounting for frame time here)
      feedbackbrand.frameNStart = frameN;  // exact frame index
      
      feedbackbrand.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedbackbrand.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedbackbrand.setAutoDraw(false);
    }
    
    
    // *feedbackslogan* updates
    if (t >= 0.0 && feedbackslogan.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbackslogan.tStart = t;  // (not accounting for frame time here)
      feedbackslogan.frameNStart = frameN;  // exact frame index
      
      feedbackslogan.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedbackslogan.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedbackslogan.setAutoDraw(false);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbacktestComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbacktestRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedbacktest' ---
    for (const thisComponent of feedbacktestComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedbacktest.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    if (feedbacktestMaxDurationReached) {
        feedbacktestClock.add(feedbacktestMaxDuration);
    } else {
        feedbacktestClock.add(5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var end_screenMaxDurationReached;
var _key_end_allKeys;
var end_screenMaxDuration;
var end_screenComponents;
function end_screenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_screen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    end_screenClock.reset();
    routineTimer.reset();
    end_screenMaxDurationReached = false;
    // update component parameters for each repeat
    key_end.keys = undefined;
    key_end.rt = undefined;
    _key_end_allKeys = [];
    psychoJS.experiment.addData('end_screen.started', globalClock.getTime());
    end_screenMaxDuration = null
    // keep track of which components have finished
    end_screenComponents = [];
    end_screenComponents.push(end_text);
    end_screenComponents.push(key_end);
    
    for (const thisComponent of end_screenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_screenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_screen' ---
    // get current time
    t = end_screenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_text* updates
    if (t >= 0.0 && end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_text.tStart = t;  // (not accounting for frame time here)
      end_text.frameNStart = frameN;  // exact frame index
      
      end_text.setAutoDraw(true);
    }
    
    
    // *key_end* updates
    if (t >= 3 && key_end.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_end.tStart = t;  // (not accounting for frame time here)
      key_end.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_end.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_end.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_end.clearEvents(); });
    }
    
    if (key_end.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_end.getKeys({keyList: ['space'], waitRelease: false});
      _key_end_allKeys = _key_end_allKeys.concat(theseKeys);
      if (_key_end_allKeys.length > 0) {
        key_end.keys = _key_end_allKeys[_key_end_allKeys.length - 1].name;  // just the last key pressed
        key_end.rt = _key_end_allKeys[_key_end_allKeys.length - 1].rt;
        key_end.duration = _key_end_allKeys[_key_end_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_screenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_screenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_screen' ---
    for (const thisComponent of end_screenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end_screen.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_end.corr, level);
    }
    psychoJS.experiment.addData('key_end.keys', key_end.keys);
    if (typeof key_end.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_end.rt', key_end.rt);
        psychoJS.experiment.addData('key_end.duration', key_end.duration);
        routineTimer.reset();
        }
    
    key_end.stop();
    // the Routine "end_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
