# -pyterminal_
an linux-style py terminal in windows10, for convinience.
# PyTerminal_日志

[toc]

# 预期

补充一下windows下的命令行功能（顺便练手py），虽然我一般都用wsl和live发行版的linux但有时还是得用别人的电脑，这个文件我计划随时拷在移动软盘里。

语句尽量贴近linux终端风格，做适当的调整

利用py脚本语言特性，命令行里面的vi来写简短的py脚本（我还没学bashTAT)





## ver21-05-06

规划



两种帮助文档：

1. 在调用pyterminal.py的时候，用-h
2. 在启动后，采用man

man的样式，以ubuntu下的`man cal`为例

```shell
CAL(1)                               BSD General Commands Manual                               CAL(1)

NAME
     cal, ncal — displays a calendar and the date of Easter

SYNOPSIS
     cal [-31jy] [-A number] [-B number] [-d yyyy-mm] [[month] year]
     cal [-31j] [-A number] [-B number] [-d yyyy-mm] -m month [year]
     ncal [-C] [-31jy] [-A number] [-B number] [-d yyyy-mm] [[month] year]
     ncal [-C] [-31j] [-A number] [-B number] [-d yyyy-mm] -m month [year]
     ncal [-31bhjJpwySM] [-A number] [-B number] [-H yyyy-mm-dd] [-d yyyy-mm] [-s country_code]
         [[month] year]
     ncal [-31bhJeoSM] [-A number] [-B number] [-d yyyy-mm] [year]

DESCRIPTION
     The cal utility displays a simple calendar in traditional format and ncal offers an alternative
     layout, more options and the date of Easter.  The new format is a little cramped but it makes a
     year fit on a 25x80 terminal.  If arguments are not specified, the current month is displayed.

     The options are as follows:

     -h      Turns off highlighting of today.

     -J      Display Julian Calendar, if combined with the -o option, display date of Orthodox Easter
             according to the Julian Calendar.

     -e      Display date of Easter (for western churches).

     -j      Display Julian days (days one-based, numbered from January 1).

     -m month
             Display the specified month.  If month is specified as a decimal number, appending ‘f’
             or ‘p’ displays the same month of the following or previous year respectively.

     -o      Display date of Orthodox Easter (Greek and Russian Orthodox Churches).

     -p      Print the country codes and switching days from Julian to Gregorian Calendar as they are
             assumed by ncal.  The country code as determined from the local environment is marked
             with an asterisk.

     -s country_code
             Assume the switch from Julian to Gregorian Calendar at the date associated with the
             country_code.  If not specified, ncal tries to guess the switch date from the local
             environment or falls back to September 2, 1752.  This was when Great Britain and her
             colonies switched to the Gregorian Calendar.

     -w      Print the number of the week below each week column.

     -y      Display a calendar for the specified year. This option is implied when a year but no
             month are specified on the command line.

     -3      Display the previous, current and next month surrounding today.

     -1      Display only the current month. This is the default.

     -A number
```



