#-*- coding: utf-8 -*-
from PythonQt import QtCore, QtGui, MarvelousDesignerAPI
from PythonQt.MarvelousDesignerAPI import *

#####################################################################
# Contributors 
# Company: CLO Virtual Fashion, Inc.
# Test Engineers : Jake, Diana
# Software Engineers  : James, Joshua

import os
#from os import path
import time

########### Class for QA Automation by Test Engineers ############
## Owners: Jake, Diana

####
## Class Name: AutoTest
## Purpose : QA Test Automation
class AutoTest:
    # export dxf 테스트 자동화 함수
    def export_dxf_automation(object):
        inputfolder = "C:/Users/Public/Documents/Test Automation/project files"
        outputfolder = "C:/Users/Public/Documents/Test Automation/dxf files"
        allfilelist = os.listdir(inputfolder)
        inputfilelist = []
        for filename in allfilelist:
            filext = os.path.splitext(filename)[1]
            if filext == ".zprj" or filext == ".Zprj":
                inputfilelist.append(inputfolder + filename)
        pta = PythonTestAPIExportDXF()
        for filename in inputfilelist:
            ## Init export dxf options
            pta.init_export_dxf_option()
            ## first option
            pta.m_TestName = "First_Option"
            pta.export_dxf(filename, output_folder_path)
            ## second option
            pta.init_export_dxf_option()
            pta.m_TestName = "Second_Option"
            pta.m_RotateAngle = 45.0
            pta.export_dxf(filename, output_folder_path)
            ## third option
            pta.init_export_dxf_option()
            pta.m_TestName = "Third_Option"
            pta.m_RotateAngle = 90.0
            pta.m_fScale = 2.0
            pta.export_dxf(filename, output_folder_path)
            ## add to other options......
            ## Write Log
        #pta.m_bSwapOutLine = False
        #pta.m_bDupliateNotch = False
        #pta.m_bCheckedConvertCtoS = False
        #pta.m_ExportWithoutGrading = False
        #pta.m_bOptimizeCurvePoints = False
        #pta.m_bExportWithoutBaselines = False
        #pta.m_ExportDXFFormatType = 1
        #pta.m_ExportBBType = 1
        #pta.m_fScale = 1.0
        #pta.m_RotateAngle = 0.0
        #pta.m_bMetric = True
        #pta.m_TestName = "First_Option"
        #pta.export_dxf_multi(inputfilelist, outputfolder)

 # high quality rendering 테스트 자동화 함수
    def interactive_render_automation(object):
        inputfolder = "C:/Users/Public/Documents/Test Automation/project files/"
        outputfolder = "C:/Users/Public/Documents/Test Automation/render/"
        allfilelist = os.listdir(inputfolder)
        inputfilelist = []
        for filename in allfilelist:
            filext = os.path.splitext(filename)[1]
            if filext == ".zprj" or filext == ".Zprj":
                inputfilelist.append(inputfolder + filename)
        ptar = PythonTestAPIRender()
        ptar.interactive_render_multi(inputfilelist, outputfolder)

    def final_render_automation(object):
        inputfolder = "C:/Users/Public/Documents/Test Automation/project files/"
        outputfolder = "C:/Users/Public/Documents/Test Automation/render/"
        allfilelist = os.listdir(inputfolder)
        inputfilelist = []
        for filename in allfilelist:
            filext = os.path.splitext(filename)[1]
            if filext == ".zprj" or filext == ".Zprj":
                inputfilelist.append(inputfolder + filename)
        ptar = PythonTestAPIRender()
        ptar.final_render_multi(inputfilelist, outputfolder)

    # mode 변경 테스트 자동화 함수
    def change_mode_automation(object):
        return

    # colorway mode 테스트 자동화 함수
    def colorway_mode_automation(object):
        return

    # simulation speed 측정 테스트 자동화 함수
    def simulation_speed_automation(object):
        return

    # file type별 로드/저장 테스트 자동화 함수
    def file_load_save_by_type_automation(object):
        return

    def file_load_save_by_version_automation(object):
        return

    # image file type별 pattern에 텍스쳐 적용 테스트 자동화 함수
    def apply_texture_file_format_on_pattern_automation(object):
        return


