#!/usr/bin/python

import time
import RPi.GPIO as GPIO

import motor.PiMotor as PiMotor

class MotorDriver():

    def __init__(self, isTestMode=False):
        self.Message = "I am Motor Driver"
        self.Motor1 = PiMotor.Motor("MOTOR1",1)
        self.Motor2 = PiMotor.Motor("MOTOR2",1)
        self.Motor3 = PiMotor.Motor("MOTOR3",1)
        self.Motor4 = PiMotor.Motor("MOTOR4",1)

        self.Motor1.test(isTestMode)
        self.Motor2.test(isTestMode)
        self.Motor3.test(isTestMode)
        self.Motor4.test(isTestMode)

        #To drive all motors together
        self.MotorAll = PiMotor.LinkedMotors(
            self.Motor1,
            self.Motor2,
            self.Motor3,
            self.Motor4
        )

        #Names for Individual Arrows
        self.ArrowBack = PiMotor.Arrow(1)
        self.ArrowLeft = PiMotor.Arrow(2)
        self.ArrowForward = PiMotor.Arrow(3) 
        self.ArrowRight = PiMotor.Arrow(4)

    def StopMotor(self):
        self.ArrowForward.off()
        self.ArrowBack.off()
        self.ArrowLeft.off()
        self.ArrowRight.off()

        self.MotorAll.stop()

    def Forward(self):
        speed =  20
        self.StopMotor()

        self.ArrowForward.on()
        self.Motor1.forward(speed)
        self.Motor2.forward(speed)

    def Backward(self):
        speed =  20
        self.StopMotor()

        self.ArrowBack.on()
        self.Motor1.reverse(speed)
        self.Motor2.reverse(speed)

    def TurnLeft(self):
        speed = 20

        self.ArrowLeft.on()
        self.Motor1.forward(speed)
        self.Motor2.reverse(speed)

    def TurnRight(self):
        speed = 20

        self.ArrowRight.on()
        self.Motor1.reverse(speed)
        self.Motor2.forward(speed)
        