# Edited In 6 June
# -*-coding:utf-8-*-
"""
Author:@Aydenegg Shaw  and  _______
Mail:xiaojzh7@mail2.sysu.edu.cn and ______

"""

import argparse #Terminal Args Parser
import click    #Terminal Args Parser
import getpass  
import matplotlib.pyplot as plt
import numpy as np 
import os
import os.path as op
import pysnooper #A specaial function Debugger

#TODO make this file a module!

'''
#==========
Field of Argparser
支持默认秘钥和默认模式
基本的错误处理（没有提供输入文本的情况，以及提供了无法识别的参数的情况）
出错时或者不带任何参数调用脚本时会显示文档：
#==========
'''

#parser = argparse.Add_argpaer(description='Fuck this', usage='do something')
'''
#==========
Field of Global vars
#==========
'''
def startwith(obj:str, tobecmp:list):
    """
    Return True if obj starts with any one in to be compare list,
    e.g:
    ['SHUT DOWN', 'POWEROFF', 'EXIT']
    stdin-->"poweroff the fucking prog"
    return True
    """
    for item in tobecmp:
        if obj.startswith(item):
            return True

    return False




class DataKit:
    #TODO：Determine what methods shoule be included.
    #TODO: Determine 
    def __init__(self, ):
        pass

    def __repr__(self):
        #TODO a better way to show an instance.    
        pass

    def __str__(self):
        pass

    def _platform(self):
        #Check for the platform: Posix or NT
        pass

    def _Private(self):
        pass

    def wave_process(self, wave_file):
        """
        Use Scipy, Numpy and Matplot to Draw the animation of the target wave file
        """


        pass
    def rex_match(self, expr, file):
        #Search Or replace in the file, by Regex matching
        pass

    def shower(self, data, file, format):#等下加入自动类型判断测试一下
        pass



class RegexMatcher:
    pass

class CommandParser:
    #TODO try to make it a command parser, receiving some simple commands.
    #TODO Append an interface so that user can DIY the commands' format style
    def __init__(self, terminal_style):

        """
        formatstyle is a dict:
            action = 'Add'
            You can initializa the Command Parser instance
            with a DIY terminal tip style
            Or you can use CommandParser.add_style to add more style and use them 
        """

        self.user = getpass.getuser()
        self.curpath = op.abspath(op.curdir)
        tmp = os.popen('hostname').read()
        self.server = tmp.strip()
        self._cmd_styles = { 
            'UbDefault':' \033[32;40;92m{d.user}@{d.server}\033[0m:\033[34;40;94m{d.curpath}\033[0m$ ',
            'ArchDefault':' {d.user}@{d.server}->{d.curpath}$',
            'RHELDefault':' [{d.user}@{d.servre} ~]#'
        }
        if terminal_style not in self._cmd_styles:
            os.system('echo "Invalid style was examined and the style was set to ubuntustyle"')
            self._style = 'UbDefault'
        else:
            self._style = terminal_style
        self._fmt = self._cmd_styles[self._style]
        #Cannot use the root/administor

    '''    
    def __repr__(self):

        return self._fmt.format(d=self, self._style)
        #return format(self, 'UbDefault')
    '''        

    def __format__(self, format_style):
        if format_style not in self._cmd_styles:
            self.set_style('UbDefault')
        else:
            self._fmt = self._cmd_styles[format_style]
        return self._fmt.format(d=self)


    def set_style(self, spec_style):
        self._style = spec_style

    def new_styles(self, action='Not add', **kwargs):
        """
        DIY user's own formatting style
        """
        #TODO: Add a syntax checker for kwargs...
        if action.upper() in ['ADD', 'DIY', 'APPEND']:
            for key in kwargs.keys:
                if key in self._cmd_styles:
                    print(f"An existing style:{key} has been changed")
                self._cmd_styles[key] = kwargs[key]

    def add_styles(self, action='Not load', **kwargs):
        """
        add style from a json file
        """
        if action.upper() in ['ADD', 'DIT', 'APPEND']:
            pass


    def terminal(self, style):
        """
        Just using os.system() to do a simple terminal... 
        """
        cmd = input(format(self, self._cmd_styles[style]))
        #cmd = input("Commans:")
        shutlist = ['POWEROFF', 'SHUTDOWN', 'EXIT', ]
        while cmd:
            if startwith(cmd.upper(), shutlist):
                break
            else:
                os.system(cmd)
            cmd = input(format(self, self._cmd_styles[style]))
            #cmd = input("Enter Commands")

    """def printit(self):
        print(self._fmt)
        print(format(self, self._style))
"""

demo = CommandParser('UbDefault')
demo.terminal('RHELDefault')
print(demo)
print(format(demo))
print(demo.curpath, demo.user, demo.server, sep='\n\n')
