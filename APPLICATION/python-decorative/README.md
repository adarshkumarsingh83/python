## python-decorative

This small example project demonstrates three simple service classes and two ways to time and wrap method execution: (1) an instance-level wrapper returned by a factory method, and (2) a decorator function applied with the `@` syntax.

**Files:**
- **`main.py`**: Project entry point. Creates instances of each service (`ServiceOne`, `ServiceTwo`, `ServiceThree`) and calls their task methods to demonstrate the timing wrappers.

- **`service/ServiceOne.py`**: A service implemented with an instance-level wrapper.
	- **`ServiceOne.__init__(name)`**: Constructor; stores the service `name`.
	- **`start()` / `stop()`**: Simple lifecycle methods that print start/stop messages and return `1`.
	- **`performTaskOne(name)`**: Simulates work by printing a message, sleeping for a random number of seconds, and returning `1`.
	- **`runFunctionInstance(startFunction, performFunction, stopFunction)`**: Factory that returns a `runFunction` closure which, when called, runs `startFunction()`, then `performFunction(...)`, then `stopFunction()` while measuring and printing total execution time. Example usage is in `main.py` where the returned function is invoked to wrap `ServiceOne`'s task.

- **`service/ServiceTwo.py`**: Demonstrates a decorator implemented as a nested function inside the class file.
	- **`ServiceTwo.__init__(name)`**: Constructor; stores the service `name`.
	- **`runFunctionInstance(performTaskTwo)`**: A decorator (defined as a plain function in the module) that wraps `performTaskTwo` with timing logic. It prints total execution time and returns `1` from the wrapper.
	- **`performTaskTwo(self, name)`**: Method annotated with `@runFunctionInstance` which calls `start()`, sleeps for a random interval to simulate work, then `stop()`.
	- **`start()` / `stop()`**: Lifecycle methods similar to `ServiceOne`.

- **`service/decorator/Decorator.py`**: Reusable decorator implementation used by `ServiceThree`.
	- **`runFunctionInstance(func)`**: A decorator that wraps `func` to print an entry message, measure execution time, print the elapsed time and an exit message, and return `1`.

- **`service/ServiceThree.py`**: Uses the reusable decorator from `service.decorator.Decorator`.
	- **`ServiceThree.__init__(name)`**: Constructor.
	- **`start()` / `stop()`**: Lifecycle methods.
	- **`performTaskThree(self, name)`** and **`performNewTask(self)`**: Both are decorated with `@runFunctionInstance` from `service.decorator.Decorator` and simulate work using `time.sleep(random.randint(1, 10))`.

**How it works**
- `ServiceOne` shows how to build a wrapper by returning a function closure that calls start/perform/stop and measures elapsed time. This is useful for per-instance, dynamic wrapping.
- `ServiceTwo` defines a decorator function in the same module and applies it with `@runFunctionInstance` to the method. The decorator measures runtime and prints it.
- `ServiceThree` imports the decorator from `service.decorator.Decorator` to demonstrate sharing a decorator across modules.

**Run**
- From the project root run:

```bash
python main.py
```

This will instantiate the three services and print start/stop messages and timing information for each task. Note: the tasks sleep for a random number of seconds (1–10) so runs will take several seconds.

**Notes & suggestions**
- The timing wrappers return `1` from wrapped functions; in a real project they might return the original function's return value instead of a constant.
- `ServiceOne.runFunctionInstance` defines `runFunction(self,*args, **kwargs)` but the outer signature doesn't enforce `self` — ensure correct binding when using the returned function.
- Consider replacing `time.sleep` with non-blocking or shorter simulated work for faster tests.

If you want, I can adjust the README to include example output, or modify the wrappers to preserve and return the original function's return value.