########### Classes for Python API by Software Engineers ############
## Purpose: Open Marvelous Designer functions to Python API for QA Test Automation
## Owners: Joshua, James
##        

####
## Class Name: PythonTestAPIExportDXF
## Purpose: Open Python APIs for Export DXF Test Automation
##
## Export DXF Options
## bool m_bSwapOutLine;  	    // if true, swap the boundary line with sew line
## bool m_bDuplicateNotch;	    // if true, remove duplicate notches
## bool m_bCheckedConvertCtoS;	    // if true, convert curve points to straight points to export
## bool m_bExportWithoutGrading;    // if true, export without grading information
## bool m_bOptimizeCurvePoints;	    // if true, optimize curve points with removing the points close to some points
## bool m_bExportWithoutBaselines;     // if true, export only out lines without base lines
## unsigned int m_ExportDXFFormatType; // 0: DXF-AAMA, 1: DXF-ASTM
## unsigned int m_ExportBBType;		// 1: Use Bounding box covering all the patterns, 2: use Bounding Box for each pattern
## float m_fScale;     		    // scale variables 
## float m_RotateAngle;		    // Rotation angle for patterns
## bool m_bMetric;		    // Measurement unit shown on DXF, true: Metric, false: English
##
class PythonTestAPIExportDXF:    
    m_bSwapOutLine = False
    m_bDuplicateNotch = False
    m_bCheckedConvertCtoS = False
    m_bExportWithoutGrading = False
    m_bOptimizeCurvePoints = False
    m_bExportWithoutBaselines = False
    m_ExportDXFFormatType = 1
    m_ExportBBType = 1
    m_fScale = 1.0
    m_RotateAngle = 0.0
    m_bMetric = True
    m_TestName = "BaseTest"
    
    __mdm_func = MarvelousDesignerModule()
    
    def export_dxf(object, input_file, output_folder_path):
        print("Trying to import zprj " + input_file)
        print(object.__mdm_func.ImportZprj(input_file, True))
        outputpath = object.get_output_dxf_file_path(input_file, output_folder_path)
        print("Setting for Export DXF options for " + outputpath)
        object.__mdm_func.SetSwapOutLineOnExportAPI(object.m_bSwapOutLine)
        object.__mdm_func.SetDuplicateNotchOnExportAPI(object.m_bDuplicateNotch)
        object.__mdm_func.SetCheckedConvertCtoSOnExportAPI(object.m_bCheckedConvertCtoS)
        object.__mdm_func.SetExportWithoutGradingOnExportAPI(object.m_bExportWithoutGrading)
        object.__mdm_func.SetOptimizeCurvePointsOnExportAPI(object.m_bOptimizeCurvePoints)
        object.__mdm_func.SetExportWithoutBaselinesOnExportAPI(object.m_bExportWithoutBaselines)
        object.__mdm_func.SetExportDXFFormatTypeOnExportAPI(object.m_ExportDXFFormatType)
        object.__mdm_func.SetExportBBTypeOnExportAPI(object.m_ExportBBType)
        object.__mdm_func.SetExportDXFScaleOnExportAPI(object.m_fScale)
        object.__mdm_func.SetRotateAngleOnExportAPI(object.m_RotateAngle)
        object.__mdm_func.SetMetricOnExportAPI(object.m_bMetric)        
        print("Trying to Export Dxf " + outputpath)
        print(object.__mdm_func.ExportDXF(outputpath, True))
    
    def export_dxf_multi(object, input_file_list, output_folder_path):
        for filename in input_file_list:
            object.export_dxf(filename, output_folder_path)

    def get_output_dxf_file_path(object, input_file, output_folder_path):
        onlyfilename = os.path.splitext(os.path.basename(input_file))[0]
        outputpath = output_folder_path + onlyfilename + "_" + object.m_TestName + ".dxf"
        return outputpath

    def init_export_dxf_option(object):
        m_bSwapOutLine = False
        m_bDuplicateNotch = False
        m_bCheckedConvertCtoS = False
        m_bExportWithoutGrading = False
        m_bOptimizeCurvePoints = False
        m_bExportWithoutBaselines = False
        m_ExportDXFFormatType = 1
        m_ExportBBType = 1
        m_fScale = 1.0
        m_RotateAngle = 0.0
        m_bMetric = True
        m_TestName = "BaseTest"

