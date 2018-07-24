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
###############################################################
def GetDeadlineEventListener():
    return SetNukePluginPathListener()

def CleanupDeadlineEventListener(eventListener):
    eventListener.Cleanup()


###############################################################
#  The SetNukePluginPath event listener class.
###############################################################
class SetNukePluginPathListener (DeadlineEventListener):
    def __init__(self):
        self.OnJobSubmittedCallback += self.OnJobSubmitted
        # self.OnJobStartedCallback += self.OnJobStarted
        
    # def OnJobStarted(self, job):
    #     eventType = self.GetConfigEntryWithDefault( "SetNukePluginPath", "On Job Started" )
    #     if 'Nuke' in job.PluginName and ( eventType == "On Job Started" ):
    #         myDir = r"//lax04rend/Nikola/library/scripts/nuke"
    #         print (myDir)
    #         job.JobCustomPluginDirectory=myDir
        
    #     RepositoryUtils.SaveJob(job)      
    #     pass
        
    def OnJobSubmitted(self, job):
        eventType = self.GetConfigEntryWithDefault( "SetNukePluginPath", "On Job Submitted" )
        if 'Nuke' in job.PluginName and ( eventType == "On Job Submitted" ):
            myDir = r"\\lax04rend\Nikola\library\scripts\nuke"
            print (myDir)
            job.JobCustomPluginDirectory=myDir
            job.SetJobEnvironmentKeyValue("NUKE_PATH", myDir)
        
        RepositoryUtils.SaveJob(job)
        pass
        
