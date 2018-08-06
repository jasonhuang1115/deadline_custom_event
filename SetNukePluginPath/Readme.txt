This is a simple Deadline custom event plugin. 
To use it, copy/paste the SetNukePluginPath folder (along with content inside) to your Deadline repo.
 (ex. \\network..\\DeadlineRepo10\custom\events\SetNukePluginPath)
That's it.
When users submit Nuke jobs, an environment variable "NUKE_PATH" will be added with its value set to whatever path you specify.
The submitted Nuke job will pick up custom plugin/gizmos/scripts from the specified directory for rendering.