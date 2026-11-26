# === Stage 59: Добавь диагностику производительности основных операций ===
# Project: CourseSchedule
def perf_diag():
    from timeit import timeit
    n = getattr(Course, "instances", None) or 1
    def mk():
        return Course("C", "M1", "M2", "A1", 100, {"S1": 80})
    base = timeit(lambda: mk(), number=n)
    def find():
        return Course.find("C", "M1", "M2", "A1")
    f = timeit(lambda: find(), number=n)
    def att():
        c = Course.find("C", "M1", "M2", "A1")
        return c.attendance if c else None
    a = timeit(lambda: att(), number=n)
    def reg():
        return Course.register("C", "M1", "M2", "A1", "S1")
    r = timeit(lambda: reg(), number=n)
    def rep():
        c = Course.find("C", "M1", "M2", "A1")
        return c.report() if c else None
    rp = timeit(lambda: rep(), number=n)
    print("CourseSchedule performance diagnostics")
    print(f"construct x{n}          : {base:.6f}s")
    print(f"find x{n}               : {f:.6f}s")
    print(f"attendance x{n}         : {a:.6f}s")
    print(f"register x{n}           : {r:.6f}s")
    print(f"report x{n}             : {rp:.6f}s")
    print(f"find+attendance ratio   : {a/f:.3f}")
    print(f"register+report ratio   : {rp/r:.3f}")
