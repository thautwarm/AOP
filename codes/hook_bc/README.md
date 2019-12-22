# Python Import Hooker

1. [documentation of import](https://docs.python.org/3/reference/import.html)
2. Explanation:
   1. when `import`ing, Python uses `importlib.abc.Finder`s `sys.meta_path` to find a
   `importlib._bootstrap.ModuleSpec`.
   2. `importlib._bootstrap.ModuleSpec` has a method `loader` typed  `importlib.abc.Loader` to
   specify the behaviour of how to load the module.
   3. the corresponding `Loader` creates a `importlib._bootstrap.ModuleSpec` by the method `create_module`,
   and executes it later to create an actual module by `exec_module`.
   
## Example

Check spec.py:

First, import the hooker functions.

```python
from codes.hook_bc.hook_bc import within
```

Next, given a scope, apply hooking. 
```python
with within():
```

Then, perform our metaprogramming operation on the whole module `codes.hook_bc.examplar`.
```
import codes.hook_bc.examplar
```

Specifically, we rewrite the bytecode instructions of the module `codes.hook_bc.examplar`,
as a result, when Python interpreter is interpreting a instruction `i` from the module `codes.hook_bc.examplar`,
the latest task Python interpreter did is printing `i`.  


```python
def f(x):
    return x + 1


a = print(f(1))
```

produces

```
<LOAD_CONST arg=<code object f at 0x000001E57D8078A0, file "C:\Users\twshe\Desktop\works\AOP\codes\hook_bc\examplar.py", line 1> lineno=1>
<LOAD_CONST arg='f' lineno=1>
<MAKE_FUNCTION arg=0 lineno=1>
<STORE_NAME arg='f' lineno=1>
<LOAD_NAME arg='print' lineno=5>
<LOAD_NAME arg='f' lineno=5>
<LOAD_CONST arg=1 lineno=5>
<CALL_FUNCTION arg=1 lineno=5>
<CALL_FUNCTION arg=1 lineno=5>
2
<STORE_NAME arg='a' lineno=5>
<LOAD_CONST arg=None lineno=5>
<RETURN_VALUE lineno=5>
```
