###############################################################
#  Imports
###############################################################
import os

from System.Diagnostics import *
from System.IO import *

from Deadline.Events import *
from Deadline.Scripting import *


###############################################################
#  Give Deadline an instance of this class so it can use it.
#  If you've dug around the repository, you'll notice I poached
#  this from our Draft code.
###############################################################
def GetDeadlineEventListener():
    return SetNukePluginPathListener()

def CleanupDeadlineEventListener(eventListener):
    eventListener.Cleanup()


###############################################################
#  The Draft event listener class.
###############################################################
class SetNukePluginPathListener (DeadlineEventListener):
    def __init__(self):
        self.OnJobSubmittedCallback += self.OnJobSubmitted
        self.OnJobStartedCallback += self.OnJobStarted
    
        
    def OnJobStarted(self, job):
        self.CustomPluginDirectory='//lax04rend/Nikola/library/scripts/nuke'
        # eventType = self.GetConfigEntryWithDefault( "SetNukePluginPathProperty", "On Job Started" )

        # if 'Nuke' in job.PluginName and ( eventType == "On Job Started" or eventType == "On Job Started and On Job Finished" ):
        #     self.CustomPluginDirectory='//lax04rend/Nikola/library/scripts/nuke'
        #     #self.RemoveFiles( job )
        pass
        
    def OnJobSubmitted(self, job):
        self.CustomPluginDirectory='//lax04rend/Nikola/library/scripts/nuke'
        # eventType = self.GetConfigEntryWithDefault( "SetNukePluginPathProperty", "On Job Started" )
        # if 'Nuke' in job.PluginName and ( eventType == "On Job Started" or eventType == "On Job Started and On Job Finished" ):
        #     self.CustomPluginDirectory='//lax04rend/Nikola/library/scripts/nuke'
        #     #self.RemoveFiles( job )
        pass
        
