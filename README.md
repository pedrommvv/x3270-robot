RF Library for x3270
Robot Framework Library for x3270 emulator automation

Installation and dependencies:
RobotFramework and py3270 module

Example:
Open 3270    ${hostname}
Input Text on Field    5     10     Text_content_here
Sleep     2s
${field_content}=     Get_String     5     20     16
Log     ${field_content}
Press_Enter

Please check Automation3270.htm for keyword documentation. Many more keywords are waiting to be created.

Contributors

Credits to Randy Syring for the py3270 module, that made this library possible.
https://groups.google.com/forum/#!forum/blazelibs
https://pypi.python.org/pypi/py3270/0.3.3



