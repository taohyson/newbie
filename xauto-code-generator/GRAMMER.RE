Grammer:

<Macro>$variable,$ctx</Macro>=''' + eval($variable, $ctx) + '''
<MacroFunc>$variable<MacroCtx>$cxt</MacroCtx></MacroFunc>=eval($variable, $ctx)
<MacroRepeat>$variable<Context>$cxt</Context></MacroRepeat>=res='';for i in range(len(array)):res+=eval($variable, {"item": array[i]});res
