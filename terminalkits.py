# Edited In 6 June
# -*-coding:utf-8-*-
"""
Author:@Aydenegg Shaw  and  _______
Mail:xiaojzh7@mail2.sysu.edu.cn and ______

"""

import argparse #Terminal Args Parser
import click    #Terminal Args Parser
import getpass  
import os
import os.path as op
import pysnooper #A specaial function Debugger

import warnings
#Moduel built by myself
import datakits.testWaveKits
#TODO make this file a module!
#__all__ = []
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
#warnings.simplefilter('always')

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



class RegexMatcher:#It will be moved to the grepy module..
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
            To ensure many platform can use this emulating temrinal freely, I will modify this class in two weeks.
        """

        self.user = getpass.getuser()
        self.curpath = op.abspath(op.curdir)
        tmp = os.popen('hostname').read()
        self.server = tmp.strip()
        self._cmd_styles = { 
            'UbDefault':'\033[32;40;92m{d.user}@{d.server}\033[0m:\033[34;40;94m{d.curpath}\033[0m$ ',
            'ArchDefault':'\033[32;41;91m{d.user}@{d.server}\033[0m->\033[34;40;94m{d.curpath}\033[0m#',
            'RHELDefault':' [{d.user}@{d.servre} {d.curpath} ~]#'
        }
        self._Messages = {
    'WarningStyle':'Invalid style has been examined. ',
    'WarningStyleReset':'The current style was set to the default UbDefault Style',
}
        self._io_style_valid(terminal_style, auto_fix=True)
        #Cannot use the root/administor
    
    '''    
    def __repr__(self):

        return self._fmt.format(d=self, self._style)
        #return format(self, 'UbDefault')
    '''        
    def _io_style_valid(self, style, auto_fix=False):
        if style not in self._cmd_styles.keys():
            #os.system('echo "Invalid style was examined and the style was set to previous style"')
            
            if auto_fix:
                warnings.warn(self._Messages['WarningStyleReset'])
                self._style = 'UbDefault'
            else:
                warnings.warn(self._Messages['WarningStyle'])
        else:
            self._style = style
        self._fmt = self._cmd_styles[self._style]
    def _load_style_check(self, styles:str):
        """Check the styles. If it is invalid, print messages, and return False"""
        res = 0
        if res:
            warnings.warn(self._Messages['WarningStyle'])
            return False
            pass

    def __format__(self, format_style):
        if format_style not in self._cmd_styles:
            self.set_style('UbDefault')
        else:
            self._fmt = self._cmd_styles[format_style]
        return self._fmt.format(d=self)


    def set_style(self, spec_style):
        self._io_style_valid(spec_style, auto_fix=False)


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

    '''Lock it temporatly..
    def add_styles(self, action='Not load', file):
        """
        add style from a json file
        """
        if action.upper() in ['ADD', 'DIT', 'APPEND']:
            #Read the file Using For loop!
            for i in range(5):#Take this for example..
                print(i)
                if self._load_style_check():
                    pass
            
        pass
    '''
        


    def terminal(self):
        """
        Just using os.system() to do a simple terminal... 
        """

        cmd = input(format(self, self._cmd_styles[self._style]))
        #cmd = input("Commans:")
        shutlist = ['POWEROFF', 'SHUTDOWN', 'EXIT', ]
        while cmd:
            if startwith(cmd.upper(), shutlist):
                break
            else:
                os.system(cmd)
            cmd = input(format(self, self._cmd_styles[self._style]))
            #cmd = input("Enter Commands")


    def change_os():
        #TODO Difficult!!! change wsl terminal<->powershell in this program
        """
        os.system里面的访问效率低，以后尝试一下能不能直接用远程连接的方式
        """
        pass

if __name__ == '__main__':
    """Doing Some Tests...."""
    demo = CommandParser('UbDefault')
    demo.terminal()
    print(demo)
    print(format(demo))
    print(demo.curpath, demo.user, demo.server, sep='\n\n')
    demo.set_style('ArchDefault')
    demo.terminal()
    demo.set_style('REHLDefault')
    demo.terminal()
