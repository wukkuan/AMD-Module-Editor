// In this case, the missing module is fine, but it shouldn't reappear if a new
// one isn't added.
require(['path/1', 'path/2', 'path/3'],
  function(Mod1, Mod2) {
    Mod1.doThing();
  }
);