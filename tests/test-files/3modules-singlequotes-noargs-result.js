// Should ask for an argument if editing path1, but not for any others.
require([
    'path/1',
    'path/2',
    'path/3'
  ],
  function() {
    Mod1.doThing();
  }
);