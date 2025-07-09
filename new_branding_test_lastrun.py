#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on July 09, 2025, at 18:56
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'new branding test'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\000Faezeh\\New folder\\new branding test_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_welcome') is None:
        # initialise key_welcome
        key_welcome = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_welcome',
        )
    if deviceManager.getDevice('key_instruction') is None:
        # initialise key_instruction
        key_instruction = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruction',
        )
    if deviceManager.getDevice('key_break') is None:
        # initialise key_break
        key_break = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_break',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_end') is None:
        # initialise key_end
        key_end = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_end',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome_screen" ---
    welcome_text = visual.TextStim(win=win, name='welcome_text',
        text='سلام\nروز خوش\n\nممنونم که ما را در انجام این آزمون همراهی می کنید\n با فشردن کلید\n space\nبه صفحه بعد منتقل می شوید.',
        font='B Nazanin',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    key_welcome = keyboard.Keyboard(deviceName='key_welcome')
    
    # --- Initialize components for Routine "instruction" ---
    Instruction_text = visual.TextStim(win=win, name='Instruction_text',
        text=' سلام و خوش آمدید\n\nشما در حال شرکت در یک آزمون حافظه و \nتوجه هستید. این آزمون شامل دو مرحله است\n\n «مرحله اول: «یادگیری برندها و شعارها\nدر این مرحله، تعدادی برند به\u200cهمراه شعار آن\u200cها\n روی صفحه نمایش داده می\u200cشوند.  \nلطفاً با دقت به برند و شعار نمایش\u200cداده\u200cشده \nنگاه کنید و سعی کنید آن را به خاطر بسپارید.  \nبرخی از برندها ممکن است چند بار تکرار شوند.\n\n هر برند و شعار به مدت چند ثانیه نمایش داده می\u200cشود.\n\n« مرحله دوم: «تشخیص\nپس از پایان مرحله یادگیری، برندها و شعارهایی\n به شما نمایش داده می\u200cشوند.  \nبرخی از آن\u200cها در مرحله یادگیری وجود داشتند و برخی جدید هستند.  \nشما باید با فشردن یکی از دکمه\u200cهای زیر پاسخ دهید:\n\n اگر فکر می\u200cکنید این برند و شعار در مرحله یادگیری وجود داشت\n، کلید Y را فشار دهید.  \n اگر فکر می\u200cکنید قبلاً این برند و شعار را ندیده\u200cاید،\n کلید N را فشار دهید.\n\n سعی کنید با دقت و بدون عجله پاسخ دهید.\n اطلاعات شما فقط برای اهداف پژوهشی استفاده خواهد شد.\n\nبرای شروع آزمون کلید\n Space فشار دهید.',
        font='B Nazanin',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    key_instruction = keyboard.Keyboard(deviceName='key_instruction')
    
    # --- Initialize components for Routine "study_phase" ---
    brands = visual.TextStim(win=win, name='brands',
        text='',
        font='B Nazanin',
        pos=(0, 0.1), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    slogan_2 = visual.TextStim(win=win, name='slogan_2',
        text='',
        font='B Nazanin',
        pos=(0,-0.1), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='red', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-1.0);
    
    # --- Initialize components for Routine "fixction" ---
    cross = visual.ShapeStim(
        win=win, name='cross', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "break_phase" ---
    break_text = visual.TextStim(win=win, name='break_text',
        text='لطفا 5 دقیقه استراحت کنید.\n\n\nبا فشردن کلید\n space\nبه صفحه بعد منتقل می شوید.',
        font='B Nazanin',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    key_break = keyboard.Keyboard(deviceName='key_break')
    
    # --- Initialize components for Routine "feedbacktest" ---
    feedbackbrand = visual.TextStim(win=win, name='feedbackbrand',
        text='',
        font='B Nazanin',
        pos=(0, 0.1), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    feedbackslogan = visual.TextStim(win=win, name='feedbackslogan',
        text='',
        font='B Nazanin',
        pos=(0, -0.1), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='red', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-1.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "end_screen" ---
    end_text = visual.TextStim(win=win, name='end_text',
        text='سپاسگزارم بابت همراهی تون\nروز خوش\n\n\nلطفا کمی صبر کنید ما در حال ذخیره سازی\nاطلاعات آزمون شما هستیم\nسپس با فشردن کلید \nspace\nاز آزمون خارج شوید',
        font='B Nazanin',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    key_end = keyboard.Keyboard(deviceName='key_end')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcome_screen" ---
    # create an object to store info about Routine welcome_screen
    welcome_screen = data.Routine(
        name='welcome_screen',
        components=[welcome_text, key_welcome],
    )
    welcome_screen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_welcome
    key_welcome.keys = []
    key_welcome.rt = []
    _key_welcome_allKeys = []
    # store start times for welcome_screen
    welcome_screen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome_screen.tStart = globalClock.getTime(format='float')
    welcome_screen.status = STARTED
    thisExp.addData('welcome_screen.started', welcome_screen.tStart)
    welcome_screen.maxDuration = None
    # keep track of which components have finished
    welcome_screenComponents = welcome_screen.components
    for thisComponent in welcome_screen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome_screen" ---
    welcome_screen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_text* updates
        
        # if welcome_text is starting this frame...
        if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text.frameNStart = frameN  # exact frame index
            welcome_text.tStart = t  # local t and not account for scr refresh
            welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_text.started')
            # update status
            welcome_text.status = STARTED
            welcome_text.setAutoDraw(True)
        
        # if welcome_text is active this frame...
        if welcome_text.status == STARTED:
            # update params
            pass
        
        # *key_welcome* updates
        waitOnFlip = False
        
        # if key_welcome is starting this frame...
        if key_welcome.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            key_welcome.frameNStart = frameN  # exact frame index
            key_welcome.tStart = t  # local t and not account for scr refresh
            key_welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_welcome.started')
            # update status
            key_welcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_welcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_welcome.status == STARTED and not waitOnFlip:
            theseKeys = key_welcome.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_welcome_allKeys.extend(theseKeys)
            if len(_key_welcome_allKeys):
                key_welcome.keys = _key_welcome_allKeys[-1].name  # just the last key pressed
                key_welcome.rt = _key_welcome_allKeys[-1].rt
                key_welcome.duration = _key_welcome_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            welcome_screen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome_screen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome_screen" ---
    for thisComponent in welcome_screen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome_screen
    welcome_screen.tStop = globalClock.getTime(format='float')
    welcome_screen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome_screen.stopped', welcome_screen.tStop)
    # check responses
    if key_welcome.keys in ['', [], None]:  # No response was made
        key_welcome.keys = None
    thisExp.addData('key_welcome.keys',key_welcome.keys)
    if key_welcome.keys != None:  # we had a response
        thisExp.addData('key_welcome.rt', key_welcome.rt)
        thisExp.addData('key_welcome.duration', key_welcome.duration)
    thisExp.nextEntry()
    # the Routine "welcome_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction" ---
    # create an object to store info about Routine instruction
    instruction = data.Routine(
        name='instruction',
        components=[Instruction_text, key_instruction],
    )
    instruction.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_instruction
    key_instruction.keys = []
    key_instruction.rt = []
    _key_instruction_allKeys = []
    # store start times for instruction
    instruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction.tStart = globalClock.getTime(format='float')
    instruction.status = STARTED
    thisExp.addData('instruction.started', instruction.tStart)
    instruction.maxDuration = None
    # keep track of which components have finished
    instructionComponents = instruction.components
    for thisComponent in instruction.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction" ---
    instruction.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instruction_text* updates
        
        # if Instruction_text is starting this frame...
        if Instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction_text.frameNStart = frameN  # exact frame index
            Instruction_text.tStart = t  # local t and not account for scr refresh
            Instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction_text.started')
            # update status
            Instruction_text.status = STARTED
            Instruction_text.setAutoDraw(True)
        
        # if Instruction_text is active this frame...
        if Instruction_text.status == STARTED:
            # update params
            pass
        
        # *key_instruction* updates
        waitOnFlip = False
        
        # if key_instruction is starting this frame...
        if key_instruction.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            key_instruction.frameNStart = frameN  # exact frame index
            key_instruction.tStart = t  # local t and not account for scr refresh
            key_instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instruction, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_instruction.started')
            # update status
            key_instruction.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instruction.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instruction.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instruction.status == STARTED and not waitOnFlip:
            theseKeys = key_instruction.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instruction_allKeys.extend(theseKeys)
            if len(_key_instruction_allKeys):
                key_instruction.keys = _key_instruction_allKeys[-1].name  # just the last key pressed
                key_instruction.rt = _key_instruction_allKeys[-1].rt
                key_instruction.duration = _key_instruction_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instruction.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction" ---
    for thisComponent in instruction.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction
    instruction.tStop = globalClock.getTime(format='float')
    instruction.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruction.stopped', instruction.tStop)
    # check responses
    if key_instruction.keys in ['', [], None]:  # No response was made
        key_instruction.keys = None
    thisExp.addData('key_instruction.keys',key_instruction.keys)
    if key_instruction.keys != None:  # we had a response
        thisExp.addData('key_instruction.rt', key_instruction.rt)
        thisExp.addData('key_instruction.duration', key_instruction.duration)
    thisExp.nextEntry()
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    study_brands = data.TrialHandler2(
        name='study_brands',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('D:/000Faezeh/پایان نامه قطعی/پرسشنامه/psychopy/studyphase.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(study_brands)  # add the loop to the experiment
    thisStudy_brand = study_brands.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStudy_brand.rgb)
    if thisStudy_brand != None:
        for paramName in thisStudy_brand:
            globals()[paramName] = thisStudy_brand[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisStudy_brand in study_brands:
        currentLoop = study_brands
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisStudy_brand.rgb)
        if thisStudy_brand != None:
            for paramName in thisStudy_brand:
                globals()[paramName] = thisStudy_brand[paramName]
        
        # --- Prepare to start Routine "study_phase" ---
        # create an object to store info about Routine study_phase
        study_phase = data.Routine(
            name='study_phase',
            components=[brands, slogan_2],
        )
        study_phase.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        brands.setText(brand)
        slogan_2.setText(slogan)
        # store start times for study_phase
        study_phase.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        study_phase.tStart = globalClock.getTime(format='float')
        study_phase.status = STARTED
        thisExp.addData('study_phase.started', study_phase.tStart)
        study_phase.maxDuration = None
        # keep track of which components have finished
        study_phaseComponents = study_phase.components
        for thisComponent in study_phase.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "study_phase" ---
        # if trial has changed, end Routine now
        if isinstance(study_brands, data.TrialHandler2) and thisStudy_brand.thisN != study_brands.thisTrial.thisN:
            continueRoutine = False
        study_phase.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *brands* updates
            
            # if brands is starting this frame...
            if brands.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                brands.frameNStart = frameN  # exact frame index
                brands.tStart = t  # local t and not account for scr refresh
                brands.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(brands, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'brands.started')
                # update status
                brands.status = STARTED
                brands.setAutoDraw(True)
            
            # if brands is active this frame...
            if brands.status == STARTED:
                # update params
                pass
            
            # if brands is stopping this frame...
            if brands.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > brands.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    brands.tStop = t  # not accounting for scr refresh
                    brands.tStopRefresh = tThisFlipGlobal  # on global time
                    brands.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'brands.stopped')
                    # update status
                    brands.status = FINISHED
                    brands.setAutoDraw(False)
            
            # *slogan_2* updates
            
            # if slogan_2 is starting this frame...
            if slogan_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slogan_2.frameNStart = frameN  # exact frame index
                slogan_2.tStart = t  # local t and not account for scr refresh
                slogan_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slogan_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slogan_2.started')
                # update status
                slogan_2.status = STARTED
                slogan_2.setAutoDraw(True)
            
            # if slogan_2 is active this frame...
            if slogan_2.status == STARTED:
                # update params
                pass
            
            # if slogan_2 is stopping this frame...
            if slogan_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > slogan_2.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    slogan_2.tStop = t  # not accounting for scr refresh
                    slogan_2.tStopRefresh = tThisFlipGlobal  # on global time
                    slogan_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'slogan_2.stopped')
                    # update status
                    slogan_2.status = FINISHED
                    slogan_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                study_phase.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in study_phase.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "study_phase" ---
        for thisComponent in study_phase.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for study_phase
        study_phase.tStop = globalClock.getTime(format='float')
        study_phase.tStopRefresh = tThisFlipGlobal
        thisExp.addData('study_phase.stopped', study_phase.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if study_phase.maxDurationReached:
            routineTimer.addTime(-study_phase.maxDuration)
        elif study_phase.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # --- Prepare to start Routine "fixction" ---
        # create an object to store info about Routine fixction
        fixction = data.Routine(
            name='fixction',
            components=[cross],
        )
        fixction.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixction
        fixction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixction.tStart = globalClock.getTime(format='float')
        fixction.status = STARTED
        thisExp.addData('fixction.started', fixction.tStart)
        fixction.maxDuration = None
        # keep track of which components have finished
        fixctionComponents = fixction.components
        for thisComponent in fixction.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixction" ---
        # if trial has changed, end Routine now
        if isinstance(study_brands, data.TrialHandler2) and thisStudy_brand.thisN != study_brands.thisTrial.thisN:
            continueRoutine = False
        fixction.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.4:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            
            # if cross is starting this frame...
            if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross.frameNStart = frameN  # exact frame index
                cross.tStart = t  # local t and not account for scr refresh
                cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.started')
                # update status
                cross.status = STARTED
                cross.setAutoDraw(True)
            
            # if cross is active this frame...
            if cross.status == STARTED:
                # update params
                pass
            
            # if cross is stopping this frame...
            if cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 0.4-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.tStopRefresh = tThisFlipGlobal  # on global time
                    cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross.stopped')
                    # update status
                    cross.status = FINISHED
                    cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fixction.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixction.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixction" ---
        for thisComponent in fixction.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixction
        fixction.tStop = globalClock.getTime(format='float')
        fixction.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixction.stopped', fixction.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixction.maxDurationReached:
            routineTimer.addTime(-fixction.maxDuration)
        elif fixction.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.400000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'study_brands'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "break_phase" ---
    # create an object to store info about Routine break_phase
    break_phase = data.Routine(
        name='break_phase',
        components=[break_text, key_break],
    )
    break_phase.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_break
    key_break.keys = []
    key_break.rt = []
    _key_break_allKeys = []
    # store start times for break_phase
    break_phase.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    break_phase.tStart = globalClock.getTime(format='float')
    break_phase.status = STARTED
    thisExp.addData('break_phase.started', break_phase.tStart)
    break_phase.maxDuration = None
    # keep track of which components have finished
    break_phaseComponents = break_phase.components
    for thisComponent in break_phase.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "break_phase" ---
    break_phase.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text* updates
        
        # if break_text is starting this frame...
        if break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_text.frameNStart = frameN  # exact frame index
            break_text.tStart = t  # local t and not account for scr refresh
            break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'break_text.started')
            # update status
            break_text.status = STARTED
            break_text.setAutoDraw(True)
        
        # if break_text is active this frame...
        if break_text.status == STARTED:
            # update params
            pass
        
        # *key_break* updates
        waitOnFlip = False
        
        # if key_break is starting this frame...
        if key_break.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            key_break.frameNStart = frameN  # exact frame index
            key_break.tStart = t  # local t and not account for scr refresh
            key_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_break, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_break.started')
            # update status
            key_break.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_break.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_break.status == STARTED and not waitOnFlip:
            theseKeys = key_break.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_break_allKeys.extend(theseKeys)
            if len(_key_break_allKeys):
                key_break.keys = _key_break_allKeys[-1].name  # just the last key pressed
                key_break.rt = _key_break_allKeys[-1].rt
                key_break.duration = _key_break_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break_phase.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_phase.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "break_phase" ---
    for thisComponent in break_phase.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for break_phase
    break_phase.tStop = globalClock.getTime(format='float')
    break_phase.tStopRefresh = tThisFlipGlobal
    thisExp.addData('break_phase.stopped', break_phase.tStop)
    # check responses
    if key_break.keys in ['', [], None]:  # No response was made
        key_break.keys = None
    thisExp.addData('key_break.keys',key_break.keys)
    if key_break.keys != None:  # we had a response
        thisExp.addData('key_break.rt', key_break.rt)
        thisExp.addData('key_break.duration', key_break.duration)
    thisExp.nextEntry()
    # the Routine "break_phase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    test_brands = data.TrialHandler2(
        name='test_brands',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('D:/000Faezeh/پایان نامه قطعی/پرسشنامه/psychopy/testphase.csv'), 
        seed=None, 
    )
    thisExp.addLoop(test_brands)  # add the loop to the experiment
    thisTest_brand = test_brands.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest_brand.rgb)
    if thisTest_brand != None:
        for paramName in thisTest_brand:
            globals()[paramName] = thisTest_brand[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTest_brand in test_brands:
        currentLoop = test_brands
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTest_brand.rgb)
        if thisTest_brand != None:
            for paramName in thisTest_brand:
                globals()[paramName] = thisTest_brand[paramName]
        
        # --- Prepare to start Routine "feedbacktest" ---
        # create an object to store info about Routine feedbacktest
        feedbacktest = data.Routine(
            name='feedbacktest',
            components=[feedbackbrand, feedbackslogan, key_resp],
        )
        feedbacktest.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        feedbackbrand.setText(brand)
        feedbackslogan.setText(slogan)
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # store start times for feedbacktest
        feedbacktest.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedbacktest.tStart = globalClock.getTime(format='float')
        feedbacktest.status = STARTED
        thisExp.addData('feedbacktest.started', feedbacktest.tStart)
        feedbacktest.maxDuration = None
        # keep track of which components have finished
        feedbacktestComponents = feedbacktest.components
        for thisComponent in feedbacktest.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedbacktest" ---
        # if trial has changed, end Routine now
        if isinstance(test_brands, data.TrialHandler2) and thisTest_brand.thisN != test_brands.thisTrial.thisN:
            continueRoutine = False
        feedbacktest.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbackbrand* updates
            
            # if feedbackbrand is starting this frame...
            if feedbackbrand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackbrand.frameNStart = frameN  # exact frame index
                feedbackbrand.tStart = t  # local t and not account for scr refresh
                feedbackbrand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackbrand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbackbrand.started')
                # update status
                feedbackbrand.status = STARTED
                feedbackbrand.setAutoDraw(True)
            
            # if feedbackbrand is active this frame...
            if feedbackbrand.status == STARTED:
                # update params
                pass
            
            # if feedbackbrand is stopping this frame...
            if feedbackbrand.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackbrand.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackbrand.tStop = t  # not accounting for scr refresh
                    feedbackbrand.tStopRefresh = tThisFlipGlobal  # on global time
                    feedbackbrand.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedbackbrand.stopped')
                    # update status
                    feedbackbrand.status = FINISHED
                    feedbackbrand.setAutoDraw(False)
            
            # *feedbackslogan* updates
            
            # if feedbackslogan is starting this frame...
            if feedbackslogan.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackslogan.frameNStart = frameN  # exact frame index
                feedbackslogan.tStart = t  # local t and not account for scr refresh
                feedbackslogan.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackslogan, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbackslogan.started')
                # update status
                feedbackslogan.status = STARTED
                feedbackslogan.setAutoDraw(True)
            
            # if feedbackslogan is active this frame...
            if feedbackslogan.status == STARTED:
                # update params
                pass
            
            # if feedbackslogan is stopping this frame...
            if feedbackslogan.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackslogan.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackslogan.tStop = t  # not accounting for scr refresh
                    feedbackslogan.tStopRefresh = tThisFlipGlobal  # on global time
                    feedbackslogan.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedbackslogan.stopped')
                    # update status
                    feedbackslogan.status = FINISHED
                    feedbackslogan.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['y','n'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedbacktest.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbacktest.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedbacktest" ---
        for thisComponent in feedbacktest.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedbacktest
        feedbacktest.tStop = globalClock.getTime(format='float')
        feedbacktest.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedbacktest.stopped', feedbacktest.tStop)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        test_brands.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            test_brands.addData('key_resp.rt', key_resp.rt)
            test_brands.addData('key_resp.duration', key_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedbacktest.maxDurationReached:
            routineTimer.addTime(-feedbacktest.maxDuration)
        elif feedbacktest.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'test_brands'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end_screen" ---
    # create an object to store info about Routine end_screen
    end_screen = data.Routine(
        name='end_screen',
        components=[end_text, key_end],
    )
    end_screen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_end
    key_end.keys = []
    key_end.rt = []
    _key_end_allKeys = []
    # Run 'Begin Routine' code from exit
    // Prevent PsychoJS’s default download dialog
    psychoJS._saveResults = 0;
    // Build a filename: experimentName_datetime.csv
    const filename = `${psychoJS._experiment._experimentName}_${psychoJS._experiment._datetime}.csv`;
    // Extract trial data as an array of objects
    const dataObj = psychoJS._experiment._trialsData;
    // Convert array of objects to CSV string
    const data = [Object.keys(dataObj[0])].concat(dataObj).map(row => {
      return Object.values(row).toString();
    }).join('\n');
    // POST data to DataPipe’s API endpoint
    fetch('https://pipe.jspsych.org/api/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: '*/*',
      },
      body: JSON.stringify({
        experimentID: 'sbUdjyD5xBio', // ← Replace with your DataPipe ID
        filename: filename,
        data: data,
      }),
    })
      .then(response => response.json())
      .then(json => {
        console.log('DataPipe response:', json);
        // After saving, end the PsychoJS experiment
        quitPsychoJS();
      })
      .catch(err => {
        console.error('Error sending data to DataPipe:', err);
        quitPsychoJS();
      });
    
    # store start times for end_screen
    end_screen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end_screen.tStart = globalClock.getTime(format='float')
    end_screen.status = STARTED
    thisExp.addData('end_screen.started', end_screen.tStart)
    end_screen.maxDuration = None
    # keep track of which components have finished
    end_screenComponents = end_screen.components
    for thisComponent in end_screen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_screen" ---
    end_screen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_text* updates
        
        # if end_text is starting this frame...
        if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_text.frameNStart = frameN  # exact frame index
            end_text.tStart = t  # local t and not account for scr refresh
            end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_text.started')
            # update status
            end_text.status = STARTED
            end_text.setAutoDraw(True)
        
        # if end_text is active this frame...
        if end_text.status == STARTED:
            # update params
            pass
        
        # *key_end* updates
        waitOnFlip = False
        
        # if key_end is starting this frame...
        if key_end.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            key_end.frameNStart = frameN  # exact frame index
            key_end.tStart = t  # local t and not account for scr refresh
            key_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_end, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_end.started')
            # update status
            key_end.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_end.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_end.status == STARTED and not waitOnFlip:
            theseKeys = key_end.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_end_allKeys.extend(theseKeys)
            if len(_key_end_allKeys):
                key_end.keys = _key_end_allKeys[-1].name  # just the last key pressed
                key_end.rt = _key_end_allKeys[-1].rt
                key_end.duration = _key_end_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end_screen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_screen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_screen" ---
    for thisComponent in end_screen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end_screen
    end_screen.tStop = globalClock.getTime(format='float')
    end_screen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end_screen.stopped', end_screen.tStop)
    # check responses
    if key_end.keys in ['', [], None]:  # No response was made
        key_end.keys = None
    thisExp.addData('key_end.keys',key_end.keys)
    if key_end.keys != None:  # we had a response
        thisExp.addData('key_end.rt', key_end.rt)
        thisExp.addData('key_end.duration', key_end.duration)
    thisExp.nextEntry()
    # the Routine "end_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
