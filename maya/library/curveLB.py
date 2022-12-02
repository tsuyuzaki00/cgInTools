# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import math

from . import setBaseLB as sbLB

class SetCurve(sbLB.BaseName):
    def __init__(self):
        self._name="curveName"
        self._curveType="circlePlane"

    def create(self):
        curveFunction=eval("self."+self._curveType+"_create_curve")
        curveFunction(name=self._name)

    def trsSetting(self,ctrl):
        createNull=cmds.createNode('transform')
        renameNull=self.renameTemplate(sel=createNull)
        trs=cmds.rename(createNull,renameNull)
        cmds.parent(ctrl,trs)
        return trs

    def selectPosition(self, sel, trs):
        cmds.parent(trs, sel)
        cmds.move(0, 0, 0 ,ls=True)
        cmds.rotate(0, 0, 0 , os=True)
        cmds.parent(trs ,w = True)

    def sameName_check_func(self,check_node):
        if cmds.objExists(check_node):
            cmds.error("It has the same name. Please change the name")
        else:
            pass

#Single Function
    def degresslinear_create_curve(self,points,name):
        knot=list(range(len(points)))
        previousCurve=cmds.curve(d=1,per=True,p=points,k=knot)
        curve=cmds.rename(previousCurve,name)
        return curve

    def degresscubic_create_curve(self,points,name):
        knot=list(range(len(points)+2))
        previousCurve=cmds.curve(d=3,per=True,p=points,k=knot)
        curve=cmds.rename(previousCurve,name)
        return curve

    def parentcurve_create_curve(self,curves,name):
        curve=cmds.createNode("transform",n=name)
        for curve_trs in curves:
            print(curves)
            shape=cmds.listRelatives(curve_trs)
            cmds.parent(shape,curve,r=True,s=True)
            cmds.delete(curve_trs)
            cmds.select(cl=True)
        return curve

    def linecurve_create_curve(self,points,name):
        previousCurve=cmds.curve(d=1,p=points)
        curve=cmds.rename(previousCurve,name)
        return curve

    #Plane
    def circlePlane_create_curve(self,name,stroke=4):
        pizza=0.5/stroke
        points=[]
        for i in range(stroke*4):
            vartex=(0,math.cos(math.pi*(pizza*i)),math.sin(math.pi*(pizza*i)))
            points.append(vartex)
        points.append((0,1,0))
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def circleSmooth_create_curve(self,name,stroke=2):
        pizza=0.5/stroke
        points=[]
        for i in range(stroke*4+3):
            vartex=(0,math.cos(math.pi*(pizza*i))*1.1,math.sin(math.pi*(pizza*i))*1.1)
            points.append(vartex)
        curve=self.degresscubic_create_curve(points,name)
        return curve

    def circlePlaneHalf_create_curve(self,name):
        a00=(0,1.07,0)
        a01=(0,0.86,-0.63)
        a02=(0,0.33,-1.02)
        a03=(0,0,-1)
        a04=(0,0,-0.95)
        a05=(0,0,0)
        a06=(0,0,0.95)
        a07=(0,0,1)
        a08=(0,0.33,1.02)
        a09=(0,0.86,0.63)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a00,a01,a02]
        curve=self.degresscubic_create_curve(points,name)
        return curve

    def trianglePlane_create_curve(self,name):
        a00=(1,0,0)
        a01=(-1,0,1)
        a02=(-1,0,-1)
        points=[a00,a01,a02,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def featherPlane_create_curve(self,name):
        a00=(1,0,0)
        a01=(0.5,0,0.5)
        a02=(0,0,0.78)
        a03=(-1,0,1)
        a04=(-0.5,0,0)
        a05=(-1,0,-1)
        a06=(0,0,-0.78)
        a07=(0.5,0,-0.5)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve
    
    def featherSmooth_create_curve(self,name):
        a00=(1.05,0,0)
        a01=(0.8,0,0.2)
        a02=(0,0,0.75)
        a03=(-0.8,0,1)
        a04=(-1,0,1)
        a05=(-1,0,0.8)
        a06=(-0.8,0,0)
        a07=(-1,0,-0.8)
        a08=(-1,0,-1)
        a09=(-0.8,0,-1)
        a10=(0,0,-0.75)
        a11=(0.8,0,-0.2)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a00,a01,a02]
        curve=self.degresscubic_create_curve(points,name)
        return curve

    def squarePlane_create_curve(self,name):
        a00=(1,0,1)
        a01=(-1,0,1)
        a02=(-1,0,-1)
        a03=(1,0,-1)
        points=[a00,a01,a02,a03,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def squareSmooth_create_curve(self,name):
        a00=(0.85,0,-1)
        a01=(0.95,0,-0.95)
        a02=(1,0,-0.85)
        a03=(1,0,0.85)
        a04=(0.95,0,0.95)
        a05=(0.85,0,1)
        a06=(-0.85,0,1)
        a07=(-0.95,0,0.95)
        a08=(-1,0,0.85)
        a09=(-1,0,-0.85)
        a10=(-0.95,0,-0.95)
        a11=(-0.85,0,-1)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a00,a01,a02]
        curve=self.degresscubic_create_curve(points,name)
        return curve

    def crossPlane_create_curve(self,name):
        a00=(0.25,0,-1)
        a01=(0.25,0,-0.25)
        a02=(1,0,-0.25)
        a03=(1,0,0.25)
        a04=(0.25,0,0.25)
        a05=(0.25,0,1)
        a06=(-0.25,0,1)
        a07=(-0.25,0,0.25)
        a08=(-1,0,0.25)
        a09=(-1,0,-0.25)
        a10=(-0.25,0,-0.25)
        a11=(-0.25,0,-1)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def crossSmooth_create_curve(self,name):
        a00=(0.35,0,-1)
        a01=(0.4,0,-1)
        a02=(0.4,0,-0.95)
        a03=(0.4,0,-0.45)
        a04=(0.4,0,-0.4)
        a05=(0.45,0,-0.4)
        a06=(0.95,0,-0.4)
        a07=(1,0,-0.4)
        a08=(1,0,-0.35)
        a09=(1,0,0.35)
        a10=(1,0,0.4)
        a11=(0.95,0,0.4)
        a12=(0.45,0,0.4)
        a13=(0.4,0,0.4)
        a14=(0.4,0,0.45)
        a15=(0.4,0,0.95)
        a16=(0.4,0,1)
        a17=(0.35,0,1)
        a18=(-0.35,0,1)
        a19=(-0.4,0,1)
        a20=(-0.4,0,0.95)
        a21=(-0.4,0,0.45)
        a22=(-0.4,0,0.4)
        a23=(-0.45,0,0.4)
        a24=(-0.95,0,0.4)
        a25=(-1,0,0.4)
        a26=(-1,0,0.35)
        a27=(-1,0,-0.35)
        a28=(-1,0,-0.4)
        a29=(-0.95,0,-0.4)
        a30=(-0.45,0,-0.4)
        a31=(-0.4,0,-0.4)
        a32=(-0.4,0,-0.45)
        a33=(-0.4,0,-0.95)
        a34=(-0.4,0,-1)
        a35=(-0.35,0,-1)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a00,a01,a02]
        curve=self.degresscubic_create_curve(points,name)
        return curve

    def pentagonPlane_create_curve(self,name):
        a00=(1,0,0)
        a01=(0.18,0,1)
        a02=(-1,0,0.62)
        a03=(-1,0,-0.62)
        a04=(0.18,0,-1)
        points=[a00,a01,a02,a03,a04,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def hexagonPlane_create_curve(self,name):
        a00=(1,0,0)
        a01=(0.5,0,0.87)
        a02=(-0.5,0,0.87)
        a03=(-1,0,0)
        a04=(-0.5,0,-0.87)
        a05=(0.5,0,-0.87)
        points=[a00,a01,a02,a03,a04,a05,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def starPlane_create_curve(self,name):
        a00=(1,0,0)
        a01=(0.18,0,1)
        a02=(-1,0,0.62)
        a03=(-1,0,-0.62)
        a04=(0.18,0,-1)
        points=[a00,a03,a01,a04,a02,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def starSmooth_create_curve(self,name):
        a00=(1,0,0)
        a01=(0.9,0,0.03)
        a02=(0.23,0,0.23)
        a03=(0.18,0,0.25)
        a04=(0.18,0,0.3)
        a05=(0.18,0,0.9)
        a06=(0.18,0,1)
        a07=(0.1,0,0.9)
        a08=(-0.22,0,0.43)
        a09=(-0.26,0,0.39)
        a10=(-0.32,0,0.4)
        a11=(-0.92,0,0.6)
        a12=(-1,0,0.62)
        a13=(-0.95,0,0.55)
        a14=(-0.58,0,0.05)
        a15=(-0.55,0,0)
        a16=(-0.58,0,-0.05)
        a17=(-0.95,0,-0.55)
        a18=(-1,0,-0.62)
        a19=(-0.92,0,-0.6)
        a20=(-0.32,0,-0.4)
        a21=(-0.26,0,-0.39)
        a22=(-0.22,0,-0.43)
        a23=(0.1,0,-0.9)
        a24=(0.18,0,-1)
        a25=(0.18,0,-0.9)
        a26=(0.18,0,-0.3)
        a27=(0.18,0,-0.25)
        a28=(0.23,0,-0.23)
        a29=(0.9,0,-0.03)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a00,a01,a02]
        curve=self.degresscubic_create_curve(points,name)
        return curve

    def pinPlane_create_curve(self,name):
        a00=(0,0,0)
        a01=(0,1,0)
        a02=(-0.35,1.15,0)
        a03=(-0.5,1.5,0)
        a04=(-0.35,1.85,0)
        a05=(0,2,0)
        a06=(0.35,1.85,0)
        a07=(0.5,1.5,0)
        a08=(0.35,1.15,0)
        points=[a00,a05,a06,a07,a03,a04,a05,a01,a02,a03,a07,a08,a01,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def antennaPlane_create_curve(self,name):
        a00=(0,0.95,0)
        a01=(-0.4,1.1,0)
        a02=(-0.55,1.5,0)
        a03=(-0.4,1.9,0)
        a04=(0,2.05,0)
        a05=(0.4,1.9,0)
        a06=(0.55,1.5,0)
        a07=(0.4,1.1,0)
        b00=(0,0,0)
        b01=(0,2,0)
        c00=(-0.5,1.5,0)
        c01=(0.5,1.5,0)
        pointAs=[a00,a01,a02,a03,a04,a05,a06,a07,a00,a01,a02]
        pointBs=[b00,b01]
        pointCs=[c00,c01]
        curveA=self.degresscubic_create_curve(pointAs,name=name+"1")
        curveB=self.linecurve_create_curve(pointBs,name=name+"2")
        curveC=self.linecurve_create_curve(pointCs,name=name+"3")
        curves=[curveA,curveB,curveC]
        curve=self.parentcurve_create_curve(curves=curves,name=name)
        return curve

    #Solid
    def cubeSolid_create_curve(self,name):
        a01=(1,1,1)
        a02=(1,1,-1)
        a03=(-1,1,-1)
        a04=(-1,1,1)
        b01=(1,-1,1)
        b02=(1,-1,-1)
        b03=(-1,-1,-1)
        b04=(-1,-1,1)
        points=[a01,a02,a03,a04,a01,b01,b02,a02,b02,b03,a03,b03,b04,a04,b04,b01,a01]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def ballSolid_create_curve(self,name,stroke=4):
        pizza=0.5/stroke
        points=[]
        for i in range(stroke*4):
            vartex=(0,math.cos(math.pi*(pizza*i)),math.sin(math.pi*(pizza*i)))
            points.append(vartex)
        for i in range(stroke*1):
            vartex=(math.sin(math.pi*(pizza*i)),math.cos(math.pi*(pizza*i)),0)
            points.append(vartex)
        for i in range(stroke*4):
            vartex=(math.cos(math.pi*(pizza*i)),0,math.sin(math.pi*(pizza*i)))
            points.append(vartex)
        for i in range(stroke*3):
            vartex=(math.sin(math.pi*((pizza*i)+pizza*stroke)),math.cos(math.pi*((pizza*i)+pizza*stroke)),0)
            points.append(vartex)
        points.append((0,1,0))
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def ballSmooth_create_curve(self,name,stroke=2):
        pizza=0.5/stroke
        pointZYs=[]
        pointXYs=[]
        pointZXs=[]
        for i in range(stroke*4+3):
            vartex=(0,math.cos(math.pi*(pizza*i))*1.1,math.sin(math.pi*(pizza*i))*1.1)
            pointZYs.append(vartex)
        for i in range(stroke*4+3):
            vartex=(math.sin(math.pi*(pizza*i))*1.1,math.cos(math.pi*(pizza*i))*1.1,0)
            pointXYs.append(vartex)
        for i in range(stroke*4+3):
            vartex=(math.cos(math.pi*(pizza*i))*1.1,0,math.sin(math.pi*(pizza*i))*1.1)
            pointZXs.append(vartex)
        curveZY=self.degresscubic_create_curve(pointZYs,name=name+"1")
        curveXY=self.degresscubic_create_curve(pointXYs,name=name+"2")
        curveZX=self.degresscubic_create_curve(pointZXs,name=name+"3")
        curves=[curveZY,curveXY,curveZX]
        curve=self.parentcurve_create_curve(curves=curves,name=name)
        return curve

    def ballSolidHalf_create_curve(self,name):
        a00=(1,0,0)
        a01=(0.92,0,0.38)
        a02=(0.71,0,0.71)
        a03=(0.38,0,0.92)
        a04=(0,0,1)
        a05=(-0.38,0,0.92)
        a06=(-0.71,0,0.71)
        a07=(-0.92,0,0.38)
        a08=(-1,0,0)
        a09=(-0.92,0,-0.38)
        a10=(-0.71,0,-0.71)
        a11=(-0.38,0,-0.92)
        a12=(0,0,-1)
        a13=(0.38,0,-0.92)
        a14=(0.71,0,-0.71)
        a15=(0.92,0,-0.38)
        xy00=(0,1,0)
        x00=(0.92,0.38,0)
        x01=(0.71,0.71,0)
        x02=(0.38,0.92,0)
        x03=(-0.38,0.92,0)
        x04=(-0.71,0.71,0)
        x05=(-0.92,0.38,0)
        z00=(0,0.38,0.92)
        z01=(0,0.71,0.71)
        z02=(0,0.92,0.38)
        z03=(0,0.92,-0.38)
        z04=(0,0.71,-0.71)
        z05=(0,0.38,-0.92)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a00,x00,x01,x02,xy00,z02,z01,z00,a04,z00,z01,z02,xy00,x03,x04,x05,a08,x05,x04,x03,xy00,z03,z04,z05,a12,z05,z04,z03,xy00,x02,x01,x00,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def hexagonSolid_create_curve(self,name):
        a01=(0,-1,0)
        a02=(0,-0.5,0.87)
        a03=(0,0.5,0.87)
        a04=(0,1,0)
        a05=(0,0.5,-0.87)
        a06=(0,-0.5,-0.87)
        b01=(2,-1,0)
        b02=(2,-0.5,0.87)
        b03=(2,0.5,0.87)
        b04=(2,1,0)
        b05=(2,0.5,-0.87)
        b06=(2,-0.5,-0.87)
        points=[a01,a02,a03,a04,a05,a06,a01,b01,b02,a02,b02,b03,a03,b03,b04,a04,b04,b05,a05,b05,b06,a06,b06,b01,a01]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def octagonSolid_create_curve(self,name):
        a01=(0,-1,0)
        a02=(0,-0.71,0.71)
        a03=(0,0,1)
        a04=(0,0.71,0.71)
        a05=(0,1,0)
        a06=(0,0.71,-0.71)
        a07=(0,0,-1)
        a08=(0,-0.71,-0.71)
        b01=(2,-1,0)
        b02=(2,-0.71,0.71)
        b03=(2,0,1)
        b04=(2,0.71,0.71)
        b05=(2,1,0)
        b06=(2,0.71,-0.71)
        b07=(2,0,-1)
        b08=(2,-0.71,-0.71)
        points=[a01,a02,a03,a04,a05,a06,a07,a08,a01,b01,b02,a02,b02,b03,a03,b03,b04,a04,b04,b05,a05,b05,b06,a06,b06,b07,a07,b07,b08,a08,b08,b01,a01]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def diamondSolid_create_curve(self,name):
        xu=(1,0,0)
        xd=(-1,0,0)
        yu=(0,1,0)
        yd=(0,-1,0)
        zu=(0,0,1)
        zd=(0,0,-1)
        points=[xu,zd,xd,zu,xu,yu,xd,yd,xu,zd,yu,zu,yd,zd,xu]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def pyramidSolid_create_curve(self,name):
        a00=(2,0,0)
        a01=(0,0,1)
        a02=(0,1,0)
        a03=(0,0,-1)
        a04=(0,-1,0)
        points=[a00,a01,a02,a03,a04,a01,a00,a02,a00,a03,a00,a04,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def coneSolid_create_curve(self,name):
        a00=(2,0,0)
        a01=(0,0,1)
        a02=(0,0.87,0.5)
        a03=(0,0.87,-0.5)
        a04=(0,0,-1)
        a05=(0,-0.87,-0.5)
        a06=(0,-0.87,0.5)
        points=[a00,a01,a02,a03,a04,a05,a06,a01,a00,a02,a00,a03,a00,a04,a00,a05,a00,a06,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def pinSolid_create_curve(self,name):
        a00=(0,0,0)
        a01=(0,1,0)
        a02=(-0.35,1.15,0)
        a03=(-0.5,1.5,0)
        a04=(-0.35,1.85,0)
        a05=(0,2,0)
        a06=(0.35,1.85,0)
        a07=(0.5,1.5,0)
        a08=(0.35,1.15,0)
        a09=(0,1.15,-0.35)
        a10=(0,1.5,-0.5)
        a11=(0,1.85,-0.35)
        a12=(0,1.85,0.35)
        a13=(0,1.5,0.5)
        a14=(0,1.15,0.35)
        a15=(0.35,1.5,0.35)
        a16=(-0.35,1.5,0.35)
        a17=(-0.35,1.5,-0.35)
        a18=(0.35,1.5,-0.35)
        points=[a00,a05,a06,a07,a03,a04,a05,a01,a02,a03,a07,a08,a01,a09,a10,a13,a14,a01,a05,a12,a13,a10,a18,a07,a15,a13,a16,a03,a17,a10,a11,a05,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def antennaSolid_create_curve(self,name):
        a00=(0,0.95,0)
        a01=(-0.4,1.1,0)
        a02=(-0.55,1.5,0)
        a03=(-0.4,1.9,0)
        a04=(0,2.05,0)
        a05=(0.4,1.9,0)
        a06=(0.55,1.5,0)
        a07=(0.4,1.1,0)
        b00=(0,0,0)
        b01=(0,2,0)
        d00=(0,0.95,0)
        d01=(0,1.1,-0.4)
        d02=(0,1.5,-0.55)
        d03=(0,1.9,-0.4)
        d04=(0,2.05,0)
        d05=(0,1.9,0.4)
        d06=(0,1.5,0.55)
        d07=(0,1.1,0.4)
        e00=(0.55,1.5,0)
        e01=(0.4,1.5,0.4)
        e02=(0,1.5,0.55)
        e03=(-0.4,1.5,0.4)
        e04=(-0.55,1.5,0)
        e05=(-0.4,1.5,-0.4)
        e06=(0,1.5,-0.55)
        e07=(0.4,1.5,-0.4)
        pointAs=[a00,a01,a02,a03,a04,a05,a06,a07,a00,a01,a02]
        pointDs=[d00,d01,d02,d03,d04,d05,d06,d07,d00,d01,d02]
        pointEs=[e00,e01,e02,e03,e04,e05,e06,e07,e00,e01,e02]
        pointBs=[b00,b01]
        curveA=self.degresscubic_create_curve(pointAs,name=name+"1")
        curveB=self.linecurve_create_curve(pointBs,name=name+"4")
        curveD=self.degresscubic_create_curve(pointDs,name=name+"2")
        curveE=self.degresscubic_create_curve(pointEs,name=name+"3")
        curves=[curveA,curveD,curveE,curveB]
        curve=self.parentcurve_create_curve(curves=curves,name=name)
        return curve

    def circleCurve_create_curve(self,name):
        a00=(0.3,1,0)
        a01=(0.25,0.75,-0.78)
        a02=(0,-0.25,-1)
        a03=(-0.25,0.75,-0.78)
        a04=(-0.3,1,0)
        a05=(-0.25,0.75,0.78)
        a06=(0,-0.25,1)
        a07=(0.25,0.75,0.78)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a00,a01,a02]
        curve=self.degresscubic_create_curve(points,name)
        return curve

    #Arrows
    def singleArrow_create_curve(self,name):
        a00=(1,0,0)
        a01=(0,0,-1)
        a02=(0,0,-0.5)
        a03=(-1,0,-0.5)
        a04=(-1,0,0.5)
        a05=(0,0,0.5)
        a06=(0,0,1)
        points=[a00,a01,a02,a03,a04,a05,a06,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def doubleArrow_create_curve(self,name):
        a00=(1,0,0)
        a01=(0.4,0,0.6)
        a02=(0.4,0,0.2)
        a03=(0.2,0,0.2)
        a04=(0,0,0.2)
        a05=(-0.2,0,0.2)
        a06=(-0.4,0,0.2)
        a07=(-0.4,0,0.6)
        a08=(-1,0,0)
        a09=(-0.4,0,-0.6)
        a10=(-0.4,0,-0.2)
        a11=(-0.2,0,-0.2)
        a12=(0,0,-0.2)
        a13=(0.2,0,-0.2)
        a14=(0.4,0,-0.2)
        a15=(0.4,0,-0.6)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def fourArrow_create_curve(self,name):
        a00=(1,0,0)
        a01=(0.6,0,0.4)
        a02=(0.6,0,0.2)
        a03=(0.2,0,0.2)
        a04=(0.2,0,0.6)
        a05=(0.4,0,0.6)
        a06=(0,0,1)
        a07=(-0.4,0,0.6)
        a08=(-0.2,0,0.6)
        a09=(-0.2,0,0.2)
        a10=(-0.6,0,0.2)
        a11=(-0.6,0,0.4)
        a12=(-1,0,0)
        a13=(-0.6,0,-0.4)
        a14=(-0.6,0,-0.2)
        a15=(-0.2,0,-0.2)
        a16=(-0.2,0,-0.6)
        a17=(-0.4,0,-0.6)
        a18=(0,0,-1)
        a19=(0.4,0,-0.6)
        a20=(0.2,0,-0.6)
        a21=(0.2,0,-0.2)
        a22=(0.6,0,-0.2)
        a23=(0.6,0,-0.4)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def smoothFour_create_curve(self,name):
        a00=(0,1.03,0)
        a01=(0,0.92,-0.12)
        a02=(0,0.8,-0.23)
        a03=(0,0.69,-0.35)
        a04=(0,0.69,-0.29)
        a05=(0,0.69,-0.23)
        a06=(0,0.69,-0.17)
        a07=(0,0.65,-0.17)
        a08=(0,0.6,-0.17)
        a09=(0,0.56,-0.17)
        a10=(0,0.53,-0.27)
        a11=(0,0.43,-0.43)
        a12=(0,0.27,-0.53)
        a13=(0,0.17,-0.56)
        a14=(0,0.17,-0.61)
        a15=(0,0.17,-0.65)
        a16=(0,0.17,-0.7)
        a17=(0,0.23,-0.7)
        a18=(0,0.29,-0.7)
        a19=(0,0.34,-0.7)
        a20=(0,0.23,-0.81)
        a21=(0,0.11,-0.93)
        a22=(0,0,-1.03)
        a23=(0,-0.11,-0.93)
        a24=(0,-0.34,-0.7)
        a25=(0,-0.29,-0.7)
        a26=(0,-0.23,-0.7)
        a27=(0,-0.17,-0.7)
        a28=(0,-0.17,-0.65)
        a29=(0,-0.17,-0.61)
        a30=(0,-0.17,-0.56)
        a31=(0,-0.27,-0.53)
        a32=(0,-0.43,-0.43)
        a33=(0,-0.53,-0.27)
        a34=(0,-0.56,-0.17)
        a35=(0,-0.6,-0.17)
        a36=(0,-0.65,-0.17)
        a37=(0,-0.69,-0.17)
        a38=(0,-0.69,-0.23)
        a39=(0,-0.69,-0.29)
        a40=(0,-0.69,-0.35)
        a41=(0,-0.8,-0.23)
        a42=(0,-0.92,-0.12)
        a43=(0,-1.03,0)
        a44=(0,-0.92,0.12)
        a45=(0,-0.8,0.23)
        a46=(0,-0.69,0.35)
        a47=(0,-0.69,0.29)
        a48=(0,-0.69,0.23)
        a49=(0,-0.69,0.17)
        a50=(0,-0.65,0.17)
        a51=(0,-0.6,0.17)
        a52=(0,-0.56,0.17)
        a53=(0,-0.53,0.27)
        a54=(0,-0.43,0.43)
        a55=(0,-0.27,0.53)
        a56=(0,-0.17,0.56)
        a57=(0,-0.17,0.61)
        a58=(0,-0.17,0.65)
        a59=(0,-0.17,0.7)
        a60=(0,-0.23,0.7)
        a61=(0,-0.29,0.7)
        a62=(0,-0.34,0.7)
        a63=(0,-0.11,0.93)
        a64=(0,0,1.03)
        a65=(0,0.11,0.93)
        a66=(0,0.23,0.81)
        a67=(0,0.34,0.7)
        a68=(0,0.29,0.7)
        a69=(0,0.23,0.7)
        a70=(0,0.17,0.7)
        a71=(0,0.17,0.65)
        a72=(0,0.17,0.61)
        a73=(0,0.17,0.56)
        a74=(0,0.27,0.53)
        a75=(0,0.43,0.43)
        a76=(0,0.53,0.27)
        a77=(0,0.56,0.17)
        a78=(0,0.6,0.17)
        a79=(0,0.65,0.17)
        a80=(0,0.69,0.17)
        a81=(0,0.69,0.23)
        a82=(0,0.69,0.29)
        a83=(0,0.69,0.35)
        a84=(0,0.8,0.23)
        a85=(0,0.92,0.12)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72,a73,a74,a75,a76,a77,a78,a79,a80,a81,a82,a83,a84,a85,a00,a01,a02]
        curve=self.degresscubic_create_curve(points,name)
        return curve

    def rightAngleArrow_create_curve(self,name):
        a00=(0.66,0.58,0)
        a01=(0.15,0.52,0)
        a02=(0.41,0.64,0)
        a03=(0.34,0.67,0)
        a04=(0.17,0.73,0)
        a05=(-0.09,0.75,0)
        a06=(-0.35,0.69,0)
        a07=(-0.58,0.57,0)
        a08=(-0.64,0.65,0)
        a09=(-0.38,0.79,0)
        a10=(-0.1,0.85,0)
        a11=(0.19,0.83,0)
        a12=(0.37,0.77,0)
        a13=(0.46,0.72,0)
        a14=(0.34,0.98,0)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def rotArrow_create_curve(self,name):
        points=[
            (-7.45058e-009,0,0.5),
            (0.11126,0,0.487464),
            (0.216942,0,0.450484),
            (0.311745,0,0.390916),
            (0.390916,0,0.311745),
            (0.450484,0,0.216942),
            (0.487464,0,0.11126),
            (0.5,0,0),
            (0.487464,0,-0.11126),
            (0.450484,0,-0.216942),
            (0.390916,0,-0.311745),
            (0.311745,0,-0.390916),
            (0.216942,0,-0.450484),
            (0.11126,0,-0.487464),
            (2.23517e-008,0,-0.5),
            (-0.11126,0,-0.487464),
            (-0.216942,0,-0.450484),
            (-0.311745,0,-0.390916),
            (-0.390916,0,-0.311745),
            (-0.450484,0,-0.216942),
            (-0.487464,0,-0.11126),
            (-0.5,0,-2.23517e-008),
            (-0.601241,0,0),
            (-0.416241,0,0.31218),
            (-0.231241,0,0),
            (-0.333,0,-1.48863e-008),
            (-0.324651,0,-0.0740995),
            (-0.300023,0,-0.144483),
            (-0.26035,0,-0.207622),
            (-0.207622,0,-0.26035),
            (-0.144483,0,-0.300023),
            (-0.0740994,0,-0.324651),
            (1.48863e-008,0,-0.333),
            (0.0740995,0,-0.324651),
            (0.144483,0,-0.300023),
            (0.207622,0,-0.26035),
            (0.26035,0,-0.207622),
            (0.300023,0,-0.144483),
            (0.324651,0,-0.0740994),
            (0.333,0,0),
            (0.324651,0,0.0740995),
            (0.300023,0,0.144483),
            (0.26035,0,0.207622),
            (0.207622,0,0.26035),
            (0.144483,0,0.300023),
            (0.0740995,0,0.324651),
            (-4.96209e-009,0,0.333),
            (-7.45058e-009,0,0.5)
            ]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def archArrow_create_curve(self,name):
        a00=(0,1,0)
        a01=(0.28,0.96,0)
        a02=(0.54,0.85,0)
        a03=(0.76,0.67,0)
        a04=(0.87,0.52,0)
        a05=(0.91,0.43,0)
        a06=(0.96,0.7,0)
        a07=(1,0.2,0)
        a08=(0.56,0.45,0)
        a09=(0.83,0.39,0)
        a10=(0.79,0.46,0)
        a11=(0.69,0.6,0)
        a12=(0.49,0.76,0)
        a13=(0.25,0.86,0)
        a14=(0,0.9,0)
        a15=(-0.25,0.86,0)
        a16=(-0.49,0.76,0)
        a17=(-0.69,0.6,0)
        a18=(-0.79,0.46,0)
        a19=(-0.83,0.39,0)
        a20=(-0.56,0.45,0)
        a21=(-1,0.2,0)
        a22=(-0.96,0.7,0)
        a23=(-0.91,0.43,0)
        a24=(-0.87,0.52,0)
        a25=(-0.76,0.67,0)
        a26=(-0.54,0.85,0)
        a27=(-0.28,0.96,0)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def ballArrow_create_curve(self,name):
        a00=(1,0.35,0)
        a01=(0.75,0.68,0.34)
        a02=(0.75,0.68,0.1)
        a03=(0.5,0.85,0.1)
        a04=(0.1,0.95,0.1)
        a05=(0.1,0.85,0.5)
        a06=(0.1,0.68,0.75)
        a07=(0.34,0.68,0.75)
        a08=(0,0.35,1)
        a09=(-0.34,0.68,0.75)
        a10=(-0.1,0.68,0.75)
        a11=(-0.1,0.85,0.5)
        a12=(-0.1,0.95,0.1)
        a13=(-0.5,0.85,0.1)
        a14=(-0.75,0.68,0.1)
        a15=(-0.75,0.68,0.34)
        a16=(-1,0.35,0)
        a17=(-0.75,0.68,-0.34)
        a18=(-0.75,0.68,-0.1)
        a19=(-0.5,0.85,-0.1)
        a20=(-0.1,0.95,-0.1)
        a21=(-0.1,0.85,-0.5)
        a22=(-0.1,0.68,-0.75)
        a23=(-0.34,0.68,-0.75)
        a24=(0,0.35,-1)
        a25=(0.34,0.68,-0.75)
        a26=(0.1,0.68,-0.75)
        a27=(0.1,0.85,-0.5)
        a28=(0.1,0.95,-0.1)
        a29=(0.5,0.85,-0.1)
        a30=(0.75,0.68,-0.1)
        a31=(0.75,0.68,-0.34)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def solidArrow_create_curve(self,name):
        a00=(1,0,0)
        a01=(0,1,1)
        a02=(0,1,-1)
        a03=(0,-1,-1)
        a04=(0,-1,1)
        a05=(0,0.5,0.5)
        a06=(0,0.5,-0.5)
        a07=(0,-0.5,-0.5)
        a08=(0,-0.5,0.5)
        a09=(-1,0.5,0.5)
        a10=(-1,0.5,-0.5)
        a11=(-1,-0.5,-0.5)
        a12=(-1,-0.5,0.5)
        points=[a00,a01,a05,a09,a10,a11,a12,a09,a05,a06,a10,a06,a02,a06,a07,a11,a07,a03,a07,a08,a12,a08,a05,a08,a04,a03,a02,a01,a04,a00,a03,a00,a02,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def solidFour_create_curve(self,name):
        a00=(0,1.03,0)
        a01=(0,0.92,-0.12)
        a02=(0,0.8,-0.23)
        a03=(0,0.69,-0.35)
        a04=(0,0.69,-0.29)
        a05=(0,0.69,-0.23)
        a06=(0,0.69,-0.17)
        a07=(0,0.65,-0.17)
        a08=(0,0.6,-0.17)
        a09=(0,0.56,-0.17)
        a10=(0,0.53,-0.27)
        a11=(0,0.43,-0.43)
        a12=(0,0.27,-0.53)
        a13=(0,0.17,-0.56)
        a14=(0,0.17,-0.61)
        a15=(0,0.17,-0.65)
        a16=(0,0.17,-0.7)
        a17=(0,0.23,-0.7)
        a18=(0,0.29,-0.7)
        a19=(0,0.34,-0.7)
        a20=(0,0.23,-0.81)
        a21=(0,0.11,-0.93)
        a22=(0,0,-1.03)
        a23=(0,-0.11,-0.93)
        a24=(0,-0.34,-0.7)
        a25=(0,-0.29,-0.7)
        a26=(0,-0.23,-0.7)
        a27=(0,-0.17,-0.7)
        a28=(0,-0.17,-0.65)
        a29=(0,-0.17,-0.61)
        a30=(0,-0.17,-0.56)
        a31=(0,-0.27,-0.53)
        a32=(0,-0.43,-0.43)
        a33=(0,-0.53,-0.27)
        a34=(0,-0.56,-0.17)
        a35=(0,-0.6,-0.17)
        a36=(0,-0.65,-0.17)
        a37=(0,-0.69,-0.17)
        a38=(0,-0.69,-0.23)
        a39=(0,-0.69,-0.29)
        a40=(0,-0.69,-0.35)
        a41=(0,-0.8,-0.23)
        a42=(0,-0.92,-0.12)
        a43=(0,-1.03,0)
        a44=(0,-0.92,0.12)
        a45=(0,-0.8,0.23)
        a46=(0,-0.69,0.35)
        a47=(0,-0.69,0.29)
        a48=(0,-0.69,0.23)
        a49=(0,-0.69,0.17)
        a50=(0,-0.65,0.17)
        a51=(0,-0.6,0.17)
        a52=(0,-0.56,0.17)
        a53=(0,-0.53,0.27)
        a54=(0,-0.43,0.43)
        a55=(0,-0.27,0.53)
        a56=(0,-0.17,0.56)
        a57=(0,-0.17,0.61)
        a58=(0,-0.17,0.65)
        a59=(0,-0.17,0.7)
        a60=(0,-0.23,0.7)
        a61=(0,-0.29,0.7)
        a62=(0,-0.34,0.7)
        a63=(0,-0.11,0.93)
        a64=(0,0,1.03)
        a65=(0,0.11,0.93)
        a66=(0,0.23,0.81)
        a67=(0,0.34,0.7)
        a68=(0,0.29,0.7)
        a69=(0,0.23,0.7)
        a70=(0,0.17,0.7)
        a71=(0,0.17,0.65)
        a72=(0,0.17,0.61)
        a73=(0,0.17,0.56)
        a74=(0,0.27,0.53)
        a75=(0,0.43,0.43)
        a76=(0,0.53,0.27)
        a77=(0,0.56,0.17)
        a78=(0,0.6,0.17)
        a79=(0,0.65,0.17)
        a80=(0,0.69,0.17)
        a81=(0,0.69,0.23)
        a82=(0,0.69,0.29)
        a83=(0,0.69,0.35)
        a84=(0,0.8,0.23)
        a85=(0,0.92,0.12)
        pointZYs=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72,a73,a74,a75,a76,a77,a78,a79,a80,a81,a82,a83,a84,a85,a00,a01,a02]
        b00=(1.03,0,0)
        b01=(0.92,0,-0.12)
        b02=(0.8,0,-0.23)
        b03=(0.69,0,-0.35)
        b04=(0.69,0,-0.29)
        b05=(0.69,0,-0.23)
        b06=(0.69,0,-0.17)
        b07=(0.65,0,-0.17)
        b08=(0.6,0,-0.17)
        b09=(0.56,0,-0.17)
        b10=(0.53,0,-0.27)
        b11=(0.43,0,-0.43)
        b12=(0.27,0,-0.53)
        b13=(0.17,0,-0.56)
        b14=(0.17,0,-0.61)
        b15=(0.17,0,-0.65)
        b16=(0.17,0,-0.7)
        b17=(0.23,0,-0.7)
        b18=(0.29,0,-0.7)
        b19=(0.34,0,-0.7)
        b20=(0.23,0,-0.81)
        b21=(0.11,0,-0.93)
        b22=(0,0,-1.03)
        b23=(-0.11,0,-0.93)
        b24=(-0.34,0,-0.7)
        b25=(-0.29,0,-0.7)
        b26=(-0.23,0,-0.7)
        b27=(-0.17,0,-0.7)
        b28=(-0.17,0,-0.65)
        b29=(-0.17,0,-0.61)
        b30=(-0.17,0,-0.56)
        b31=(-0.27,0,-0.53)
        b32=(-0.43,0,-0.43)
        b33=(-0.53,0,-0.27)
        b34=(-0.56,0,-0.17)
        b35=(-0.6,0,-0.17)
        b36=(-0.65,0,-0.17)
        b37=(-0.69,0,-0.17)
        b38=(-0.69,0,-0.23)
        b39=(-0.69,0,-0.29)
        b40=(-0.69,0,-0.35)
        b41=(-0.8,0,-0.23)
        b42=(-0.92,0,-0.12)
        b43=(-1.03,0,0)
        b44=(-0.92,0,0.12)
        b45=(-0.8,0,0.23)
        b46=(-0.69,0,0.35)
        b47=(-0.69,0,0.29)
        b48=(-0.69,0,0.23)
        b49=(-0.69,0,0.17)
        b50=(-0.65,0,0.17)
        b51=(-0.6,0,0.17)
        b52=(-0.56,0,0.17)
        b53=(-0.53,0,0.27)
        b54=(-0.43,0,0.43)
        b55=(-0.27,0,0.53)
        b56=(-0.17,0,0.56)
        b57=(-0.17,0,0.61)
        b58=(-0.17,0,0.65)
        b59=(-0.17,0,0.7)
        b60=(-0.23,0,0.7)
        b61=(-0.29,0,0.7)
        b62=(-0.34,0,0.7)
        b63=(-0.11,0,0.93)
        b64=(0,0,1.03)
        b65=(0.11,0,0.93)
        b66=(0.23,0,0.81)
        b67=(0.34,0,0.7)
        b68=(0.29,0,0.7)
        b69=(0.23,0,0.7)
        b70=(0.17,0,0.7)
        b71=(0.17,0,0.65)
        b72=(0.17,0,0.61)
        b73=(0.17,0,0.56)
        b74=(0.27,0,0.53)
        b75=(0.43,0,0.43)
        b76=(0.53,0,0.27)
        b77=(0.56,0,0.17)
        b78=(0.6,0,0.17)
        b79=(0.65,0,0.17)
        b80=(0.69,0,0.17)
        b81=(0.69,0,0.23)
        b82=(0.69,0,0.29)
        b83=(0.69,0,0.35)
        b84=(0.8,0,0.23)
        b85=(0.92,0,0.12)
        pointZXs=[b00,b01,b02,b03,b04,b05,b06,b07,b08,b09,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,b61,b62,b63,b64,b65,b66,b67,b68,b69,b70,b71,b72,b73,b74,b75,b76,b77,b78,b79,b80,b81,b82,b83,b84,b85,b00,b01,b02]
        c00=(1.03,0,0)
        c01=(0.92,-0.12,0)
        c02=(0.8,-0.23,0)
        c03=(0.69,-0.35,0)
        c04=(0.69,-0.29,0)
        c05=(0.69,-0.23,0)
        c06=(0.69,-0.17,0)
        c07=(0.65,-0.17,0)
        c08=(0.6,-0.17,0)
        c09=(0.56,-0.17,0)
        c10=(0.53,-0.27,0)
        c11=(0.43,-0.43,0)
        c12=(0.27,-0.53,0)
        c13=(0.17,-0.56,0)
        c14=(0.17,-0.61,0)
        c15=(0.17,-0.65,0)
        c16=(0.17,-0.7,0)
        c17=(0.23,-0.7,0)
        c18=(0.29,-0.7,0)
        c19=(0.34,-0.7,0)
        c20=(0.23,-0.81,0)
        c21=(0.11,-0.93,0)
        c22=(0,-1.03,0)
        c23=(-0.11,-0.93,0)
        c24=(-0.34,-0.7,0)
        c25=(-0.29,-0.7,0)
        c26=(-0.23,-0.7,0)
        c27=(-0.17,-0.7,0)
        c28=(-0.17,-0.65,0)
        c29=(-0.17,-0.61,0)
        c30=(-0.17,-0.56,0)
        c31=(-0.27,-0.53,0)
        c32=(-0.43,-0.43,0)
        c33=(-0.53,-0.27,0)
        c34=(-0.56,-0.17,0)
        c35=(-0.6,-0.17,0)
        c36=(-0.65,-0.17,0)
        c37=(-0.69,-0.17,0)
        c38=(-0.69,-0.23,0)
        c39=(-0.69,-0.29,0)
        c40=(-0.69,-0.35,0)
        c41=(-0.8,-0.23,0)
        c42=(-0.92,-0.12,0)
        c43=(-1.03,0,0)
        c44=(-0.92,0.12,0)
        c45=(-0.8,0.23,0)
        c46=(-0.69,0.35,0)
        c47=(-0.69,0.29,0)
        c48=(-0.69,0.23,0)
        c49=(-0.69,0.17,0)
        c50=(-0.65,0.17,0)
        c51=(-0.6,0.17,0)
        c52=(-0.56,0.17,0)
        c53=(-0.53,0.27,0)
        c54=(-0.43,0.43,0)
        c55=(-0.27,0.53,0)
        c56=(-0.17,0.56,0)
        c57=(-0.17,0.61,0)
        c58=(-0.17,0.65,0)
        c59=(-0.17,0.7,0)
        c60=(-0.23,0.7,0)
        c61=(-0.29,0.7,0)
        c62=(-0.34,0.7,0)
        c63=(-0.11,0.93,0)
        c64=(0,1.03,0)
        c65=(0.11,0.93,0)
        c66=(0.23,0.81,0)
        c67=(0.34,0.7,0)
        c68=(0.29,0.7,0)
        c69=(0.23,0.7,0)
        c70=(0.17,0.7,0)
        c71=(0.17,0.65,0)
        c72=(0.17,0.61,0)
        c73=(0.17,0.56,0)
        c74=(0.27,0.53,0)
        c75=(0.43,0.43,0)
        c76=(0.53,0.27,0)
        c77=(0.56,0.17,0)
        c78=(0.6,0.17,0)
        c79=(0.65,0.17,0)
        c80=(0.69,0.17,0)
        c81=(0.69,0.23,0)
        c82=(0.69,0.29,0)
        c83=(0.69,0.35,0)
        c84=(0.8,0.23,0)
        c85=(0.92,0.12,0)
        pointXYs=[c00,c01,c02,c03,c04,c05,c06,c07,c08,c09,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38,c39,c40,c41,c42,c43,c44,c45,c46,c47,c48,c49,c50,c51,c52,c53,c54,c55,c56,c57,c58,c59,c60,c61,c62,c63,c64,c65,c66,c67,c68,c69,c70,c71,c72,c73,c74,c75,c76,c77,c78,c79,c80,c81,c82,c83,c84,c85,c00,c01,c02]
        curveZY=self.degresscubic_create_curve(pointZYs,name=name+"1")
        curveZX=self.degresscubic_create_curve(pointZXs,name=name+"2")
        curveXY=self.degresscubic_create_curve(pointXYs,name=name+"3")
        curves=[curveZY,curveXY,curveZX]
        curve=self.parentcurve_create_curve(curves=curves,name=name)
        return curve

    #Other
    def cog_create_curve(self,name):
        a00=(0,1.25,0)
        a01=(0,0.47,-0.2)
        a02=(0,0.88,-0.88)
        a03=(0,0.2,-0.47)
        a04=(0,0,-1.25)
        a05=(0,-0.2,-0.47)
        a06=(0,-0.88,-0.88)
        a07=(0,-0.47,-0.2)
        a08=(0,-1.25,0)
        a09=(0,-0.47,0.2)
        a10=(0,-0.88,0.88)
        a11=(0,-0.2,0.47)
        a12=(0,0,1.25)
        a13=(0,0.2,0.47)
        a14=(0,0.88,0.88)
        a15=(0,0.47,0.2)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a00,a01,a02]
        curve=self.degresscubic_create_curve(points,name)
        return curve

    def thorns_create_curve(self,name):
        a00=(0,-1,0)
        a01=(0,-0.5,0.2)
        a02=(0,-0.7,0.7)
        a03=(0,-0.2,0.5)
        a04=(0,0,1)
        a05=(0,0.2,0.5)
        a06=(0,0.7,0.7)
        a07=(0,0.5,0.2)
        a08=(0,1,0)
        a09=(0,0.5,-0.2)
        a10=(0,0.7,-0.7)
        a11=(0,0.2,-0.5)
        a12=(0,0,-1)
        a13=(0,-0.2,-0.5)
        a14=(0,-0.7,-0.7)
        a15=(0,-0.5,-0.2)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a00]
        curve=self.degresslinear_create_curve(points,name)
        return curve

    def sun_create_curve(self,name):
        a00=(0,1.25,0)
        a01=(0,0.47,-0.2)
        a02=(0,0.88,-0.88)
        a03=(0,0.2,-0.47)
        a04=(0,0,-1.25)
        a05=(0,-0.2,-0.47)
        a06=(0,-0.88,-0.88)
        a07=(0,-0.47,-0.2)
        a08=(0,-1.25,0)
        a09=(0,-0.47,0.2)
        a10=(0,-0.88,0.88)
        a11=(0,-0.2,0.47)
        a12=(0,0,1.25)
        a13=(0,0.2,0.47)
        a14=(0,0.88,0.88)
        a15=(0,0.47,0.2)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a00,a01,a02] 
        curve_cog=self.degresscubic_create_curve(points,name=name+"1")
        
        pizza=0.5/2
        point_circle=[]
        for i in range(2*4+3):
            vartex=(0,math.cos(math.pi*(pizza*i))*1*0.7,math.sin(math.pi*(pizza*i))*1*0.7)
            point_circle.append(vartex)
        curve_circle=self.degresscubic_create_curve(point_circle,name=name+"2")

        curves=[curve_cog,curve_circle]
        curve=self.parentcurve_create_curve(curves=curves,name=name)
        return curve

    def gear_create_curve(self,name):
        c00=(0,1,-0.09)
        c01=(0,0.95,-0.26)
        c02=(0,0.92,-0.25)
        c03=(0,0.73,-0.2)
        c04=(0,0.7,-0.19)
        c05=(0,0.67,-0.31)
        c06=(0,0.6,-0.42)
        c07=(0,0.51,-0.51)
        c08=(0,0.53,-0.53)
        c09=(0,0.68,-0.68)
        c10=(0,0.7,-0.7)
        c11=(0,0.57,-0.83)
        c12=(0,0.42,-0.91)
        c13=(0,0.26,-0.95)
        c14=(0,0.25,-0.93)
        c15=(0,0.19,-0.73)
        c16=(0,0.19,-0.7)
        c17=(0,0.06,-0.73)
        c18=(0,-0.06,-0.73)
        c19=(0,-0.19,-0.7)
        c20=(0,-0.19,-0.73)
        c21=(0,-0.25,-0.93)
        c22=(0,-0.26,-0.95)
        c23=(0,-0.42,-0.91)
        c24=(0,-0.57,-0.83)
        c25=(0,-0.7,-0.7)
        c26=(0,-0.68,-0.68)
        c27=(0,-0.53,-0.53)
        c28=(0,-0.51,-0.51)
        c29=(0,-0.6,-0.42)
        c30=(0,-0.67,-0.31)
        c31=(0,-0.7,-0.19)
        c32=(0,-0.73,-0.2)
        c33=(0,-0.92,-0.25)
        c34=(0,-0.95,-0.26)
        c35=(0,-1,-0.09)
        c36=(0,-1,0.09)
        c37=(0,-0.95,0.26)
        c38=(0,-0.92,0.25)
        c39=(0,-0.73,0.2)
        c40=(0,-0.7,0.19)
        c41=(0,-0.67,0.31)
        c42=(0,-0.6,0.42)
        c43=(0,-0.51,0.51)
        c44=(0,-0.53,0.53)
        c45=(0,-0.68,0.68)
        c46=(0,-0.7,0.7)
        c47=(0,-0.57,0.83)
        c48=(0,-0.42,0.91)
        c49=(0,-0.26,0.95)
        c50=(0,-0.25,0.93)
        c51=(0,-0.19,0.73)
        c52=(0,-0.19,0.7)
        c53=(0,-0.06,0.73)
        c54=(0,0.06,0.73)
        c55=(0,0.19,0.7)
        c56=(0,0.19,0.73)
        c57=(0,0.25,0.93)
        c58=(0,0.26,0.95)
        c59=(0,0.42,0.91)
        c60=(0,0.57,0.83)
        c61=(0,0.7,0.7)
        c62=(0,0.68,0.68)
        c63=(0,0.53,0.53)
        c64=(0,0.51,0.51)
        c65=(0,0.6,0.42)
        c66=(0,0.67,0.31)
        c67=(0,0.7,0.19)
        c68=(0,0.73,0.2)
        c69=(0,0.92,0.25)
        c70=(0,0.95,0.26)
        c71=(0,1,0.09)
        points=[c00,c01,c02,c03,c04,c05,c06,c07,c08,c09,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38,c39,c40,c41,c42,c43,c44,c45,c46,c47,c48,c49,c50,c51,c52,c53,c54,c55,c56,c57,c58,c59,c60,c61,c62,c63,c64,c65,c66,c67,c68,c69,c70,c71,c00,c01,c02]
        curve_gear=self.degresscubic_create_curve(points,name=name+"1")
        
        pizza=0.5/2
        point_circle=[]
        for i in range(2*4+3):
            vartex=(0,math.cos(math.pi*(pizza*i))*1*0.5,math.sin(math.pi*(pizza*i))*1*0.5)
            point_circle.append(vartex)
        curve_circle=self.degresscubic_create_curve(point_circle,name=name+"2")

        curves=[curve_gear,curve_circle]
        curve=self.parentcurve_create_curve(curves=curves,name=name)
        return curve

    def lens_create_curve(self,name):
        a00=(0,0.35,0)
        a01=(0,0.39,-0.11)
        a02=(0,0.56,-0.5)
        a03=(0,0.39,-0.89)
        a04=(0,0,-1.06)
        a05=(0,-0.39,-0.89)
        a06=(0,-0.56,-0.5)
        a07=(0,-0.39,-0.11)
        a08=(0,0,0)
        a09=(0,-0.39,0.11)
        a10=(0,-0.56,0.5)
        a11=(0,-0.39,0.89)
        a12=(0,0,1.06)
        a13=(0,0.39,0.89)
        a14=(0,0.56,0.5)
        a15=(0,0.39,0.11)
        points=[a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a00,a01,a02]
        curve=self.degresscubic_create_curve(points,name)
        return curve

class EditCurve(sbLB.BasePair):
    def __init__(self):
        self._sourceNode=""
        self._targetNode=""

#Public Function
    def replaceShape(self):
        self.replaceShape_edit_func(self._sourceNode,self._targetNode)

#Multi Function
    def replaceShape_edit_func(self,sourceNode,targetNode):
        shapes=self.getShapes_edit_shapes(targetNode)
        if not shapes == None:
            cmds.delete(shapes)
        self.setShapes_edit_func(sourceNode,targetNode)

#Single Function
    def renameShapes_edit_func(self,node):
        shapes=cmds.listRelatives(node,f=True,type='nurbsCurve')
        for shape in shapes:
            shape=cmds.rename(shape,node+"Shape")

    def getShapes_edit_shapes(self,node):
        shapes=cmds.listRelatives(node,type='nurbsCurve')
        return shapes

    def setShapes_edit_func(self,sourceNode,targetNode):
        copy_list=cmds.duplicate(sourceNode)
        shapes=cmds.listRelatives(copy_list[0],f=True,type='nurbsCurve')
        for shape in shapes:
            shape=cmds.rename(shape,targetNode+"Shape")
            cmds.parent(shape,targetNode,r=True,s=True)
        cmds.delete(copy_list)
