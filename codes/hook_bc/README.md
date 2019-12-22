# Python Import Hooker

1. Doc of Import: [https://docs.python.org/3/reference/import.html]
2. Explanation:
   1. when `import`ing, Python uses `importlib.abc.Finder`s `sys.meta_path` to find a
   `importlib._bootstrap.ModuleSpec`.
   2. `importlib._bootstrap.ModuleSpec` has a method `loader` typed  `importlib.abc.Loader` to
   specify the behaviour of how to load the module.
   3. the corresponding `Loader` creates a `importlib._bootstrap.ModuleSpec` by the method `create_module`,
   and executes it later to create an actual module by `exec_module`.  