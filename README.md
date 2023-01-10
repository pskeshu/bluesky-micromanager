# bluesky-micromanager
This is intended to be an interface for Micro-Manager in the bluesky ecosystem. 

Micro-Manager is a generic, open-source microscope control software intended for use with commercially available research microscopes. With its support for a large number of devices through its device abstraction layer, Micro-Manager is an attractive tool to integrate with existing device orchestration libraries to bring control innovations from other fields of instrument control into bioimaging.

# Micro-manager system architecture
The most basic object in the Micro-Manager system architecture to control a device is a "Device Adapter". The Device Adapter acts as an interface for the manufacturer's drivers and standardizes the API within the Micro-Manager system where individual devices are defined by the MMDevice object. The access to the devices are provided with MMCore which manages multiple MMDevices that can be a part of the microscope system and acts as an intermediate between the Device and the user.

![Micro-Manager system architecture](/images/mm_system_design.png "System design").

MMCore is implemented in C++. However, with SWIG, the interfaces can be accessed in scripting languages such as python.