####
## Class Name: PythonTestAPICommon
## Purpose: Open Python APIs for Common functions in QA Test Automation
##
class PythonTestAPICommon:
    __mdm_func = MarvelousDesignerModule()
    
    def capture_screen(object, outputpath):
        object.__mdm_func.CaptureScreen(outputpath)

    def capture_2d_window(object, outputpath):
        object.__mdm_func.Capture2DWindow(outputpath)

    def capture_3d_window(object, outputpath):
        object.__mdm_func.Capture3DWindow(outputpath)

    def write_log(object, log_file_name, log):
        object.__mdm_func.WriteLogFile(log_file_name, log)

    def undo(object):
        object.__mdm_func.Undo()

    def redo(object):
        object.__mdm_func.Redo()

####
## Class Name: PythonTestAPIRender
## Purpose: Open Python APIs for Render functions in QA Test Automation
##
class PythonTestAPIRender:
    __mdm_func = MarvelousDesignerModule()
    __common = PythonTestAPICommon()
    
    def execute_render(object):
        object.__mdm_func.ExecuteRender()

    def start_interactive_render(object):
        object.__mdm_func.StartInteractiveRender()

    def set_render_option(object, json_file_path):
        object.__mdm_func.SetRenderProperties(json_file_path)

    def set_render_output_image_path(object, output_image_path):
        object.__mdm_func.SetRenderOutputImagePath(output_image_path)

    def start_final_render(object):
        object.__mdm_func.StartFinalRender()

    def interactive_render(object, input_file, output_folder_path):
        print("Trying to import zprj " + input_file)
        object.__mdm_func.ImportZprj(input_file, True)
        object.__mdm_func.ExecuteRender()
        object.__mdm_func.StartInteractiveRender()
        outputpath = object.get_output_capture_file_path(input_file, output_folder_path)
        time.sleep(10)
        object.__mdm_func.StartInteractiveRender()
        object.__common.capture_screen(outputpath)

    def interactive_render_multi(object, input_file_list, output_folder_path):
        for filename in input_file_list:
            object.interactive_render(filename, output_folder_path)

    def final_render(object, input_file, output_folder_path):
        print("Trying to import zprj " + input_file)
        object.__mdm_func.ImportZprj(input_file, True)
        object.__mdm_func.ExecuteRender()
        object.__mdm_func.StartFinalRender()
        outputpath = object.get_output_capture_file_path(input_file, output_folder_path)
        object.__common.capture_screen(outputpath)

    def final_render_multi(object, input_file_list, output_folder_path):
        for filename in input_file_list:
            object.final_render(filename, output_folder_path)
            
    def get_output_capture_file_path(object, input_file, output_folder_path):
        onlyfilename = os.path.splitext(os.path.basename(input_file))[0]
        outputpath = output_folder_path + onlyfilename + "_screen_capture.jpg"
        return outputpath
    
####
## Class Name: PythonTestAPIModeChange
## Purpose: Open Python APIs for Play Mode Change functions in QA Test Automation
##
class PythonTestAPIModeChange:
    __mdm_func = MarvelousDesignerModule()
    
    def execute_mode_change(object, test_file_path):
        ## Write Log
        ## Get PlayMode List
        modeList = get_play_mode_list()
        ## File Open
        for fileName in test_file_path:
            object.__mdm_func.ImportZprj(fileName, True)
            ## Change Mode
            for modename in modeList:
                change_play_mode(modename, True)
                ## Undo
                object.__mdm_func.Undo()
                ## Redo
                object.__mdm_func.Redo()
                ## Write Log
            ## Write Log
        ## Write Log

    def get_play_mode_list(object):
        return object.__mdm_func.GetPlayModeList()

    def change_play_mode(object, mode_name, bUnRe):
        object.__mdm_func.ChangePlayMode(mode_name, bUnRe)

    
